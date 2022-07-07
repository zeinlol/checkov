from typing import List, Optional, Any, Dict

from checkov.common.graph.checks_infra.enums import Operators
from .contains_attribute_solver import ContainsAttributeSolver


class NotContainsAttributeSolver(ContainsAttributeSolver):
    operator = Operators.NOT_CONTAINS

    def __init__(self, resource_types: List[str], attribute: Optional[str], value: Any, is_jsonpath_check: bool = False) -> None:
        super().__init__(resource_types=resource_types, attribute=attribute, value=value,
                         is_jsonpath_check=is_jsonpath_check)

    def _get_operation(self, vertex: Dict[str, Any], attribute: Optional[str]) -> bool:
        return not super()._get_operation(vertex, attribute)
