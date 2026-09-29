# install fast api
# pip install "fastapi[all]"
# "fastapi dev" to start the dev server

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

client = FastAPI()

@client.get("/shipment")
def get_shipment():
  return {
    "item": "wooden_table",
    "shipment_id": "100"
  }

@client.get("/scalar", include_in_schema=False)
def get_scalar_docs():
  return get_scalar_api_reference(openapi_url=client.openapi_url,title="Scalar API")

# Start server command: fastapi dev
# FastAPI searches for package file structure from directories with __init__.py
# then it looks for module
# Since we have defined the default route handler so if you visit http://127.0.0.1:8000 you get page not found but since we have defined a route handler for /shipment so we can get the API response from it
# we will use the scalar documentation
# run this command: pip install scalar_fastapi
# but now you need to visit the following URL
# http://127.0.0.1:8000/scalar
# This will give you scalar like documentation
# but by default it also include /scalar api route which you may not want, so include the include_in_schema=False flag in the api route handler for scalar