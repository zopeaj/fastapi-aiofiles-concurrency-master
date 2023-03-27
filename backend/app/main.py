import os
import sys
from dotenv import load_dotenv

from fastapi import FastAPI
from typing import Dict
import json
import asyncio
import aiofiles

app = FastAPI()

@app.get("/hello")
def data() -> Dict[str, str]:
    return {"hello": "data"}

@app.get("/get-name-file-data")
def getNameFromJsonFile():
    datavalue = { }
    with open('articuno.json', mode='r') as f:
        contents = f.read()
        datas = json.loads(contents)
        datavalue.update({"name": datas["name"]})
    return datavalue

@app.get("/get-file-data")
def getFileData():
    with open('articuno.json', mode='r') as f:
        contents = f.read()
        datas = json.loads(contents)
    return datas

@app.get("/ge-file-response-data")
async def getFileResponseData():
    async with aiofiles.open("articuno.json", mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    return data


