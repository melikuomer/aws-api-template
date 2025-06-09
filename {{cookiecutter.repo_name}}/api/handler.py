from fastapi import FastAPI
import uvicorn
from .routes import api_router

import os

app = FastAPI()
app.include_router(api_router)
def handler(event, context):
  """Exporting handler here for aws rust web adapter to work"""
  config = uvicorn.Config("api.handler:app", host=os.environ.get("HOST", "0.0.0.0"), port=8080, log_level="info")
  server = uvicorn.Server(config)
  server.run()



if __name__ == "__main__":
  handler({},{})
