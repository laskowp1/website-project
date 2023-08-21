from abc import abstractmethod

from website_project.activity.description_fields.base import (
    HtmlField, Unit, HtmlType, PythonType, IS_REQUIRED_HTML_CLASS_NAME,
)


class NumberField(HtmlField):
    def __init__(self, name: str, required: bool, unit: Unit, min_val: int, max_val: int, step: float):
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
            f"class='{IS_REQUIRED_HTML_CLASS_NAME if not self.required else ''}'"
            f"{'required' if self.required else ''}"
            ">"
        )

    @property
    @abstractmethod
    def python_type(self) -> PythonType:
        pass


class IntegerField(NumberField):
    def __init__(self, name: str, required: bool, unit: Unit, min_val: int, max_val: int):
        HtmlField.__init__(self, name, HtmlType.NUMBER, required)
        self.min_val = min_val
        self.max_val = max_val
        self.step = 1
        self.unit = unit

    @property
    def python_type(self) -> PythonType:
        return int


class FloatField(NumberField):
    def __init__(self, name: str, required: bool, unit: Unit, min_val: int, max_val: int):
        HtmlField.__init__(self, name, HtmlType.NUMBER, required)
        self.min_val = min_val
        self.max_val = max_val
        self.step = 0.1
        self.unit = unit

    @property
    def python_type(self) -> PythonType:
        return float
