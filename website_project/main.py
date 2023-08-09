import logging
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from typing import NewType
from website_project.activity.base import ACTIVITIES

app = Flask(__name__)
api = Api(app)

LOG = logging.getLogger(__name__)

API_PREFIX = "restapi"

HTML = NewType("html", str)
JSON = NewType("json", dict)


@app.route("/", methods=['GET'])
def home_page() -> HTML:
    return render_template("welcome.html")


@app.route("/activity", methods=['GET', 'POST'])
def activity_form() -> HTML:
    if request.method == "POST":
        print(request.form)
        # activity = request.form.get("activity")
        # if activity not in activity_fields:
        #     return "Invalid activity selected."
        #
        # required_fields = activity_fields[activity]
        # form_data = {field: request.form.get(field) for field in required_fields}
        #
        # # Process the form_data and save it to the database or perform other actions

        return "Form data submitted successfully."
    if request.method == "GET":
        return render_template(
            "activity-form.html",
            activities=ACTIVITIES,
            hidden_marker="Div",
            form_marker="Form"
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
