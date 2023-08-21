from typing import Optional

from website_project.activity.base import Activity
from website_project.activity.description_fields.base import Unit
from website_project.activity.description_fields import FloatField, IntegerField, TextField, DateField


DISTANCE_IN_KM = FloatField("distance", True, Unit.KM, 0, 300)
TOTAL_TIME_IN_MIN = IntegerField("total_time", True, Unit.MIN, 0, 720)
ELEVATION_GAIN_IN_M = IntegerField("elevation", False, Unit.M, 0, 3000)
DESCRIPTION = TextField("description", False)
DATE = DateField("date", True)


ACTIVITIES = (
    Activity("bike", (
        DATE,
        DISTANCE_IN_KM,
        TOTAL_TIME_IN_MIN,
        ELEVATION_GAIN_IN_M,
        DESCRIPTION
    )),
    Activity("run", (
        DATE,
        DISTANCE_IN_KM,
        TOTAL_TIME_IN_MIN,
        ELEVATION_GAIN_IN_M,
        DESCRIPTION,
    )),
    Activity("swim", (
        DATE,
        DISTANCE_IN_KM,
        TOTAL_TIME_IN_MIN,
        DESCRIPTION,
    ))
)


def get_activity(name: str) -> Optional[Activity]:
    for activity in ACTIVITIES:
        if activity.name == name:
            return activity
    return
