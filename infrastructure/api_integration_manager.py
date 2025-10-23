"""
CodeVerter API Integration Manager

This module provides unified interfaces for all supported AI services with intelligent
routing, error handling, and performance optimization.
"""

import asyncio
import json
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any, Union
import aiohttp
import logging
from datetime import datetime, timedelta

# SERAPHINA Framework imports
from federation_router import FederationRouter


class APIStatus(Enum):
    """API service status"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    DOWN = "down"
    RATE_LIMITED = "rate_limited"
    UNKNOWN = "unknown"


@dataclass
class APICredentials:
    """Secure credential storage for API services"""
    service_name: str
    api_key: str
    endpoint_url: str
    additional_headers: Dict[str, str] = field(default_factory=dict)
    rate_limit: int = 100  # requests per minute
    cost_per_request: float = 0.0


@dataclass
class APICallResult:
    """Result from an API call"""
    success: bool
    response_data: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    response_time: float = 0.0
    cost: float = 0.0
    tokens_used: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RateLimitInfo:
    """Rate limiting information"""
    requests_per_minute: int
    current_count: int
    reset_time: datetime
    
    def can_make_request(self) -> bool:
        """Check if we can make another request"""
        if datetime.now() > self.reset_time:
            self.current_count = 0
            self.reset_time = datetime.now() + timedelta(minutes=1)
        
        return self.current_count < self.requests_per_minute


class BaseAPIAdapter(ABC):
    """Base class for all API adapters"""
    
    def __init__(self, credentials: APICredentials):
        self.credentials = credentials
        self.status = APIStatus.UNKNOWN
        self.last_health_check = None
        self.rate_limit_info = RateLimitInfo(
            requests_per_minute=credentials.rate_limit,
            current_count=0,
            reset_time=datetime.now() + timedelta(minutes=1)
        )
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Circuit breaker state
        self.failure_count = 0
        self.last_failure_time = None
        self.circuit_open = False
        
        # Performance metrics
        self.total_requests = 0
        self.successful_requests = 0
        self.total_response_time = 0.0
        self.total_cost = 0.0
    
    @abstractmethod
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> APICallResult:
        """Transform code using this API"""
        pass
    
    @abstractmethod
    async def health_check(self) -> APIStatus:
        """Check if the API is healthy"""
        pass
    
    async def check_rate_limit(self) -> bool:
        """Check if we're within rate limits"""
        return self.rate_limit_info.can_make_request()
    
    def update_circuit_breaker(self, success: bool):
        """Update circuit breaker state based on request success"""
        if success:
            self.failure_count = 0
            self.circuit_open = False
        else:
            self.failure_count += 1
            self.last_failure_time = datetime.now()
            
            # Open circuit after 5 consecutive failures
            if self.failure_count >= 5:
                self.circuit_open = True
                self.logger.warning(f"Circuit breaker opened for {self.credentials.service_name}")
    
    def can_make_request(self) -> bool:
        """Check if we can make a request (rate limit + circuit breaker)"""
        # Check circuit breaker
        if self.circuit_open:
            # Try to close circuit after 1 minute
            if (self.last_failure_time and 
                datetime.now() - self.last_failure_time > timedelta(minutes=1)):
                self.circuit_open = False
                self.failure_count = 0
                self.logger.info(f"Circuit breaker closed for {self.credentials.service_name}")
            else:
                return False
        
        # Check rate limit
        return self.check_rate_limit()
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics for this adapter"""
        avg_response_time = (self.total_response_time / self.total_requests 
                           if self.total_requests > 0 else 0)
        success_rate = (self.successful_requests / self.total_requests 
                       if self.total_requests > 0 else 0)
        
        return {
            "service_name": self.credentials.service_name,
            "status": self.status.value,
            "total_requests": self.total_requests,
            "success_rate": success_rate,
            "avg_response_time": avg_response_time,
            "total_cost": self.total_cost,
            "circuit_open": self.circuit_open,
            "failure_count": self.failure_count
        }


class GeminiFlashAdapter(BaseAPIAdapter):
    """Adapter for Gemini Flash 1.5"""
    
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> APICallResult:
        """Transform code using Gemini Flash"""
        if not self.can_make_request():
            return APICallResult(
                success=False,
                error_message="Rate limited or circuit breaker open"
            )
        
        start_time = time.time()
        self.total_requests += 1
        self.rate_limit_info.current_count += 1
        
        try:
            # Prepare request payload optimized for Gemini Flash (speed focus)
            prompt = self._build_speed_optimized_prompt(code, source_lang, target_lang, requirements)
            
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.credentials.api_key}",
                    "Content-Type": "application/json",
                    **self.credentials.additional_headers
                }
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }],
                    "generationConfig": {
                        "temperature": 0.1,  # Low temperature for consistency
                        "maxOutputTokens": 4096,
                        "topK": 1,
                        "topP": 0.8
                    }
                }
                
                async with session.post(
                    self.credentials.endpoint_url,
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    response_time = time.time() - start_time
                    self.total_response_time += response_time
                    
                    if response.status == 200:
                        data = await response.json()
                        transformed_code = self._extract_code_from_response(data)
                        
                        self.successful_requests += 1
                        self.update_circuit_breaker(True)
                        
                        cost = self._calculate_cost(len(code), len(transformed_code))
                        self.total_cost += cost
                        
                        return APICallResult(
                            success=True,
                            response_data={
                                "code": transformed_code,
                                "explanation": "Fast transformation using Gemini Flash",
                                "confidence": 0.85,
                                "suggestions": ["Consider further optimization"],
                                "metadata": {"model": "gemini-flash-1.5"}
                            },
                            response_time=response_time,
                            cost=cost,
                            tokens_used=len(code.split()) + len(transformed_code.split())
                        )
                    else:
                        self.update_circuit_breaker(False)
                        error_text = await response.text()
                        return APICallResult(
                            success=False,
                            error_message=f"HTTP {response.status}: {error_text}",
                            response_time=response_time
                        )
                        
        except Exception as e:
            response_time = time.time() - start_time
            self.total_response_time += response_time
            self.update_circuit_breaker(False)
            
            return APICallResult(
                success=False,
                error_message=str(e),
                response_time=response_time
            )
    
    async def health_check(self) -> APIStatus:
        """Check Gemini Flash health"""
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.credentials.api_key}",
                    **self.credentials.additional_headers
                }
                
                # Simple health check request
                async with session.get(
                    f"{self.credentials.endpoint_url}/health",
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    if response.status == 200:
                        self.status = APIStatus.HEALTHY
                    elif response.status == 429:
                        self.status = APIStatus.RATE_LIMITED
                    else:
                        self.status = APIStatus.DEGRADED
                        
        except Exception:
            self.status = APIStatus.DOWN
        
        self.last_health_check = datetime.now()
        return self.status
    
    def _build_speed_optimized_prompt(self, code: str, source_lang: str, 
                                    target_lang: str, requirements: List[str]) -> str:
        """Build prompt optimized for speed"""
        req_text = "\n".join(requirements) if requirements else ""
        
        return f"""Transform this {source_lang} code to {target_lang}. Focus on speed and correctness.

Requirements:
{req_text}

Source Code:
```{source_lang}
{code}
```

Respond with only the transformed code in ```{target_lang} blocks."""
    
    def _extract_code_from_response(self, data: Dict) -> str:
        """Extract code from Gemini response"""
        try:
            content = data["candidates"][0]["content"]["parts"][0]["text"]
            # Extract code from markdown blocks
            if f"```" in content:
                start = content.find("```") + 3
                # Skip language identifier
                start = content.find("\n", start) + 1
                end = content.find("```", start)
                return content[start:end].strip()
            return content.strip()
        except (KeyError, IndexError):
            return ""
    
    def _calculate_cost(self, input_length: int, output_length: int) -> float:
        """Calculate cost for Gemini Flash (optimized pricing)"""
        # Simplified cost calculation
        input_tokens = input_length // 4  # Rough token estimation
        output_tokens = output_length // 4
        return (input_tokens * 0.00001) + (output_tokens * 0.00002)  # Example rates


class GeminiProAdapter(BaseAPIAdapter):
    """Adapter for Gemini Pro 2.5"""
    
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> APICallResult:
        """Transform code using Gemini Pro with deep analysis"""
        if not self.can_make_request():
            return APICallResult(
                success=False,
                error_message="Rate limited or circuit breaker open"
            )
        
        start_time = time.time()
        self.total_requests += 1
        self.rate_limit_info.current_count += 1
        
        try:
            # Prepare request with deep analysis focus
            prompt = self._build_deep_analysis_prompt(code, source_lang, target_lang, requirements)
            
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.credentials.api_key}",
                    "Content-Type": "application/json",
                    **self.credentials.additional_headers
                }
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }],
                    "generationConfig": {
                        "temperature": 0.3,  # Higher temperature for creativity
                        "maxOutputTokens": 8192,
                        "topK": 5,
                        "topP": 0.9
                    }
                }
                
                async with session.post(
                    self.credentials.endpoint_url,
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)  # Longer timeout for deep analysis
                ) as response:
                    response_time = time.time() - start_time
                    self.total_response_time += response_time
                    
                    if response.status == 200:
                        data = await response.json()
                        result = self._parse_detailed_response(data)
                        
                        self.successful_requests += 1
                        self.update_circuit_breaker(True)
                        
                        cost = self._calculate_cost(len(code), len(result["code"]))
                        self.total_cost += cost
                        
                        return APICallResult(
                            success=True,
                            response_data=result,
                            response_time=response_time,
                            cost=cost,
                            tokens_used=len(code.split()) + len(result["code"].split())
                        )
                    else:
                        self.update_circuit_breaker(False)
                        error_text = await response.text()
                        return APICallResult(
                            success=False,
                            error_message=f"HTTP {response.status}: {error_text}",
                            response_time=response_time
                        )
                        
        except Exception as e:
            response_time = time.time() - start_time
            self.total_response_time += response_time
            self.update_circuit_breaker(False)
            
            return APICallResult(
                success=False,
                error_message=str(e),
                response_time=response_time
            )
    
    async def health_check(self) -> APIStatus:
        """Check Gemini Pro health"""
        # Similar to Flash but with different endpoints
        return await super().health_check()
    
    def _build_deep_analysis_prompt(self, code: str, source_lang: str, 
                                  target_lang: str, requirements: List[str]) -> str:
        """Build prompt for deep architectural analysis"""
        req_text = "\n".join(requirements) if requirements else ""
        
        return f"""Perform a comprehensive transformation of this {source_lang} code to {target_lang}.

Analyze the code for:
1. Architecture patterns and design principles
2. Performance optimization opportunities  
3. Security considerations
4. Maintainability improvements
5. Best practices for {target_lang}

Requirements:
{req_text}

Source Code:
```{source_lang}
{code}
```

Provide:
1. Transformed code
2. Detailed explanation of changes
3. Architecture recommendations
4. Performance considerations
5. Security improvements made

Format your response as JSON:
{{
  "code": "transformed code here",
  "explanation": "detailed explanation",
  "architecture_notes": "architectural improvements",
  "performance_notes": "performance optimizations",
  "security_notes": "security enhancements",
  "suggestions": ["list of additional suggestions"]
}}"""
    
    def _parse_detailed_response(self, data: Dict) -> Dict[str, Any]:
        """Parse detailed response from Gemini Pro"""
        try:
            content = data["candidates"][0]["content"]["parts"][0]["text"]
            
            # Try to parse as JSON first
            if content.strip().startswith("{"):
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    pass
            
            # Fallback to text parsing
            return {
                "code": self._extract_code_block(content),
                "explanation": "Comprehensive transformation with architectural improvements",
                "confidence": 0.95,
                "suggestions": ["Consider additional testing", "Review performance"],
                "metadata": {"model": "gemini-pro-2.5", "analysis_type": "deep"}
            }
            
        except (KeyError, IndexError):
            return {
                "code": "",
                "explanation": "Failed to parse response",
                "confidence": 0.0,
                "suggestions": [],
                "metadata": {"error": "parsing_failed"}
            }
    
    def _extract_code_block(self, content: str) -> str:
        """Extract code block from response"""
        if "```" in content:
            start = content.find("```") + 3
            start = content.find("\n", start) + 1
            end = content.find("```", start)
            return content[start:end].strip()
        return content.strip()
    
    def _calculate_cost(self, input_length: int, output_length: int) -> float:
        """Calculate cost for Gemini Pro (premium pricing)"""
        input_tokens = input_length // 4
        output_tokens = output_length // 4
        return (input_tokens * 0.0001) + (output_tokens * 0.0002)  # Higher rates for Pro


class ClaudeAdapter(BaseAPIAdapter):
    """Adapter for Claude Sonnet"""
    
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> APICallResult:
        """Transform code using Claude with focus on clarity and documentation"""
        if not self.can_make_request():
            return APICallResult(
                success=False,
                error_message="Rate limited or circuit breaker open"
            )
        
        start_time = time.time()
        self.total_requests += 1
        self.rate_limit_info.current_count += 1
        
        try:
            prompt = self._build_documentation_focused_prompt(code, source_lang, target_lang, requirements)
            
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.credentials.api_key}",
                    "Content-Type": "application/json",
                    "anthropic-version": "2023-06-01",
                    **self.credentials.additional_headers
                }
                
                payload = {
                    "model": "claude-3-sonnet-20240229",
                    "max_tokens": 4096,
                    "temperature": 0.2,
                    "messages": [{
                        "role": "user",
                        "content": prompt
                    }]
                }
                
                async with session.post(
                    self.credentials.endpoint_url,
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=45)
                ) as response:
                    response_time = time.time() - start_time
                    self.total_response_time += response_time
                    
                    if response.status == 200:
                        data = await response.json()
                        result = self._parse_claude_response(data)
                        
                        self.successful_requests += 1
                        self.update_circuit_breaker(True)
                        
                        cost = self._calculate_cost(len(code), len(result["code"]))
                        self.total_cost += cost
                        
                        return APICallResult(
                            success=True,
                            response_data=result,
                            response_time=response_time,
                            cost=cost,
                            tokens_used=data.get("usage", {}).get("total_tokens", 0)
                        )
                    else:
                        self.update_circuit_breaker(False)
                        error_text = await response.text()
                        return APICallResult(
                            success=False,
                            error_message=f"HTTP {response.status}: {error_text}",
                            response_time=response_time
                        )
                        
        except Exception as e:
            response_time = time.time() - start_time
            self.total_response_time += response_time
            self.update_circuit_breaker(False)
            
            return APICallResult(
                success=False,
                error_message=str(e),
                response_time=response_time
            )
    
    async def health_check(self) -> APIStatus:
        """Check Claude health"""
        return await super().health_check()
    
    def _build_documentation_focused_prompt(self, code: str, source_lang: str,
                                          target_lang: str, requirements: List[str]) -> str:
        """Build prompt focused on clarity and documentation"""
        req_text = "\n".join(requirements) if requirements else ""
        
        return f"""Transform this {source_lang} code to {target_lang} with a focus on code clarity, readability, and comprehensive documentation.

Key objectives:
1. Maintain code functionality while improving readability
2. Add clear, helpful comments and documentation
3. Use idiomatic {target_lang} patterns
4. Ensure code is self-explanatory
5. Follow best practices for maintainability

Requirements:
{req_text}

Source Code:
```{source_lang}
{code}
```

Please provide:
1. The transformed, well-documented code
2. A clear explanation of the transformation approach
3. Documentation of any assumptions made
4. Suggestions for further improvements

Focus on making the code as clear and maintainable as possible."""
    
    def _parse_claude_response(self, data: Dict) -> Dict[str, Any]:
        """Parse Claude response"""
        try:
            content = data["content"][0]["text"]
            
            return {
                "code": self._extract_code_from_text(content),
                "explanation": self._extract_explanation(content),
                "confidence": 0.92,
                "suggestions": self._extract_suggestions(content),
                "metadata": {
                    "model": "claude-sonnet",
                    "focus": "documentation_clarity"
                }
            }
            
        except (KeyError, IndexError):
            return {
                "code": "",
                "explanation": "Failed to parse Claude response",
                "confidence": 0.0,
                "suggestions": [],
                "metadata": {"error": "parsing_failed"}
            }
    
    def _extract_code_from_text(self, content: str) -> str:
        """Extract code from Claude's response"""
        # Claude typically formats code in markdown blocks
        if "```" in content:
            start = content.find("```") + 3
            start = content.find("\n", start) + 1
            end = content.find("```", start)
            return content[start:end].strip()
        return ""
    
    def _extract_explanation(self, content: str) -> str:
        """Extract explanation from Claude's response"""
        # Look for explanation sections
        lines = content.split("\n")
        explanation_lines = []
        
        for line in lines:
            if ("explanation" in line.lower() or 
                "approach" in line.lower() or
                "transformation" in line.lower()):
                explanation_lines.append(line)
        
        return "\n".join(explanation_lines) if explanation_lines else "Clear, well-documented transformation"
    
    def _extract_suggestions(self, content: str) -> List[str]:
        """Extract suggestions from Claude's response"""
        suggestions = []
        lines = content.split("\n")
        
        for line in lines:
            if (line.strip().startswith("-") and 
                ("suggest" in line.lower() or "recommend" in line.lower())):
                suggestions.append(line.strip()[1:].strip())
        
        return suggestions or ["Consider adding unit tests", "Review for edge cases"]
    
    def _calculate_cost(self, input_length: int, output_length: int) -> float:
        """Calculate cost for Claude"""
        input_tokens = input_length // 4
        output_tokens = output_length // 4
        return (input_tokens * 0.00008) + (output_tokens * 0.00024)


class GPT4OAdapter(BaseAPIAdapter):
    """Adapter for GPT-4o"""
    
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> APICallResult:
        """Transform code using GPT-4o with balanced approach"""
        if not self.can_make_request():
            return APICallResult(
                success=False,
                error_message="Rate limited or circuit breaker open"
            )
        
        start_time = time.time()
        self.total_requests += 1
        self.rate_limit_info.current_count += 1
        
        try:
            prompt = self._build_balanced_prompt(code, source_lang, target_lang, requirements)
            
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.credentials.api_key}",
                    "Content-Type": "application/json",
                    **self.credentials.additional_headers
                }
                
                payload = {
                    "model": "gpt-4o-2024-05-13",
                    "messages": [{
                        "role": "system",
                        "content": "You are an expert code transformation assistant. Provide balanced, high-quality transformations."
                    }, {
                        "role": "user",
                        "content": prompt
                    }],
                    "max_tokens": 4096,
                    "temperature": 0.25
                }
                
                async with session.post(
                    self.credentials.endpoint_url,
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=45)
                ) as response:
                    response_time = time.time() - start_time
                    self.total_response_time += response_time
                    
                    if response.status == 200:
                        data = await response.json()
                        result = self._parse_gpt_response(data)
                        
                        self.successful_requests += 1
                        self.update_circuit_breaker(True)
                        
                        cost = self._calculate_cost(
                            data.get("usage", {}).get("prompt_tokens", 0),
                            data.get("usage", {}).get("completion_tokens", 0)
                        )
                        self.total_cost += cost
                        
                        return APICallResult(
                            success=True,
                            response_data=result,
                            response_time=response_time,
                            cost=cost,
                            tokens_used=data.get("usage", {}).get("total_tokens", 0)
                        )
                    else:
                        self.update_circuit_breaker(False)
                        error_text = await response.text()
                        return APICallResult(
                            success=False,
                            error_message=f"HTTP {response.status}: {error_text}",
                            response_time=response_time
                        )
                        
        except Exception as e:
            response_time = time.time() - start_time
            self.total_response_time += response_time
            self.update_circuit_breaker(False)
            
            return APICallResult(
                success=False,
                error_message=str(e),
                response_time=response_time
            )
    
    async def health_check(self) -> APIStatus:
        """Check GPT-4o health"""
        return await super().health_check()
    
    def _build_balanced_prompt(self, code: str, source_lang: str,
                             target_lang: str, requirements: List[str]) -> str:
        """Build balanced prompt for GPT-4o"""
        req_text = "\n".join(requirements) if requirements else ""
        
        return f"""Transform the following {source_lang} code to {target_lang} using a balanced approach that considers:

1. Code functionality and correctness
2. Performance and efficiency
3. Readability and maintainability
4. Best practices for {target_lang}
5. Error handling and robustness

Requirements:
{req_text}

Source Code:
```{source_lang}
{code}
```

Provide the transformed code along with a brief explanation of key changes and any important considerations."""
    
    def _parse_gpt_response(self, data: Dict) -> Dict[str, Any]:
        """Parse GPT-4o response"""
        try:
            content = data["choices"][0]["message"]["content"]
            
            return {
                "code": self._extract_code_from_text(content),
                "explanation": "Balanced transformation considering functionality, performance, and maintainability",
                "confidence": 0.90,
                "suggestions": ["Test thoroughly", "Consider edge cases"],
                "metadata": {
                    "model": "gpt-4o",
                    "approach": "balanced"
                }
            }
            
        except (KeyError, IndexError):
            return {
                "code": "",
                "explanation": "Failed to parse GPT-4o response",
                "confidence": 0.0,
                "suggestions": [],
                "metadata": {"error": "parsing_failed"}
            }
    
    def _extract_code_from_text(self, content: str) -> str:
        """Extract code from GPT response"""
        if "```" in content:
            start = content.find("```") + 3
            start = content.find("\n", start) + 1
            end = content.find("```", start)
            return content[start:end].strip()
        return content.strip()
    
    def _calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate cost for GPT-4o"""
        return (prompt_tokens * 0.00005) + (completion_tokens * 0.00015)


class APIIntegrationManager:
    """Main manager for all API integrations"""
    
    def __init__(self, federation_router: FederationRouter = None):
        self.federation_router = federation_router
        self.adapters: Dict[str, BaseAPIAdapter] = {}
        self.logger = logging.getLogger(__name__)
        
        # Health monitoring
        self.health_check_interval = 300  # 5 minutes
        self.last_health_check = {}
        
        # Load balancing
        self.request_counts = {}
        
    def register_adapter(self, service_name: str, adapter: BaseAPIAdapter):
        """Register an API adapter"""
        self.adapters[service_name] = adapter
        self.request_counts[service_name] = 0
        self.logger.info(f"Registered adapter for {service_name}")
    
    def setup_default_adapters(self, credentials_config: Dict[str, APICredentials]):
        """Setup default adapters with provided credentials"""
        for service_name, credentials in credentials_config.items():
            if service_name == "gemini_flash":
                adapter = GeminiFlashAdapter(credentials)
            elif service_name == "gemini_pro":
                adapter = GeminiProAdapter(credentials)
            elif service_name == "claude":
                adapter = ClaudeAdapter(credentials)
            elif service_name == "gpt4o":
                adapter = GPT4OAdapter(credentials)
            else:
                self.logger.warning(f"Unknown service: {service_name}")
                continue
            
            self.register_adapter(service_name, adapter)
    
    async def call_model(self, service_name: str, request_data: Any,
                        call_id: str = None) -> Dict[str, Any]:
        """Call a specific model through its adapter"""
        if service_name not in self.adapters:
            raise ValueError(f"Unknown service: {service_name}")
        
        adapter = self.adapters[service_name]
        
        # Health check if needed
        await self._ensure_health_checked(service_name)
        
        if adapter.status == APIStatus.DOWN:
            raise Exception(f"Service {service_name} is down")
        
        # Extract parameters from request_data
        if hasattr(request_data, 'code'):
            # TransformationRequest object
            result = await adapter.transform_code(
                code=request_data.code,
                source_lang=request_data.source_language,
                target_lang=request_data.target_language,
                requirements=request_data.requirements
            )
        else:
            # Dict format
            result = await adapter.transform_code(
                code=request_data.get("code", ""),
                source_lang=request_data.get("source_language", ""),
                target_lang=request_data.get("target_language", ""),
                requirements=request_data.get("requirements", [])
            )
        
        if result.success:
            self.request_counts[service_name] += 1
            return result.response_data
        else:
            raise Exception(f"API call failed: {result.error_message}")
    
    async def get_service_status(self, service_name: str) -> APIStatus:
        """Get current status of a service"""
        if service_name not in self.adapters:
            return APIStatus.UNKNOWN
        
        return await self.adapters[service_name].health_check()
    
    async def get_all_service_status(self) -> Dict[str, APIStatus]:
        """Get status of all registered services"""
        status_tasks = []
        for service_name in self.adapters:
            task = asyncio.create_task(self.get_service_status(service_name))
            status_tasks.append((service_name, task))
        
        statuses = {}
        for service_name, task in status_tasks:
            try:
                status = await task
                statuses[service_name] = status
            except Exception:
                statuses[service_name] = APIStatus.DOWN
        
        return statuses
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics for all adapters"""
        metrics = {}
        for service_name, adapter in self.adapters.items():
            metrics[service_name] = adapter.get_performance_metrics()
        
        return metrics
    
    async def _ensure_health_checked(self, service_name: str):
        """Ensure service has been health checked recently"""
        now = datetime.now()
        last_check = self.last_health_check.get(service_name)
        
        if (not last_check or 
            (now - last_check).total_seconds() > self.health_check_interval):
            await self.get_service_status(service_name)
            self.last_health_check[service_name] = now
    
    def get_recommended_service(self, task_type: str, quality_preference: int) -> str:
        """Get recommended service based on task type and quality preference"""
        # Auto-assignment logic
        if task_type in ["syntax_check", "quick_transform"]:
            return "gemini_flash"
        elif task_type in ["architecture_review", "complex_logic"]:
            return "gemini_pro"
        elif task_type in ["documentation", "explanation"]:
            return "claude"
        elif task_type in ["general_review", "refactoring"]:
            return "gpt4o"
        else:
            # Fallback based on quality preference
            if quality_preference <= 3:
                return "gemini_flash"
            elif quality_preference <= 6:
                return "gpt4o"
            else:
                return "gemini_pro"