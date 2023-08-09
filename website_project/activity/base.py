from abc import ABC, abstractmethod
from typing import Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


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
        self.name = name
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


class TextField(HtmlField):
    def __init__(self, name: str, required: bool):
        HtmlField.__init__(self, name, HtmlType.TEXT, required)

    @property
    def html_label_element(self) -> str:
        return (
            f"<label for='{self.name}'>"
            f"{self.name} {'(optional)' if not self.required else ''}"
            f"</label>"
        )

    @property
    def html_input_element(self) -> str:
        return (
            f"<input type='{self.html_type.value}'"
            f"id='{self.name}'"
            f"name='{self.name}'"
            f"{'required' if self.required else ''}"
            ">"
        )


class NumberField(HtmlField):
    def __init__(self, name: str, required: bool, unit: Unit, min_val: int = 0, max_val: int = 1000, step: float = 1.0):
        HtmlField.__init__(self, name, HtmlType.NUMBER, required)
        self.min_val = min_val
        self.max_val = max_val
        self.step = step
        self.unit = unit

    @property
    def html_label_element(self) -> str:
        return (
            f"<label for='{self.name}'>"
            f"{self.name} [{self.unit.value}] {'(optional)' if not self.required else ''}"
            f"</label>"
        )

    @property
    def html_input_element(self) -> str:
        return (
            f"<input type='{self.html_type.value}'"
            f"min='{self.min_val}'"
            f"max='{self.max_val}'"
            f"step='{self.step}'"
            f"id='{self.name}'"
            f"name='{self.name}'"
            f"{'required' if self.required else ''}"
            ">"
        )


@dataclass(frozen=True)
class Activity:
    name: str
    fields: Tuple[HtmlField]
    date: datetime = field(default_factory=datetime.now().date)


DISTANCE_IN_KM = NumberField("Distance", True, Unit.KM, 0, 250, 0.01)
TOTAL_TIME_IN_MIN = NumberField("Total time", True, Unit.MIN, 0, 360, 1)
ELEVATION_GAIN_IN_M = NumberField("Elevation", False, Unit.M, 0, 5000, 1)
DESCRIPTION = TextField("Description", False)

ACTIVITIES = {
    "swim": [
        DISTANCE_IN_KM,
        TOTAL_TIME_IN_MIN,
        DESCRIPTION,
    ],
    "run": [
        DISTANCE_IN_KM,
        TOTAL_TIME_IN_MIN,
        ELEVATION_GAIN_IN_M,
        DESCRIPTION,
    ],
    "bike": [
        DISTANCE_IN_KM,
        TOTAL_TIME_IN_MIN,
        ELEVATION_GAIN_IN_M,
        DESCRIPTION,
    ]
}
