from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class S3UriModel(BaseModel):
    s3_uri: str

@app.get("/")
def read_root():
    return {"message": "Hello, Try-On Anything!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/receive_s3_uri/")
async def receive_s3_uri(uri: S3UriModel):
    # Your logic to handle the S3 URI goes here
    return {"received_uri": uri.s3_uri}
