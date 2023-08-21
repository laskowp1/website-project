from typing import Tuple, Any, List
from dataclasses import dataclass

from website_project.activity.description_fields.base import HtmlField, PythonType


@dataclass
class Schema:
    name: str
    type: PythonType
    required: bool
    default: Any


class Activity:

    def __init__(self, name, description_fields: Tuple[HtmlField]) -> None:
        self.name = name
        self.description_fields = description_fields

    def schema(self) -> List[Schema]:
        return [
            Schema(field.name, field.python_type, field.required, field.default)
            for field in self.description_fields
        ]

    def __str__(self):
        return self.name
