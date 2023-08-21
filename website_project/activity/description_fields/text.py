from website_project.activity.description_fields.base import (
    HtmlField, HtmlType, PythonType, IS_REQUIRED_HTML_CLASS_NAME,
)


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
            f"class='{IS_REQUIRED_HTML_CLASS_NAME if self.required else ''}'"
            f"{'required' if self.required else ''}"
            ">"
        )

    @property
    def python_type(self) -> PythonType:
        return str
