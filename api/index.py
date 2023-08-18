from fastapi import FastAPI

from api.utils import reload, use_route_names_as_operation_ids

app = FastAPI()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


use_route_names_as_operation_ids(app)
reload(app)
