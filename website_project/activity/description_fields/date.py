from datetime import datetime, timedelta
from website_project.activity.description_fields.base import (
    HtmlField, HtmlType, PythonType, IS_REQUIRED_HTML_CLASS_NAME,
)


class DateField(HtmlField):
    def __init__(self, name: str, required: bool):
        HtmlField.__init__(self, name, HtmlType.DATE, required)
        self.max_val = datetime.now().date()
        self.min_val = self.max_val - timedelta(days=360)

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
            f"min='{self.min_val}'"
            f"max='{self.max_val}'"
            f"id='{self.name}'"
            f"name='{self.name}'"
            f"class='{IS_REQUIRED_HTML_CLASS_NAME if not self.required else ''}'"
            f"value='{self.default}'"
            f"{'required' if self.required else ''}"
            ">"
        )

    @property
    def python_type(self) -> PythonType:
        return str

    @property
    def default(self) -> datetime.date:
        return datetime.now().date()
