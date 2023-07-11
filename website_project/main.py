import logging
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from typing import NewType

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
    if request.method == 'GET':
        return render_template("activity-form.html")
    print('POST REQUEST')



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
