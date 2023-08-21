import logging
from flask import Flask, render_template, request, url_for, redirect
from flask_restful import Resource, Api
from typing import NewType, Tuple
from website_project.activity.description_fields.base import IS_REQUIRED_HTML_CLASS_NAME
from website_project.activity.activities import ACTIVITIES, get_activity
from website_project.database.engine import JSONFileEngine


app = Flask(__name__)
api = Api(app)

LOG = logging.getLogger(__name__)

API_PREFIX = "restapi"

HTML = NewType("html", str)
JSON = NewType("json", dict)

engine = JSONFileEngine("/home/users/laskowp1/PROJECTS/website-project/.db/_database.json")


def parse_response_form_data(form_data: JSON) -> Tuple[str, JSON]:
    activity = get_activity(form_data["name"])
    schema = activity.schema()

    valid_data = {}
    for field in schema:
        value = form_data.get(field.name)

        if field.required and value == "":
            raise Exception(f"Missing field `{field.name}` required by schema {schema}")

        valid_data[field.name] = field.default if value == "" else field.type(value)

    return activity.name, valid_data


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home_page() -> HTML:
    return render_template("welcome.html")


@app.route("/activity", methods=['GET', 'POST'])
def activity_form() -> HTML:
    if request.method == "POST":
        print(request.form.to_dict())
        activity, data = parse_response_form_data(request.form.to_dict())
        engine.insert(activity, data)
        print(f"{activity}:\n{data}")
        return redirect(url_for("activity_form"))
    if request.method == "GET":
        return render_template(
            "activity-form.html",
            activities=ACTIVITIES,
            hidden_marker="Div",
            is_required_class_name=IS_REQUIRED_HTML_CLASS_NAME,
        )

    raise Exception(f"Unsupported method `{request.method}`!")


class HealthResource(Resource):
    @staticmethod
    def get() -> JSON:
        return {"message": "ok"}


api.add_resource(
    HealthResource,
    f"/{API_PREFIX}/health",
    f"/{API_PREFIX}/",
)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
    )
