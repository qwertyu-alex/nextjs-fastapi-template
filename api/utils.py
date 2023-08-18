import json
import os
from typing import Literal
from fastapi import FastAPI

from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


def reload(app: FastAPI):
    NODE_ENV: Literal["production", "development"] | None = os.getenv("NODE_ENV")  # type: ignore

    if not (NODE_ENV != None and NODE_ENV == "development"):
        return

    print("Reloading API")
    with open("openapi.json", "w") as f:
        json.dump(
            get_openapi(
                title=app.title,
                version=app.version,
                openapi_version=app.openapi_version,
                description=app.description,
                routes=app.routes,
            ),
            f,
        )

    os.system("node scripts/syncApi.mjs")
