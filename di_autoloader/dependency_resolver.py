from typing import Any
from dependency_injector import containers

class DependencyResolver:
    """Разрешает зависимости container.xxx → Provide[container.xxx]."""
    def __init__(self, container: containers.DeclarativeContainer):
        self.container = container

    def resolve(self, value: Any) -> Any:
        if isinstance(value, dict) and 'container' in value:
            # Use relations: {'container': 'key'}
            return self._prepare_container_str(value['container'], self.container)
        elif isinstance(value, dict) and 'config' in value:
            # Use configs: {'config': 'key'}
            return self.container.config.get(value['config'])
        elif isinstance(value, dict):
            return {key: self.resolve(val) for key, val in value.items()}
        elif isinstance(value, list):
            return [self.resolve(item) for item in value]
        return value

    def _prepare_container_str(self, value: str, relation: Any) -> Any:
        if hasattr(relation, value):
            resolved_value = getattr(relation, value)
            return resolved_value() if callable(resolved_value) else resolved_value