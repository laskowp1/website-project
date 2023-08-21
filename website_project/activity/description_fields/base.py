from abc import ABC, abstractmethod
from typing import Callable, NewType, Any
from enum import Enum

PythonType = NewType("PythonType", Callable)

IS_REQUIRED_HTML_CLASS_NAME = "is_required"


class Unit(Enum):
    M = "m"
    KM = "km"
    MIN = "min"


class HtmlType(Enum):
    NUMBER = "number"
    TEXT = "text"
    DATE = "date"


class HtmlField(ABC):

    def __init__(self, name: str, html_type: HtmlType, required: bool) -> None:
        self._name = name
        self.html_type = html_type
        self.required = required

    @property
    @abstractmethod
    def html_label_element(self) -> str:
        pass

    @property
    @abstractmethod
    def html_input_element(self) -> str:
        pass

    @property
    @abstractmethod
    def python_type(self) -> PythonType:
        pass

    @property
    def name(self) -> str:
        return self._name.strip().replace(" ", "_").lower()

    @property
    def default(self) -> Any:
        return
