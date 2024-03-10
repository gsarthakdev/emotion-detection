from fastapi import FastAPI
from werkzeug.utils import secure_filename
from feat.detector import Detector
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI()

@app.get("/", tags=["Root"])
async def hello():
    return {"message": "Works"}
