"""
CodeVerter Extensibility Framework

This module provides a comprehensive extensibility framework for the CodeVerter
Multi-API Collaborative AI Review System, enabling:
1. Plugin architecture for new AI services
2. Custom review mode implementations
3. Extensible scoring algorithms
4. Configuration-driven model profiles
5. Integration hooks for external systems
6. Custom UI components and themes
"""

import asyncio
import json
import importlib
import inspect
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Type, Callable, Union
from datetime import datetime
from enum import Enum
import logging
import pkgutil
import sys
from pathlib import Path

# Plugin system imports
try:
    import pluggy
    HAS_PLUGGY = True
except ImportError:
    HAS_PLUGGY = False
    logging.warning("Pluggy not available, using basic plugin system")


class PluginType(Enum):
    """Types of plugins supported"""
    API_ADAPTER = "api_adapter"
    REVIEW_MODE = "review_mode"
    SCORING_ALGORITHM = "scoring_algorithm"
    UI_COMPONENT = "ui_component"
    INTEGRATION_HOOK = "integration_hook"
    TRANSFORMATION_FILTER = "transformation_filter"
    COST_CALCULATOR = "cost_calculator"
    PERFORMANCE_MONITOR = "performance_monitor"


class ExtensionPoint(Enum):
    """Extension points in the system"""
    PRE_TRANSFORMATION = "pre_transformation"
    POST_TRANSFORMATION = "post_transformation"
    PRE_CONSENSUS = "pre_consensus"
    POST_CONSENSUS = "post_consensus"
    ERROR_HANDLING = "error_handling"
    RESULT_FORMATTING = "result_formatting"
    UI_RENDERING = "ui_rendering"
    METRICS_COLLECTION = "metrics_collection"


@dataclass
class PluginMetadata:
    """Metadata for a plugin"""
    name: str
    version: str
    description: str
    author: str
    plugin_type: PluginType
    dependencies: List[str] = field(default_factory=list)
    configuration_schema: Dict[str, Any] = field(default_factory=dict)
    extension_points: List[ExtensionPoint] = field(default_factory=list)
    compatibility: Dict[str, Any] = field(default_factory=dict)
    license: str = "MIT"
    repository: Optional[str] = None
    documentation_url: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "plugin_type": self.plugin_type.value,
            "dependencies": self.dependencies,
            "configuration_schema": self.configuration_schema,
            "extension_points": [ep.value for ep in self.extension_points],
            "compatibility": self.compatibility,
            "license": self.license,
            "repository": self.repository,
            "documentation_url": self.documentation_url
        }


@dataclass
class PluginConfiguration:
    """Configuration for a plugin instance"""
    plugin_name: str
    enabled: bool = True
    configuration: Dict[str, Any] = field(default_factory=dict)
    priority: int = 50  # 0-100, higher = higher priority
    conditions: Dict[str, Any] = field(default_factory=dict)  # When to activate
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "plugin_name": self.plugin_name,
            "enabled": self.enabled,
            "configuration": self.configuration,
            "priority": self.priority,
            "conditions": self.conditions
        }


class BasePlugin(ABC):
    """Base class for all plugins"""
    
    def __init__(self, configuration: Dict[str, Any] = None):
        self.configuration = configuration or {}
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.is_initialized = False
        self.performance_metrics = {
            "total_calls": 0,
            "successful_calls": 0,
            "total_time": 0.0,
            "errors": []
        }
    
    @property
    @abstractmethod
    def metadata(self) -> PluginMetadata:
        """Plugin metadata"""
        pass
    
    async def initialize(self) -> bool:
        """Initialize the plugin"""
        try:
            await self._initialize_impl()
            self.is_initialized = True
            self.logger.info(f"Plugin {self.metadata.name} initialized successfully")
            return True
        except Exception as e:
            self.logger.error(f"Failed to initialize plugin {self.metadata.name}: {e}")
            return False
    
    async def _initialize_impl(self):
        """Override this for custom initialization"""
        pass
    
    async def cleanup(self):
        """Cleanup plugin resources"""
        try:
            await self._cleanup_impl()
            self.is_initialized = False
            self.logger.info(f"Plugin {self.metadata.name} cleaned up")
        except Exception as e:
            self.logger.error(f"Failed to cleanup plugin {self.metadata.name}: {e}")
    
    async def _cleanup_impl(self):
        """Override this for custom cleanup"""
        pass
    
    def validate_configuration(self, config: Dict[str, Any]) -> bool:
        """Validate plugin configuration"""
        try:
            return self._validate_configuration_impl(config)
        except Exception as e:
            self.logger.error(f"Configuration validation failed: {e}")
            return False
    
    def _validate_configuration_impl(self, config: Dict[str, Any]) -> bool:
        """Override this for custom validation"""
        return True
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get plugin performance metrics"""
        avg_time = (self.performance_metrics["total_time"] / 
                   max(self.performance_metrics["total_calls"], 1))
        success_rate = (self.performance_metrics["successful_calls"] / 
                       max(self.performance_metrics["total_calls"], 1))
        
        return {
            "plugin_name": self.metadata.name,
            "total_calls": self.performance_metrics["total_calls"],
            "success_rate": success_rate,
            "avg_execution_time": avg_time,
            "error_count": len(self.performance_metrics["errors"]),
            "last_errors": self.performance_metrics["errors"][-5:]  # Last 5 errors
        }
    
    def _record_call(self, success: bool, execution_time: float, error: str = None):
        """Record performance metrics for a call"""
        self.performance_metrics["total_calls"] += 1
        self.performance_metrics["total_time"] += execution_time
        
        if success:
            self.performance_metrics["successful_calls"] += 1
        else:
            self.performance_metrics["errors"].append({
                "timestamp": datetime.now().isoformat(),
                "error": error or "Unknown error"
            })
            
            # Keep only last 100 errors
            if len(self.performance_metrics["errors"]) > 100:
                self.performance_metrics["errors"] = self.performance_metrics["errors"][-100:]


class BaseAPIAdapter(BasePlugin):
    """Base class for API adapter plugins"""
    
    @abstractmethod
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Transform code using this API"""
        pass
    
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the API is healthy"""
        pass
    
    @abstractmethod
    def get_cost_estimate(self, input_length: int, complexity: float = 1.0) -> float:
        """Estimate cost for transformation"""
        pass


class BaseReviewMode(BasePlugin):
    """Base class for review mode plugins"""
    
    @abstractmethod
    async def execute_review(self, request: Any, selected_models: List[str], 
                           api_manager: Any) -> Any:
        """Execute the review mode"""
        pass
    
    @abstractmethod
    def get_optimal_model_count(self) -> Tuple[int, int]:
        """Get optimal model count range (min, max)"""
        pass
    
    @abstractmethod
    def supports_streaming(self) -> bool:
        """Whether this mode supports streaming results"""
        pass


class BaseScoringAlgorithm(BasePlugin):
    """Base class for scoring algorithm plugins"""
    
    @abstractmethod
    async def calculate_consensus_score(self, results: List[Any], 
                                      context: Dict[str, Any]) -> float:
        """Calculate consensus score"""
        pass
    
    @abstractmethod
    async def calculate_confidence_score(self, results: List[Any], 
                                       consensus_score: float,
                                       context: Dict[str, Any]) -> float:
        """Calculate confidence score"""
        pass


class BaseUIComponent(BasePlugin):
    """Base class for UI component plugins"""
    
    @abstractmethod
    def render_html(self, data: Dict[str, Any]) -> str:
        """Render HTML for the component"""
        pass
    
    @abstractmethod
    def render_css(self) -> str:
        """Render CSS for the component"""
        pass
    
    @abstractmethod
    def render_javascript(self) -> str:
        """Render JavaScript for the component"""
        pass


class BaseIntegrationHook(BasePlugin):
    """Base class for integration hook plugins"""
    
    @abstractmethod
    async def handle_event(self, event_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle integration event"""
        pass
    
    @abstractmethod
    def get_supported_events(self) -> List[str]:
        """Get list of supported event types"""
        pass


class PluginRegistry:
    """Registry for managing plugins"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.plugins: Dict[str, BasePlugin] = {}
        self.plugin_metadata: Dict[str, PluginMetadata] = {}
        self.plugin_configurations: Dict[str, PluginConfiguration] = {}
        self.extension_points: Dict[ExtensionPoint, List[str]] = {}
        self.plugin_dependencies: Dict[str, List[str]] = {}
        
        # Initialize extension points
        for ep in ExtensionPoint:
            self.extension_points[ep] = []
    
    def register_plugin(self, plugin: BasePlugin, configuration: PluginConfiguration = None) -> bool:
        """Register a plugin"""
        try:
            metadata = plugin.metadata
            
            # Validate plugin
            if not self._validate_plugin(plugin):
                return False
            
            # Check dependencies
            if not self._check_dependencies(metadata.dependencies):
                self.logger.error(f"Plugin {metadata.name} has unmet dependencies")
                return False
            
            # Register plugin
            self.plugins[metadata.name] = plugin
            self.plugin_metadata[metadata.name] = metadata
            
            if configuration:
                self.plugin_configurations[metadata.name] = configuration
            else:
                self.plugin_configurations[metadata.name] = PluginConfiguration(
                    plugin_name=metadata.name
                )
            
            # Register extension points
            for ep in metadata.extension_points:
                if metadata.name not in self.extension_points[ep]:
                    self.extension_points[ep].append(metadata.name)
            
            # Track dependencies
            self.plugin_dependencies[metadata.name] = metadata.dependencies
            
            self.logger.info(f"Registered plugin: {metadata.name} v{metadata.version}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to register plugin: {e}")
            return False
    
    def unregister_plugin(self, plugin_name: str) -> bool:
        """Unregister a plugin"""
        try:
            if plugin_name not in self.plugins:
                return False
            
            # Check if other plugins depend on this one
            dependents = self._get_dependents(plugin_name)
            if dependents:
                self.logger.error(f"Cannot unregister {plugin_name}, required by: {dependents}")
                return False
            
            # Cleanup plugin
            plugin = self.plugins[plugin_name]
            asyncio.create_task(plugin.cleanup())
            
            # Remove from registries
            del self.plugins[plugin_name]
            del self.plugin_metadata[plugin_name]
            del self.plugin_configurations[plugin_name]
            del self.plugin_dependencies[plugin_name]
            
            # Remove from extension points
            for ep_plugins in self.extension_points.values():
                if plugin_name in ep_plugins:
                    ep_plugins.remove(plugin_name)
            
            self.logger.info(f"Unregistered plugin: {plugin_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to unregister plugin {plugin_name}: {e}")
            return False
    
    def get_plugin(self, plugin_name: str) -> Optional[BasePlugin]:
        """Get a plugin by name"""
        return self.plugins.get(plugin_name)
    
    def get_plugins_by_type(self, plugin_type: PluginType) -> List[BasePlugin]:
        """Get all plugins of a specific type"""
        return [
            plugin for plugin in self.plugins.values()
            if plugin.metadata.plugin_type == plugin_type
        ]
    
    def get_plugins_for_extension_point(self, extension_point: ExtensionPoint) -> List[BasePlugin]:
        """Get plugins that implement a specific extension point"""
        plugin_names = self.extension_points.get(extension_point, [])
        
        # Sort by priority
        plugins_with_priority = []
        for name in plugin_names:
            if name in self.plugins and self.plugin_configurations[name].enabled:
                plugin = self.plugins[name]
                priority = self.plugin_configurations[name].priority
                plugins_with_priority.append((priority, plugin))
        
        # Sort by priority (highest first)
        plugins_with_priority.sort(key=lambda x: x[0], reverse=True)
        
        return [plugin for priority, plugin in plugins_with_priority]
    
    def list_plugins(self) -> List[Dict[str, Any]]:
        """List all registered plugins"""
        return [
            {
                "metadata": metadata.to_dict(),
                "configuration": self.plugin_configurations[name].to_dict(),
                "initialized": self.plugins[name].is_initialized,
                "performance": self.plugins[name].get_performance_metrics()
            }
            for name, metadata in self.plugin_metadata.items()
        ]
    
    async def initialize_plugins(self) -> Dict[str, bool]:
        """Initialize all plugins"""
        results = {}
        
        # Sort plugins by dependencies
        sorted_plugins = self._topological_sort()
        
        for plugin_name in sorted_plugins:
            if plugin_name in self.plugins:
                plugin = self.plugins[plugin_name]
                config = self.plugin_configurations[plugin_name]
                
                if config.enabled:
                    results[plugin_name] = await plugin.initialize()
                else:
                    results[plugin_name] = True  # Disabled plugins are "successful"
        
        return results
    
    async def cleanup_plugins(self):
        """Cleanup all plugins"""
        for plugin in self.plugins.values():
            try:
                await plugin.cleanup()
            except Exception as e:
                self.logger.error(f"Error cleaning up plugin {plugin.metadata.name}: {e}")
    
    def _validate_plugin(self, plugin: BasePlugin) -> bool:
        """Validate a plugin"""
        try:
            # Check if it has required metadata
            metadata = plugin.metadata
            if not metadata or not metadata.name:
                return False
            
            # Check if plugin type is supported
            if metadata.plugin_type not in PluginType:
                return False
            
            # Check if it implements required methods based on type
            if metadata.plugin_type == PluginType.API_ADAPTER:
                if not isinstance(plugin, BaseAPIAdapter):
                    return False
            elif metadata.plugin_type == PluginType.REVIEW_MODE:
                if not isinstance(plugin, BaseReviewMode):
                    return False
            elif metadata.plugin_type == PluginType.SCORING_ALGORITHM:
                if not isinstance(plugin, BaseScoringAlgorithm):
                    return False
            elif metadata.plugin_type == PluginType.UI_COMPONENT:
                if not isinstance(plugin, BaseUIComponent):
                    return False
            elif metadata.plugin_type == PluginType.INTEGRATION_HOOK:
                if not isinstance(plugin, BaseIntegrationHook):
                    return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Plugin validation failed: {e}")
            return False
    
    def _check_dependencies(self, dependencies: List[str]) -> bool:
        """Check if all dependencies are available"""
        for dep in dependencies:
            if dep not in self.plugins:
                return False
        return True
    
    def _get_dependents(self, plugin_name: str) -> List[str]:
        """Get plugins that depend on the given plugin"""
        dependents = []
        for name, deps in self.plugin_dependencies.items():
            if plugin_name in deps:
                dependents.append(name)
        return dependents
    
    def _topological_sort(self) -> List[str]:
        """Sort plugins by dependencies using topological sort"""
        # Simplified topological sort
        visited = set()
        result = []
        
        def visit(plugin_name: str):
            if plugin_name in visited:
                return
            
            visited.add(plugin_name)
            
            # Visit dependencies first
            if plugin_name in self.plugin_dependencies:
                for dep in self.plugin_dependencies[plugin_name]:
                    if dep in self.plugins:
                        visit(dep)
            
            result.append(plugin_name)
        
        for plugin_name in self.plugins:
            visit(plugin_name)
        
        return result


class PluginLoader:
    """Loads plugins from various sources"""
    
    def __init__(self, plugin_registry: PluginRegistry):
        self.registry = plugin_registry
        self.logger = logging.getLogger(__name__)
        self.plugin_directories = ["plugins", "extensions", "addons"]
    
    def add_plugin_directory(self, directory: str):
        """Add a directory to search for plugins"""
        if directory not in self.plugin_directories:
            self.plugin_directories.append(directory)
    
    async def load_from_directory(self, directory: str) -> Dict[str, bool]:
        """Load plugins from a directory"""
        results = {}
        
        try:
            plugin_dir = Path(directory)
            if not plugin_dir.exists():
                self.logger.warning(f"Plugin directory {directory} does not exist")
                return results
            
            # Add to Python path
            sys.path.insert(0, str(plugin_dir))
            
            try:
                # Scan for plugin modules
                for module_info in pkgutil.iter_modules([str(plugin_dir)]):
                    module_name = module_info.name
                    
                    try:
                        # Import module
                        module = importlib.import_module(module_name)
                        
                        # Find plugin classes
                        for name, obj in inspect.getmembers(module, inspect.isclass):
                            if (issubclass(obj, BasePlugin) and 
                                obj != BasePlugin and 
                                not inspect.isabstract(obj)):
                                
                                # Create plugin instance
                                plugin = obj()
                                
                                # Register plugin
                                success = self.registry.register_plugin(plugin)
                                results[f"{module_name}.{name}"] = success
                                
                    except Exception as e:
                        self.logger.error(f"Failed to load plugin module {module_name}: {e}")
                        results[module_name] = False
                        
            finally:
                # Remove from Python path
                sys.path.remove(str(plugin_dir))
                
        except Exception as e:
            self.logger.error(f"Failed to load plugins from {directory}: {e}")
        
        return results
    
    async def load_from_package(self, package_name: str) -> bool:
        """Load plugin from installed package"""
        try:
            # Import package
            package = importlib.import_module(package_name)
            
            # Look for plugin entry point
            if hasattr(package, 'get_plugin'):
                plugin = package.get_plugin()
                return self.registry.register_plugin(plugin)
            elif hasattr(package, 'Plugin'):
                plugin = package.Plugin()
                return self.registry.register_plugin(plugin)
            else:
                self.logger.error(f"Package {package_name} does not have plugin entry point")
                return False
                
        except ImportError as e:
            self.logger.error(f"Failed to import plugin package {package_name}: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Failed to load plugin from package {package_name}: {e}")
            return False
    
    async def load_from_config(self, config_file: str) -> Dict[str, bool]:
        """Load plugins from configuration file"""
        results = {}
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            plugins_config = config.get("plugins", [])
            
            for plugin_config in plugins_config:
                plugin_type = plugin_config.get("type", "package")
                plugin_name = plugin_config.get("name")
                
                if plugin_type == "package":
                    success = await self.load_from_package(plugin_name)
                    results[plugin_name] = success
                elif plugin_type == "directory":
                    directory_results = await self.load_from_directory(plugin_name)
                    results.update(directory_results)
                else:
                    self.logger.error(f"Unknown plugin type: {plugin_type}")
                    results[plugin_name] = False
        
        except Exception as e:
            self.logger.error(f"Failed to load plugins from config {config_file}: {e}")
        
        return results


class ExtensibilityManager:
    """Main manager for the extensibility framework"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.plugin_registry = PluginRegistry()
        self.plugin_loader = PluginLoader(self.plugin_registry)
        self.event_handlers: Dict[str, List[Callable]] = {}
        self.is_initialized = False
    
    async def initialize(self, config: Dict[str, Any] = None) -> bool:
        """Initialize the extensibility framework"""
        try:
            config = config or {}
            
            # Load core plugins
            await self._load_core_plugins()
            
            # Load plugins from directories
            plugin_dirs = config.get("plugin_directories", ["plugins"])
            for directory in plugin_dirs:
                await self.plugin_loader.load_from_directory(directory)
            
            # Load plugins from packages
            plugin_packages = config.get("plugin_packages", [])
            for package in plugin_packages:
                await self.plugin_loader.load_from_package(package)
            
            # Load plugins from config file
            config_file = config.get("plugin_config_file")
            if config_file:
                await self.plugin_loader.load_from_config(config_file)
            
            # Initialize all plugins
            init_results = await self.plugin_registry.initialize_plugins()
            
            # Log results
            successful = sum(1 for success in init_results.values() if success)
            total = len(init_results)
            self.logger.info(f"Initialized {successful}/{total} plugins successfully")
            
            self.is_initialized = True
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize extensibility framework: {e}")
            return False
    
    async def cleanup(self):
        """Cleanup the extensibility framework"""
        await self.plugin_registry.cleanup_plugins()
        self.is_initialized = False
    
    def get_api_adapters(self) -> List[BaseAPIAdapter]:
        """Get all API adapter plugins"""
        return self.plugin_registry.get_plugins_by_type(PluginType.API_ADAPTER)
    
    def get_review_modes(self) -> List[BaseReviewMode]:
        """Get all review mode plugins"""
        return self.plugin_registry.get_plugins_by_type(PluginType.REVIEW_MODE)
    
    def get_scoring_algorithms(self) -> List[BaseScoringAlgorithm]:
        """Get all scoring algorithm plugins"""
        return self.plugin_registry.get_plugins_by_type(PluginType.SCORING_ALGORITHM)
    
    def get_ui_components(self) -> List[BaseUIComponent]:
        """Get all UI component plugins"""
        return self.plugin_registry.get_plugins_by_type(PluginType.UI_COMPONENT)
    
    def get_integration_hooks(self) -> List[BaseIntegrationHook]:
        """Get all integration hook plugins"""
        return self.plugin_registry.get_plugins_by_type(PluginType.INTEGRATION_HOOK)
    
    async def execute_hooks(self, extension_point: ExtensionPoint, 
                          data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute hooks for an extension point"""
        plugins = self.plugin_registry.get_plugins_for_extension_point(extension_point)
        
        result_data = data.copy()
        
        for plugin in plugins:
            try:
                if isinstance(plugin, BaseIntegrationHook):
                    hook_result = await plugin.handle_event(extension_point.value, result_data)
                    if hook_result:
                        result_data.update(hook_result)
                        
            except Exception as e:
                self.logger.error(f"Hook execution failed for {plugin.metadata.name}: {e}")
        
        return result_data
    
    def register_event_handler(self, event_type: str, handler: Callable):
        """Register an event handler"""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)
    
    async def emit_event(self, event_type: str, data: Dict[str, Any]):
        """Emit an event to all registered handlers"""
        handlers = self.event_handlers.get(event_type, [])
        
        for handler in handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(data)
                else:
                    handler(data)
            except Exception as e:
                self.logger.error(f"Event handler failed for {event_type}: {e}")
    
    def get_plugin_status(self) -> Dict[str, Any]:
        """Get status of all plugins"""
        return {
            "total_plugins": len(self.plugin_registry.plugins),
            "initialized_plugins": sum(
                1 for plugin in self.plugin_registry.plugins.values()
                if plugin.is_initialized
            ),
            "plugins_by_type": {
                plugin_type.value: len(self.plugin_registry.get_plugins_by_type(plugin_type))
                for plugin_type in PluginType
            },
            "extension_points": {
                ep.value: len(plugins) for ep, plugins in self.plugin_registry.extension_points.items()
            }
        }
    
    def get_plugin_performance(self) -> List[Dict[str, Any]]:
        """Get performance metrics for all plugins"""
        return [
            plugin.get_performance_metrics()
            for plugin in self.plugin_registry.plugins.values()
        ]
    
    async def _load_core_plugins(self):
        """Load core built-in plugins"""
        # This would load essential plugins that come with the system
        pass


# Example plugin implementations
class ExampleAPIAdapter(BaseAPIAdapter):
    """Example API adapter plugin"""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="example_api_adapter",
            version="1.0.0",
            description="Example API adapter for demonstration",
            author="SERAPHINA Framework",
            plugin_type=PluginType.API_ADAPTER,
            extension_points=[ExtensionPoint.PRE_TRANSFORMATION, ExtensionPoint.POST_TRANSFORMATION]
        )
    
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Example transformation"""
        import time
        start_time = time.time()
        
        try:
            # Simulate transformation
            await asyncio.sleep(0.1)
            
            transformed = f"// Transformed by Example API\n{code}"
            
            result = {
                "code": transformed,
                "explanation": "Example transformation with basic comment addition",
                "confidence": 0.8,
                "suggestions": ["Add more comprehensive error handling"],
                "metadata": {"api": "example"}
            }
            
            self._record_call(True, time.time() - start_time)
            return result
            
        except Exception as e:
            self._record_call(False, time.time() - start_time, str(e))
            raise
    
    async def health_check(self) -> bool:
        """Example health check"""
        return True
    
    def get_cost_estimate(self, input_length: int, complexity: float = 1.0) -> float:
        """Example cost estimation"""
        return input_length * 0.00001 * complexity


class ExampleReviewMode(BaseReviewMode):
    """Example review mode plugin"""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="example_review_mode",
            version="1.0.0",
            description="Example review mode for demonstration",
            author="SERAPHINA Framework",
            plugin_type=PluginType.REVIEW_MODE
        )
    
    async def execute_review(self, request: Any, selected_models: List[str], 
                           api_manager: Any) -> Any:
        """Example review execution"""
        import time
        start_time = time.time()
        
        try:
            # Simple implementation: just use the first model
            if selected_models:
                result = await api_manager.call_model(selected_models[0], request)
                
                self._record_call(True, time.time() - start_time)
                return result
            else:
                raise ValueError("No models selected")
                
        except Exception as e:
            self._record_call(False, time.time() - start_time, str(e))
            raise
    
    def get_optimal_model_count(self) -> Tuple[int, int]:
        """Example optimal model count"""
        return (1, 3)
    
    def supports_streaming(self) -> bool:
        """Example streaming support"""
        return False


# Configuration management
class ConfigurationManager:
    """Manages plugin configurations"""
    
    def __init__(self, config_file: str = "plugin_config.json"):
        self.config_file = config_file
        self.logger = logging.getLogger(__name__)
        self.configurations: Dict[str, PluginConfiguration] = {}
    
    def load_configurations(self) -> bool:
        """Load configurations from file"""
        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)
            
            for plugin_name, config_data in data.items():
                config = PluginConfiguration(
                    plugin_name=plugin_name,
                    enabled=config_data.get("enabled", True),
                    configuration=config_data.get("configuration", {}),
                    priority=config_data.get("priority", 50),
                    conditions=config_data.get("conditions", {})
                )
                self.configurations[plugin_name] = config
            
            return True
            
        except FileNotFoundError:
            self.logger.info(f"Configuration file {self.config_file} not found, using defaults")
            return True
        except Exception as e:
            self.logger.error(f"Failed to load configurations: {e}")
            return False
    
    def save_configurations(self) -> bool:
        """Save configurations to file"""
        try:
            data = {
                plugin_name: config.to_dict()
                for plugin_name, config in self.configurations.items()
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to save configurations: {e}")
            return False
    
    def get_configuration(self, plugin_name: str) -> Optional[PluginConfiguration]:
        """Get configuration for a plugin"""
        return self.configurations.get(plugin_name)
    
    def set_configuration(self, plugin_name: str, configuration: PluginConfiguration):
        """Set configuration for a plugin"""
        self.configurations[plugin_name] = configuration
    
    def enable_plugin(self, plugin_name: str):
        """Enable a plugin"""
        if plugin_name in self.configurations:
            self.configurations[plugin_name].enabled = True
    
    def disable_plugin(self, plugin_name: str):
        """Disable a plugin"""
        if plugin_name in self.configurations:
            self.configurations[plugin_name].enabled = False


# Plugin development utilities
class PluginDeveloperToolkit:
    """Utilities for plugin developers"""
    
    @staticmethod
    def create_plugin_template(plugin_name: str, plugin_type: PluginType, 
                             output_dir: str = "plugins") -> bool:
        """Create a plugin template"""
        try:
            plugin_dir = Path(output_dir) / plugin_name
            plugin_dir.mkdir(parents=True, exist_ok=True)
            
            # Create __init__.py
            init_content = f'''"""
{plugin_name} Plugin for CodeVerter
"""

from .plugin import {plugin_name.title()}Plugin

def get_plugin():
    """Plugin entry point"""
    return {plugin_name.title()}Plugin()
'''
            
            with open(plugin_dir / "__init__.py", "w") as f:
                f.write(init_content)
            
            # Create plugin.py based on type
            plugin_content = PluginDeveloperToolkit._generate_plugin_template(plugin_name, plugin_type)
            
            with open(plugin_dir / "plugin.py", "w") as f:
                f.write(plugin_content)
            
            # Create README.md
            readme_content = f'''# {plugin_name} Plugin

## Description
{plugin_name} plugin for CodeVerter Multi-API Collaborative AI Review System.

## Installation
Copy this directory to your CodeVerter plugins folder.

## Configuration
Add configuration in plugin_config.json:

```json
{{
  "{plugin_name}": {{
    "enabled": true,
    "configuration": {{}},
    "priority": 50
  }}
}}
```

## Usage
The plugin will be automatically loaded when CodeVerter starts.
'''
            
            with open(plugin_dir / "README.md", "w") as f:
                f.write(readme_content)
            
            return True
            
        except Exception as e:
            logging.error(f"Failed to create plugin template: {e}")
            return False
    
    @staticmethod
    def _generate_plugin_template(plugin_name: str, plugin_type: PluginType) -> str:
        """Generate plugin template based on type"""
        
        class_name = f"{plugin_name.title()}Plugin"
        
        if plugin_type == PluginType.API_ADAPTER:
            base_class = "BaseAPIAdapter"
            methods = '''
    async def transform_code(self, code: str, source_lang: str, target_lang: str,
                           requirements: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Transform code using this API"""
        # Implement your API call here
        return {
            "code": code,  # Replace with transformed code
            "explanation": "Transformation explanation",
            "confidence": 0.8,
            "suggestions": [],
            "metadata": {}
        }
    
    async def health_check(self) -> bool:
        """Check if the API is healthy"""
        # Implement health check
        return True
    
    def get_cost_estimate(self, input_length: int, complexity: float = 1.0) -> float:
        """Estimate cost for transformation"""
        # Implement cost estimation
        return 0.0
'''
        elif plugin_type == PluginType.REVIEW_MODE:
            base_class = "BaseReviewMode"
            methods = '''
    async def execute_review(self, request: Any, selected_models: List[str], 
                           api_manager: Any) -> Any:
        """Execute the review mode"""
        # Implement your review mode logic here
        pass
    
    def get_optimal_model_count(self) -> Tuple[int, int]:
        """Get optimal model count range (min, max)"""
        return (1, 5)
    
    def supports_streaming(self) -> bool:
        """Whether this mode supports streaming results"""
        return False
'''
        else:
            base_class = "BasePlugin"
            methods = '''
    # Implement your plugin methods here
    pass
'''
        
        return f'''"""
{plugin_name} Plugin Implementation
"""

from typing import Dict, List, Any, Optional, Tuple
from codeverter.extensibility_framework import (
    {base_class}, PluginMetadata, PluginType, ExtensionPoint
)


class {class_name}({base_class}):
    """
    {plugin_name} plugin for CodeVerter
    """
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="{plugin_name}",
            version="1.0.0",
            description="{plugin_name} plugin for CodeVerter",
            author="Your Name",
            plugin_type=PluginType.{plugin_type.name},
            dependencies=[],
            extension_points=[]
        )
    
    async def _initialize_impl(self):
        """Initialize the plugin"""
        # Add initialization logic here
        pass
    
    async def _cleanup_impl(self):
        """Cleanup plugin resources"""
        # Add cleanup logic here
        pass
{methods}
'''
    
    @staticmethod
    def validate_plugin_structure(plugin_dir: str) -> Dict[str, bool]:
        """Validate plugin directory structure"""
        plugin_path = Path(plugin_dir)
        
        checks = {
            "directory_exists": plugin_path.exists(),
            "has_init_py": (plugin_path / "__init__.py").exists(),
            "has_plugin_py": (plugin_path / "plugin.py").exists(),
            "has_readme": (plugin_path / "README.md").exists()
        }
        
        if checks["has_plugin_py"]:
            try:
                # Try to import and validate plugin
                import sys
                sys.path.insert(0, str(plugin_path.parent))
                
                module = __import__(plugin_path.name)
                
                if hasattr(module, 'get_plugin'):
                    plugin = module.get_plugin()
                    checks["valid_plugin"] = isinstance(plugin, BasePlugin)
                    checks["has_metadata"] = hasattr(plugin, 'metadata')
                else:
                    checks["valid_plugin"] = False
                    checks["has_metadata"] = False
                    
                sys.path.remove(str(plugin_path.parent))
                
            except Exception:
                checks["valid_plugin"] = False
                checks["has_metadata"] = False
        
        return checks