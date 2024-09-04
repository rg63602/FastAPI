from click import clear
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

uri = "mongodb+srv://rishabh-mongo-db:2gJr6C5lIX2DI6rG@fastapi-mongodb.3cago.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi(version="1", strict=True, deprecation_errors=True), tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    data = client.fastapi.item.find()
    for row in data:
        print(row)
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
