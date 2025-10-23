"""
CodeVerter Consensus Engine

This module implements sophisticated consensus scoring and confidence analysis
for multi-API collaborative code transformations.
"""

import json
import re
import ast
import difflib
import statistics
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple, Union
from datetime import datetime
from enum import Enum
import logging

# External dependencies for advanced analysis
try:
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    HAS_ML_LIBS = True
except ImportError:
    HAS_ML_LIBS = False
    logging.warning("ML libraries not available, using basic similarity metrics")


class AgreementType(Enum):
    """Types of agreement analysis"""
    SYNTAX = "syntax"
    SEMANTICS = "semantics"
    STYLE = "style"
    PERFORMANCE = "performance"
    SECURITY = "security"
    MAINTAINABILITY = "maintainability"


class ConfidenceLevel(Enum):
    """Confidence level categories"""
    VERY_LOW = "very_low"    # 0-20%
    LOW = "low"              # 20-40%
    MEDIUM_LOW = "medium_low" # 40-60%
    MEDIUM = "medium"        # 60-75%
    MEDIUM_HIGH = "medium_high" # 75-85%
    HIGH = "high"            # 85-95%
    VERY_HIGH = "very_high"  # 95-100%


@dataclass
class SimilarityMetrics:
    """Detailed similarity metrics between two results"""
    lexical_similarity: float = 0.0          # String/token similarity
    structural_similarity: float = 0.0       # AST/code structure similarity
    semantic_similarity: float = 0.0         # Meaning/functionality similarity
    style_similarity: float = 0.0           # Coding style consistency
    performance_similarity: float = 0.0      # Performance characteristics
    overall_similarity: float = 0.0         # Weighted combined score
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary for serialization"""
        return {
            "lexical": self.lexical_similarity,
            "structural": self.structural_similarity,
            "semantic": self.semantic_similarity,
            "style": self.style_similarity,
            "performance": self.performance_similarity,
            "overall": self.overall_similarity
        }


@dataclass
class ConflictAnalysis:
    """Analysis of conflicts between different model results"""
    conflict_areas: List[str] = field(default_factory=list)
    severity_scores: Dict[str, float] = field(default_factory=dict)
    resolution_suggestions: List[str] = field(default_factory=list)
    confidence_impact: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "conflict_areas": self.conflict_areas,
            "severity_scores": self.severity_scores,
            "resolution_suggestions": self.resolution_suggestions,
            "confidence_impact": self.confidence_impact
        }


@dataclass
class ConsensusResult:
    """Complete consensus analysis result"""
    consensus_score: float = 0.0
    confidence_score: float = 0.0
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEDIUM
    agreement_breakdown: Dict[str, float] = field(default_factory=dict)
    similarity_matrix: Dict[str, Dict[str, SimilarityMetrics]] = field(default_factory=dict)
    conflict_analysis: ConflictAnalysis = field(default_factory=ConflictAnalysis)
    quality_indicators: Dict[str, float] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses"""
        return {
            "consensus_score": self.consensus_score,
            "confidence_score": self.confidence_score,
            "confidence_level": self.confidence_level.value,
            "agreement_breakdown": self.agreement_breakdown,
            "similarity_matrix": {
                model1: {
                    model2: metrics.to_dict() 
                    for model2, metrics in similarities.items()
                }
                for model1, similarities in self.similarity_matrix.items()
            },
            "conflict_analysis": self.conflict_analysis.to_dict(),
            "quality_indicators": self.quality_indicators,
            "recommendations": self.recommendations,
            "metadata": self.metadata
        }


class AdvancedCodeAnalyzer:
    """Advanced code analysis utilities"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Language-specific patterns
        self.language_patterns = {
            'python': {
                'function_def': r'def\s+(\w+)\s*\(',
                'class_def': r'class\s+(\w+)\s*[\(:]',
                'imports': r'(?:from\s+\w+\s+)?import\s+[\w\.,\s]+',
                'comments': r'#.*$',
                'docstrings': r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''
            },
            'javascript': {
                'function_def': r'function\s+(\w+)\s*\(|(\w+)\s*=\s*function|\(\s*\)\s*=>|(\w+)\s*=>\s*\{',
                'class_def': r'class\s+(\w+)\s*\{',
                'imports': r'import\s+.*?from\s+.*?;|require\s*\(.*?\)',
                'comments': r'//.*$|/\*[\s\S]*?\*/',
                'arrow_functions': r'=>'
            },
            'typescript': {
                'function_def': r'function\s+(\w+)\s*\(|(\w+)\s*=\s*function|\(\s*\)\s*=>|(\w+)\s*=>\s*\{',
                'class_def': r'class\s+(\w+)\s*\{',
                'interface_def': r'interface\s+(\w+)\s*\{',
                'type_def': r'type\s+(\w+)\s*=',
                'imports': r'import\s+.*?from\s+.*?;',
                'comments': r'//.*$|/\*[\s\S]*?\*/',
                'type_annotations': r':\s*\w+[\[\]<>]*'
            }
        }
    
    def extract_code_features(self, code: str, language: str) -> Dict[str, Any]:
        """Extract comprehensive features from code"""
        features = {
            'line_count': len(code.split('\n')),
            'char_count': len(code),
            'word_count': len(code.split()),
            'functions': [],
            'classes': [],
            'interfaces': [],
            'imports': [],
            'comments': [],
            'complexity_indicators': {}
        }
        
        if language not in self.language_patterns:
            return features
        
        patterns = self.language_patterns[language]
        
        # Extract functions
        if 'function_def' in patterns:
            features['functions'] = re.findall(patterns['function_def'], code, re.MULTILINE)
            
        # Extract classes
        if 'class_def' in patterns:
            features['classes'] = re.findall(patterns['class_def'], code, re.MULTILINE)
            
        # Extract interfaces (TypeScript)
        if 'interface_def' in patterns:
            features['interfaces'] = re.findall(patterns['interface_def'], code, re.MULTILINE)
            
        # Extract imports
        if 'imports' in patterns:
            features['imports'] = re.findall(patterns['imports'], code, re.MULTILINE)
            
        # Extract comments
        if 'comments' in patterns:
            features['comments'] = re.findall(patterns['comments'], code, re.MULTILINE)
        
        # Calculate complexity indicators
        features['complexity_indicators'] = self._calculate_complexity_indicators(code, language)
        
        return features
    
    def _calculate_complexity_indicators(self, code: str, language: str) -> Dict[str, float]:
        """Calculate various complexity indicators"""
        indicators = {}
        
        lines = code.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Cyclomatic complexity (simplified)
        decision_keywords = ['if', 'elif', 'else', 'while', 'for', 'try', 'except', 'case', 'switch']
        decision_count = sum(
            len(re.findall(r'\b' + keyword + r'\b', code, re.IGNORECASE))
            for keyword in decision_keywords
        )
        indicators['cyclomatic_complexity'] = decision_count + 1
        
        # Nesting depth (simplified)
        max_depth = 0
        current_depth = 0
        for line in lines:
            stripped = line.strip()
            if stripped:
                # Count indentation (assuming 4 spaces or 1 tab = 1 level)
                leading_spaces = len(line) - len(line.lstrip())
                depth = leading_spaces // 4  # Approximate
                max_depth = max(max_depth, depth)
        
        indicators['max_nesting_depth'] = max_depth
        
        # Halstead metrics (simplified)
        # This is a very basic approximation
        unique_operators = len(set(re.findall(r'[+\-*/=<>!&|^%]+', code)))
        unique_operands = len(set(re.findall(r'\b[a-zA-Z_]\w*\b', code)))
        
        indicators['halstead_vocabulary'] = unique_operators + unique_operands
        indicators['halstead_length'] = len(re.findall(r'[+\-*/=<>!&|^%]+|\b[a-zA-Z_]\w*\b', code))
        
        return indicators
    
    def calculate_structural_similarity(self, code1: str, code2: str, language: str) -> float:
        """Calculate structural similarity using AST or pattern-based analysis"""
        try:
            if language == 'python':
                return self._python_ast_similarity(code1, code2)
            else:
                return self._pattern_based_similarity(code1, code2, language)
        except Exception as e:
            self.logger.warning(f"Structural similarity calculation failed: {e}")
            return self._fallback_similarity(code1, code2)
    
    def _python_ast_similarity(self, code1: str, code2: str) -> float:
        """Calculate similarity using Python AST"""
        try:
            ast1 = ast.parse(code1)
            ast2 = ast.parse(code2)
            
            # Extract structural elements
            elements1 = self._extract_ast_elements(ast1)
            elements2 = self._extract_ast_elements(ast2)
            
            # Calculate similarity
            common_elements = len(elements1.intersection(elements2))
            total_elements = len(elements1.union(elements2))
            
            return common_elements / total_elements if total_elements > 0 else 0.0
            
        except SyntaxError:
            return self._fallback_similarity(code1, code2)
    
    def _extract_ast_elements(self, tree: ast.AST) -> set:
        """Extract structural elements from AST"""
        elements = set()
        
        for node in ast.walk(tree):
            node_type = type(node).__name__
            elements.add(node_type)
            
            # Add specific patterns
            if isinstance(node, ast.FunctionDef):
                elements.add(f"function:{node.name}")
            elif isinstance(node, ast.ClassDef):
                elements.add(f"class:{node.name}")
            elif isinstance(node, ast.Call) and hasattr(node.func, 'id'):
                elements.add(f"call:{node.func.id}")
        
        return elements
    
    def _pattern_based_similarity(self, code1: str, code2: str, language: str) -> float:
        """Calculate similarity using language-specific patterns"""
        features1 = self.extract_code_features(code1, language)
        features2 = self.extract_code_features(code2, language)
        
        similarities = []
        
        # Compare function counts
        func_similarity = self._compare_lists(features1['functions'], features2['functions'])
        similarities.append(func_similarity)
        
        # Compare class counts
        class_similarity = self._compare_lists(features1['classes'], features2['classes'])
        similarities.append(class_similarity)
        
        # Compare complexity indicators
        for key in features1['complexity_indicators']:
            if key in features2['complexity_indicators']:
                val1 = features1['complexity_indicators'][key]
                val2 = features2['complexity_indicators'][key]
                if val1 == 0 and val2 == 0:
                    similarities.append(1.0)
                elif val1 == 0 or val2 == 0:
                    similarities.append(0.0)
                else:
                    similarity = 1.0 - abs(val1 - val2) / max(val1, val2)
                    similarities.append(max(0.0, similarity))
        
        return statistics.mean(similarities) if similarities else 0.0
    
    def _compare_lists(self, list1: List, list2: List) -> float:
        """Compare two lists for similarity"""
        if not list1 and not list2:
            return 1.0
        if not list1 or not list2:
            return 0.0
        
        set1 = set(str(item) for item in list1)
        set2 = set(str(item) for item in list2)
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def _fallback_similarity(self, code1: str, code2: str) -> float:
        """Fallback similarity calculation using string comparison"""
        return difflib.SequenceMatcher(None, code1, code2).ratio()


class ConsensusEngine:
    """Main consensus analysis engine"""
    
    def __init__(self, model_weights: Optional[Dict[str, float]] = None):
        self.logger = logging.getLogger(__name__)
        self.code_analyzer = AdvancedCodeAnalyzer()
        
        # Model reliability weights (can be learned over time)
        self.model_weights = model_weights or {
            'gemini_flash': 0.85,
            'gemini_pro': 0.95,
            'claude_sonnet': 0.92,
            'gpt_4o': 0.90,
            'federation_satellite': 0.88
        }
        
        # Agreement type weights
        self.agreement_weights = {
            AgreementType.SYNTAX: 0.25,
            AgreementType.SEMANTICS: 0.30,
            AgreementType.STYLE: 0.15,
            AgreementType.PERFORMANCE: 0.15,
            AgreementType.SECURITY: 0.10,
            AgreementType.MAINTAINABILITY: 0.05
        }
        
        # Historical performance tracking
        self.performance_history = {}
        
    def analyze_consensus(self, results: List[Any], request_context: Dict[str, Any]) -> ConsensusResult:
        """
        Analyze consensus among multiple transformation results
        
        Args:
            results: List of TransformationResult objects
            request_context: Context about the original request
            
        Returns:
            ConsensusResult with detailed analysis
        """
        if len(results) < 2:
            return self._single_result_analysis(results[0] if results else None)
        
        try:
            # Calculate pairwise similarities
            similarity_matrix = self._calculate_similarity_matrix(results, request_context)
            
            # Analyze agreement across different dimensions
            agreement_breakdown = self._analyze_agreement_breakdown(results, request_context)
            
            # Detect and analyze conflicts
            conflict_analysis = self._analyze_conflicts(results, similarity_matrix)
            
            # Calculate overall consensus score
            consensus_score = self._calculate_consensus_score(
                similarity_matrix, agreement_breakdown, conflict_analysis
            )
            
            # Calculate confidence score
            confidence_score = self._calculate_confidence_score(
                results, consensus_score, conflict_analysis, request_context
            )
            
            # Determine confidence level
            confidence_level = self._determine_confidence_level(confidence_score)
            
            # Calculate quality indicators
            quality_indicators = self._calculate_quality_indicators(results, request_context)
            
            # Generate recommendations
            recommendations = self._generate_recommendations(
                results, consensus_score, conflict_analysis, quality_indicators
            )
            
            return ConsensusResult(
                consensus_score=consensus_score,
                confidence_score=confidence_score,
                confidence_level=confidence_level,
                agreement_breakdown=agreement_breakdown,
                similarity_matrix=similarity_matrix,
                conflict_analysis=conflict_analysis,
                quality_indicators=quality_indicators,
                recommendations=recommendations,
                metadata={
                    'analysis_timestamp': datetime.now().isoformat(),
                    'num_results': len(results),
                    'analysis_version': '1.0',
                    'has_ml_features': HAS_ML_LIBS
                }
            )
            
        except Exception as e:
            self.logger.error(f"Consensus analysis failed: {e}")
            return self._fallback_consensus_result(results)
    
    def _calculate_similarity_matrix(self, results: List[Any], context: Dict[str, Any]) -> Dict[str, Dict[str, SimilarityMetrics]]:
        """Calculate pairwise similarity matrix between all results"""
        matrix = {}
        source_language = context.get('source_language', 'unknown')
        target_language = context.get('target_language', 'unknown')
        
        for i, result1 in enumerate(results):
            model1 = result1.model
            matrix[model1] = {}
            
            for j, result2 in enumerate(results):
                model2 = result2.model
                
                if i == j:
                    # Self-similarity is perfect
                    matrix[model1][model2] = SimilarityMetrics(
                        lexical_similarity=1.0,
                        structural_similarity=1.0,
                        semantic_similarity=1.0,
                        style_similarity=1.0,
                        performance_similarity=1.0,
                        overall_similarity=1.0
                    )
                else:
                    # Calculate detailed similarity metrics
                    metrics = self._calculate_detailed_similarity(
                        result1, result2, target_language
                    )
                    matrix[model1][model2] = metrics
        
        return matrix
    
    def _calculate_detailed_similarity(self, result1: Any, result2: Any, language: str) -> SimilarityMetrics:
        """Calculate detailed similarity metrics between two results"""
        code1 = result1.transformed_code
        code2 = result2.transformed_code
        
        # Lexical similarity (string-based)
        lexical_sim = difflib.SequenceMatcher(None, code1, code2).ratio()
        
        # Structural similarity (AST/pattern-based)
        structural_sim = self.code_analyzer.calculate_structural_similarity(code1, code2, language)
        
        # Semantic similarity
        semantic_sim = self._calculate_semantic_similarity(result1, result2)
        
        # Style similarity
        style_sim = self._calculate_style_similarity(code1, code2, language)
        
        # Performance similarity (based on explanations and metadata)
        performance_sim = self._calculate_performance_similarity(result1, result2)
        
        # Calculate weighted overall similarity
        overall_sim = (
            lexical_sim * 0.2 +
            structural_sim * 0.3 +
            semantic_sim * 0.25 +
            style_sim * 0.15 +
            performance_sim * 0.1
        )
        
        return SimilarityMetrics(
            lexical_similarity=lexical_sim,
            structural_similarity=structural_sim,
            semantic_similarity=semantic_sim,
            style_similarity=style_sim,
            performance_similarity=performance_sim,
            overall_similarity=overall_sim
        )
    
    def _calculate_semantic_similarity(self, result1: Any, result2: Any) -> float:
        """Calculate semantic similarity using various approaches"""
        if not HAS_ML_LIBS:
            # Fallback to basic similarity
            return difflib.SequenceMatcher(
                None, 
                result1.explanation + " " + " ".join(result1.suggestions),
                result2.explanation + " " + " ".join(result2.suggestions)
            ).ratio()
        
        try:
            # Use TF-IDF and cosine similarity for semantic analysis
            documents = [
                result1.explanation + " " + " ".join(result1.suggestions),
                result2.explanation + " " + " ".join(result2.suggestions)
            ]
            
            if not documents[0].strip() or not documents[1].strip():
                return 0.5  # Neutral similarity if no explanations
            
            vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
            tfidf_matrix = vectorizer.fit_transform(documents)
            
            similarity_matrix = cosine_similarity(tfidf_matrix)
            return float(similarity_matrix[0][1])
            
        except Exception as e:
            self.logger.warning(f"Semantic similarity calculation failed: {e}")
            return 0.5
    
    def _calculate_style_similarity(self, code1: str, code2: str, language: str) -> float:
        """Calculate code style similarity"""
        # Extract style features
        features1 = self._extract_style_features(code1, language)
        features2 = self._extract_style_features(code2, language)
        
        similarities = []
        
        # Compare indentation style
        if features1['indentation'] and features2['indentation']:
            indent_sim = 1.0 if features1['indentation'] == features2['indentation'] else 0.3
            similarities.append(indent_sim)
        
        # Compare naming conventions
        naming_sim = self._compare_naming_conventions(features1['identifiers'], features2['identifiers'])
        similarities.append(naming_sim)
        
        # Compare line length consistency
        length_sim = 1.0 - abs(features1['avg_line_length'] - features2['avg_line_length']) / 100
        similarities.append(max(0.0, length_sim))
        
        # Compare comment density
        comment_sim = 1.0 - abs(features1['comment_density'] - features2['comment_density'])
        similarities.append(max(0.0, comment_sim))
        
        return statistics.mean(similarities) if similarities else 0.5
    
    def _extract_style_features(self, code: str, language: str) -> Dict[str, Any]:
        """Extract style-related features from code"""
        lines = code.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Indentation detection
        indentation = 'unknown'
        for line in lines:
            if line.startswith('    '):
                indentation = 'spaces'
                break
            elif line.startswith('\t'):
                indentation = 'tabs'
                break
        
        # Extract identifiers for naming convention analysis
        identifiers = re.findall(r'\b[a-zA-Z_]\w*\b', code)
        
        # Calculate average line length
        avg_line_length = statistics.mean([len(line) for line in non_empty_lines]) if non_empty_lines else 0
        
        # Comment density
        comment_lines = len([line for line in lines if line.strip().startswith('#') or line.strip().startswith('//')])
        comment_density = comment_lines / len(non_empty_lines) if non_empty_lines else 0
        
        return {
            'indentation': indentation,
            'identifiers': identifiers,
            'avg_line_length': avg_line_length,
            'comment_density': comment_density
        }
    
    def _compare_naming_conventions(self, identifiers1: List[str], identifiers2: List[str]) -> float:
        """Compare naming convention consistency"""
        if not identifiers1 or not identifiers2:
            return 0.5
        
        # Analyze naming patterns
        patterns1 = self._analyze_naming_patterns(identifiers1)
        patterns2 = self._analyze_naming_patterns(identifiers2)
        
        similarities = []
        
        for pattern in ['snake_case', 'camelCase', 'PascalCase']:
            ratio1 = patterns1.get(pattern, 0)
            ratio2 = patterns2.get(pattern, 0)
            similarity = 1.0 - abs(ratio1 - ratio2)
            similarities.append(similarity)
        
        return statistics.mean(similarities)
    
    def _analyze_naming_patterns(self, identifiers: List[str]) -> Dict[str, float]:
        """Analyze naming pattern distribution"""
        patterns = {'snake_case': 0, 'camelCase': 0, 'PascalCase': 0}
        
        for identifier in identifiers:
            if '_' in identifier and identifier.islower():
                patterns['snake_case'] += 1
            elif identifier[0].islower() and any(c.isupper() for c in identifier[1:]):
                patterns['camelCase'] += 1
            elif identifier[0].isupper():
                patterns['PascalCase'] += 1
        
        total = sum(patterns.values())
        if total == 0:
            return {k: 0.0 for k in patterns}
        
        return {k: v / total for k, v in patterns.items()}
    
    def _calculate_performance_similarity(self, result1: Any, result2: Any) -> float:
        """Calculate performance-related similarity"""
        # This is a simplified version - in production, would analyze
        # performance implications from explanations and metadata
        
        perf_keywords = ['performance', 'speed', 'optimization', 'efficiency', 'fast', 'slow']
        
        text1 = (result1.explanation + " " + " ".join(result1.suggestions)).lower()
        text2 = (result2.explanation + " " + " ".join(result2.suggestions)).lower()
        
        perf_mentions1 = sum(text1.count(keyword) for keyword in perf_keywords)
        perf_mentions2 = sum(text2.count(keyword) for keyword in perf_keywords)
        
        if perf_mentions1 == 0 and perf_mentions2 == 0:
            return 1.0  # Both don't mention performance
        
        if perf_mentions1 == 0 or perf_mentions2 == 0:
            return 0.3  # Only one mentions performance
        
        # Both mention performance - check if similar frequency
        ratio = min(perf_mentions1, perf_mentions2) / max(perf_mentions1, perf_mentions2)
        return ratio
    
    def _analyze_agreement_breakdown(self, results: List[Any], context: Dict[str, Any]) -> Dict[str, float]:
        """Analyze agreement across different dimensions"""
        breakdown = {}
        
        for agreement_type in AgreementType:
            scores = []
            
            for i in range(len(results)):
                for j in range(i + 1, len(results)):
                    score = self._calculate_agreement_score(
                        results[i], results[j], agreement_type, context
                    )
                    scores.append(score)
            
            breakdown[agreement_type.value] = statistics.mean(scores) if scores else 0.0
        
        return breakdown
    
    def _calculate_agreement_score(self, result1: Any, result2: Any, 
                                 agreement_type: AgreementType, context: Dict[str, Any]) -> float:
        """Calculate agreement score for a specific dimension"""
        if agreement_type == AgreementType.SYNTAX:
            return self._analyze_syntax_agreement(result1, result2, context)
        elif agreement_type == AgreementType.SEMANTICS:
            return self._analyze_semantic_agreement(result1, result2)
        elif agreement_type == AgreementType.STYLE:
            return self._analyze_style_agreement(result1, result2, context)
        elif agreement_type == AgreementType.PERFORMANCE:
            return self._analyze_performance_agreement(result1, result2)
        elif agreement_type == AgreementType.SECURITY:
            return self._analyze_security_agreement(result1, result2)
        elif agreement_type == AgreementType.MAINTAINABILITY:
            return self._analyze_maintainability_agreement(result1, result2)
        else:
            return 0.5  # Default neutral score
    
    def _analyze_syntax_agreement(self, result1: Any, result2: Any, context: Dict[str, Any]) -> float:
        """Analyze syntax-level agreement"""
        language = context.get('target_language', 'unknown')
        
        try:
            if language == 'python':
                # Try to parse both as valid Python
                ast.parse(result1.transformed_code)
                ast.parse(result2.transformed_code)
                return 1.0  # Both are syntactically valid
            else:
                # For other languages, use basic pattern matching
                return self._basic_syntax_check(result1.transformed_code, result2.transformed_code, language)
        except SyntaxError:
            return 0.3  # Syntax error in one or both
    
    def _basic_syntax_check(self, code1: str, code2: str, language: str) -> float:
        """Basic syntax agreement check for non-Python languages"""
        # Count brackets, braces, parentheses balance
        for code in [code1, code2]:
            if (code.count('(') != code.count(')') or
                code.count('[') != code.count(']') or
                code.count('{') != code.count('}')):
                return 0.3  # Unbalanced brackets suggest syntax error
        
        return 0.8  # Basic syntax seems okay
    
    def _analyze_semantic_agreement(self, result1: Any, result2: Any) -> float:
        """Analyze semantic agreement"""
        return self._calculate_semantic_similarity(result1, result2)
    
    def _analyze_style_agreement(self, result1: Any, result2: Any, context: Dict[str, Any]) -> float:
        """Analyze style agreement"""
        language = context.get('target_language', 'unknown')
        return self._calculate_style_similarity(result1.transformed_code, result2.transformed_code, language)
    
    def _analyze_performance_agreement(self, result1: Any, result2: Any) -> float:
        """Analyze performance-related agreement"""
        return self._calculate_performance_similarity(result1, result2)
    
    def _analyze_security_agreement(self, result1: Any, result2: Any) -> float:
        """Analyze security-related agreement"""
        security_keywords = ['security', 'secure', 'vulnerability', 'safe', 'unsafe', 'injection', 'validation']
        
        text1 = (result1.explanation + " " + " ".join(result1.suggestions)).lower()
        text2 = (result2.explanation + " " + " ".join(result2.suggestions)).lower()
        
        security_mentions1 = sum(text1.count(keyword) for keyword in security_keywords)
        security_mentions2 = sum(text2.count(keyword) for keyword in security_keywords)
        
        if security_mentions1 == 0 and security_mentions2 == 0:
            return 1.0  # Neither mentions security concerns
        
        if abs(security_mentions1 - security_mentions2) <= 1:
            return 0.8  # Similar security awareness
        
        return 0.4  # Different levels of security awareness
    
    def _analyze_maintainability_agreement(self, result1: Any, result2: Any) -> float:
        """Analyze maintainability agreement"""
        maint_keywords = ['maintainable', 'readable', 'clean', 'documentation', 'comments', 'modular']
        
        text1 = (result1.explanation + " " + " ".join(result1.suggestions)).lower()
        text2 = (result2.explanation + " " + " ".join(result2.suggestions)).lower()
        
        maint_mentions1 = sum(text1.count(keyword) for keyword in maint_keywords)
        maint_mentions2 = sum(text2.count(keyword) for keyword in maint_keywords)
        
        if maint_mentions1 == 0 and maint_mentions2 == 0:
            return 0.7  # Neither explicitly mentions maintainability
        
        if abs(maint_mentions1 - maint_mentions2) <= 1:
            return 0.9  # Similar maintainability focus
        
        return 0.5  # Different maintainability emphasis
    
    def _analyze_conflicts(self, results: List[Any], similarity_matrix: Dict[str, Dict[str, SimilarityMetrics]]) -> ConflictAnalysis:
        """Analyze conflicts between different results"""
        conflict_areas = []
        severity_scores = {}
        resolution_suggestions = []
        
        # Find low similarity pairs
        low_similarity_threshold = 0.6
        conflicts_found = False
        
        for model1, similarities in similarity_matrix.items():
            for model2, metrics in similarities.items():
                if model1 != model2 and metrics.overall_similarity < low_similarity_threshold:
                    conflicts_found = True
                    
                    # Identify specific conflict areas
                    if metrics.structural_similarity < 0.5:
                        area = f"Structural differences between {model1} and {model2}"
                        if area not in conflict_areas:
                            conflict_areas.append(area)
                            severity_scores[area] = 1.0 - metrics.structural_similarity
                    
                    if metrics.semantic_similarity < 0.5:
                        area = f"Semantic differences between {model1} and {model2}"
                        if area not in conflict_areas:
                            conflict_areas.append(area)
                            severity_scores[area] = 1.0 - metrics.semantic_similarity
                    
                    if metrics.style_similarity < 0.4:
                        area = f"Style inconsistencies between {model1} and {model2}"
                        if area not in conflict_areas:
                            conflict_areas.append(area)
                            severity_scores[area] = 1.0 - metrics.style_similarity
        
        # Generate resolution suggestions
        if conflicts_found:
            resolution_suggestions.extend([
                "Consider using higher quality settings for more consistent results",
                "Review conflicting transformations manually",
                "Use cross-validation mode for better conflict resolution",
                "Check if specific requirements are causing divergent interpretations"
            ])
        
        # Calculate confidence impact
        avg_similarity = statistics.mean([
            metrics.overall_similarity
            for similarities in similarity_matrix.values()
            for model, metrics in similarities.items()
            if model != list(similarities.keys())[0]  # Exclude self-similarity
        ]) if similarity_matrix else 1.0
        
        confidence_impact = max(0.0, 1.0 - avg_similarity)
        
        return ConflictAnalysis(
            conflict_areas=conflict_areas,
            severity_scores=severity_scores,
            resolution_suggestions=resolution_suggestions,
            confidence_impact=confidence_impact
        )
    
    def _calculate_consensus_score(self, similarity_matrix: Dict[str, Dict[str, SimilarityMetrics]], 
                                 agreement_breakdown: Dict[str, float], 
                                 conflict_analysis: ConflictAnalysis) -> float:
        """Calculate overall consensus score"""
        # Average pairwise similarity
        similarities = []
        for model1, model_similarities in similarity_matrix.items():
            for model2, metrics in model_similarities.items():
                if model1 != model2:
                    similarities.append(metrics.overall_similarity)
        
        avg_similarity = statistics.mean(similarities) if similarities else 0.0
        
        # Weighted agreement score
        weighted_agreement = sum(
            score * self.agreement_weights.get(AgreementType(dimension), 0.1)
            for dimension, score in agreement_breakdown.items()
        )
        
        # Conflict penalty
        conflict_penalty = conflict_analysis.confidence_impact * 0.3
        
        # Final consensus score
        consensus_score = (avg_similarity * 0.5 + weighted_agreement * 0.5) * (1.0 - conflict_penalty)
        
        return max(0.0, min(1.0, consensus_score))
    
    def _calculate_confidence_score(self, results: List[Any], consensus_score: float,
                                  conflict_analysis: ConflictAnalysis, context: Dict[str, Any]) -> float:
        """Calculate overall confidence score"""
        factors = []
        
        # Model confidence average (weighted)
        weighted_confidences = []
        for result in results:
            weight = self.model_weights.get(result.model, 0.8)
            weighted_confidences.append(result.confidence * weight)
        
        avg_confidence = statistics.mean(weighted_confidences) if weighted_confidences else 0.5
        factors.append(('model_confidence', avg_confidence, 0.3))
        
        # Consensus score contribution
        factors.append(('consensus', consensus_score, 0.4))
        
        # Result consistency (low variance in confidence scores)
        if len(results) > 1:
            confidence_variance = statistics.variance([r.confidence for r in results])
            consistency_score = max(0.0, 1.0 - confidence_variance)
            factors.append(('consistency', consistency_score, 0.2))
        
        # Historical performance (if available)
        model_names = [r.model for r in results]
        historical_score = self._get_historical_performance(model_names, context)
        factors.append(('historical', historical_score, 0.1))
        
        # Calculate weighted confidence
        total_weight = sum(weight for _, _, weight in factors)
        weighted_score = sum(score * weight for _, score, weight in factors) / total_weight
        
        # Apply conflict penalty
        final_score = weighted_score * (1.0 - conflict_analysis.confidence_impact * 0.2)
        
        return max(0.0, min(1.0, final_score))
    
    def _get_historical_performance(self, model_names: List[str], context: Dict[str, Any]) -> float:
        """Get historical performance score for the model combination"""
        # This would query historical data in a real implementation
        # For now, return a baseline score
        
        task_type = context.get('task_type', 'general')
        combination_key = tuple(sorted(model_names))
        
        if combination_key in self.performance_history:
            return self.performance_history[combination_key].get(task_type, 0.8)
        
        return 0.8  # Default baseline
    
    def _determine_confidence_level(self, confidence_score: float) -> ConfidenceLevel:
        """Determine confidence level category"""
        if confidence_score >= 0.95:
            return ConfidenceLevel.VERY_HIGH
        elif confidence_score >= 0.85:
            return ConfidenceLevel.HIGH
        elif confidence_score >= 0.75:
            return ConfidenceLevel.MEDIUM_HIGH
        elif confidence_score >= 0.60:
            return ConfidenceLevel.MEDIUM
        elif confidence_score >= 0.40:
            return ConfidenceLevel.MEDIUM_LOW
        elif confidence_score >= 0.20:
            return ConfidenceLevel.LOW
        else:
            return ConfidenceLevel.VERY_LOW
    
    def _calculate_quality_indicators(self, results: List[Any], context: Dict[str, Any]) -> Dict[str, float]:
        """Calculate various quality indicators"""
        indicators = {}
        
        # Response time quality (faster is better, but not too fast)
        response_times = [r.processing_time for r in results]
        avg_response_time = statistics.mean(response_times)
        
        # Optimal response time range (2-10 seconds)
        if 2.0 <= avg_response_time <= 10.0:
            time_quality = 1.0
        elif avg_response_time < 2.0:
            time_quality = 0.7  # Too fast might indicate shallow analysis
        else:
            time_quality = max(0.2, 1.0 - (avg_response_time - 10.0) / 20.0)
        
        indicators['response_time_quality'] = time_quality
        
        # Cost efficiency
        total_cost = sum(r.cost for r in results)
        if total_cost <= 0.01:
            cost_efficiency = 1.0
        elif total_cost <= 0.05:
            cost_efficiency = 0.8
        elif total_cost <= 0.10:
            cost_efficiency = 0.6
        else:
            cost_efficiency = max(0.2, 1.0 - total_cost)
        
        indicators['cost_efficiency'] = cost_efficiency
        
        # Explanation quality (length and informativeness)
        explanations = [r.explanation for r in results if r.explanation]
        if explanations:
            avg_explanation_length = statistics.mean([len(exp.split()) for exp in explanations])
            # Optimal explanation length (20-100 words)
            if 20 <= avg_explanation_length <= 100:
                explanation_quality = 1.0
            elif avg_explanation_length < 20:
                explanation_quality = avg_explanation_length / 20.0
            else:
                explanation_quality = max(0.5, 1.0 - (avg_explanation_length - 100) / 200.0)
        else:
            explanation_quality = 0.3
        
        indicators['explanation_quality'] = explanation_quality
        
        # Suggestion quality (number and relevance)
        total_suggestions = sum(len(r.suggestions) for r in results)
        avg_suggestions = total_suggestions / len(results) if results else 0
        
        if 1 <= avg_suggestions <= 5:
            suggestion_quality = 1.0
        elif avg_suggestions == 0:
            suggestion_quality = 0.4
        else:
            suggestion_quality = max(0.6, 1.0 - abs(avg_suggestions - 3) / 10.0)
        
        indicators['suggestion_quality'] = suggestion_quality
        
        return indicators
    
    def _generate_recommendations(self, results: List[Any], consensus_score: float,
                                conflict_analysis: ConflictAnalysis, 
                                quality_indicators: Dict[str, float]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Consensus-based recommendations
        if consensus_score < 0.6:
            recommendations.append(
                "Low consensus detected. Consider using cross-validation mode or "
                "increasing quality settings for more consistent results."
            )
        elif consensus_score > 0.9:
            recommendations.append(
                "High consensus achieved. Results are highly reliable."
            )
        
        # Conflict-based recommendations
        if conflict_analysis.conflict_areas:
            recommendations.extend(conflict_analysis.resolution_suggestions[:2])
        
        # Quality-based recommendations
        if quality_indicators.get('response_time_quality', 1.0) < 0.7:
            avg_time = statistics.mean([r.processing_time for r in results])
            if avg_time < 2.0:
                recommendations.append(
                    "Very fast response time. Consider using higher quality settings "
                    "for more thorough analysis."
                )
            else:
                recommendations.append(
                    "Slow response time detected. Consider using faster models or "
                    "reducing input complexity."
                )
        
        if quality_indicators.get('cost_efficiency', 1.0) < 0.6:
            recommendations.append(
                "High cost detected. Consider using more cost-effective model combinations "
                "or reducing the number of models used."
            )
        
        if quality_indicators.get('explanation_quality', 1.0) < 0.6:
            recommendations.append(
                "Consider requesting more detailed explanations or using models "
                "that provide better documentation."
            )
        
        # Model-specific recommendations
        model_confidences = {r.model: r.confidence for r in results}
        low_confidence_models = [model for model, conf in model_confidences.items() if conf < 0.7]
        
        if low_confidence_models:
            recommendations.append(
                f"Models with low confidence: {', '.join(low_confidence_models)}. "
                "Consider excluding these models or adjusting request parameters."
            )
        
        # Limit to most important recommendations
        return recommendations[:5]
    
    def _single_result_analysis(self, result: Optional[Any]) -> ConsensusResult:
        """Handle analysis when only one result is available"""
        if not result:
            return ConsensusResult(
                consensus_score=0.0,
                confidence_score=0.0,
                confidence_level=ConfidenceLevel.VERY_LOW,
                recommendations=["No results available for analysis"]
            )
        
        confidence_score = result.confidence
        confidence_level = self._determine_confidence_level(confidence_score)
        
        recommendations = []
        if confidence_score < 0.7:
            recommendations.append("Single result with low confidence. Consider using multiple models for validation.")
        else:
            recommendations.append("Single result with acceptable confidence. Consider adding validation for critical transformations.")
        
        return ConsensusResult(
            consensus_score=1.0,  # Perfect consensus with itself
            confidence_score=confidence_score,
            confidence_level=confidence_level,
            quality_indicators={
                'response_time_quality': 1.0 if 2.0 <= result.processing_time <= 10.0 else 0.7,
                'cost_efficiency': 1.0 if result.cost <= 0.01 else 0.8,
                'explanation_quality': 1.0 if result.explanation else 0.3,
                'suggestion_quality': 1.0 if result.suggestions else 0.4
            },
            recommendations=recommendations,
            metadata={
                'analysis_timestamp': datetime.now().isoformat(),
                'num_results': 1,
                'single_result_analysis': True
            }
        )
    
    def _fallback_consensus_result(self, results: List[Any]) -> ConsensusResult:
        """Fallback consensus result when analysis fails"""
        avg_confidence = statistics.mean([r.confidence for r in results]) if results else 0.0
        
        return ConsensusResult(
            consensus_score=0.5,  # Neutral consensus
            confidence_score=avg_confidence,
            confidence_level=self._determine_confidence_level(avg_confidence),
            recommendations=["Analysis failed. Manual review recommended."],
            metadata={
                'analysis_timestamp': datetime.now().isoformat(),
                'num_results': len(results),
                'fallback_analysis': True
            }
        )
    
    def update_model_weights(self, model_name: str, performance_score: float):
        """Update model weights based on performance feedback"""
        if model_name in self.model_weights:
            # Exponential moving average
            alpha = 0.1
            self.model_weights[model_name] = (
                alpha * performance_score + 
                (1 - alpha) * self.model_weights[model_name]
            )
    
    def update_performance_history(self, model_combination: List[str], 
                                 task_type: str, success_rate: float):
        """Update historical performance tracking"""
        combination_key = tuple(sorted(model_combination))
        
        if combination_key not in self.performance_history:
            self.performance_history[combination_key] = {}
        
        if task_type not in self.performance_history[combination_key]:
            self.performance_history[combination_key][task_type] = success_rate
        else:
            # Exponential moving average
            alpha = 0.2
            current = self.performance_history[combination_key][task_type]
            self.performance_history[combination_key][task_type] = (
                alpha * success_rate + (1 - alpha) * current
            )