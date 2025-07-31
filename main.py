from fastapi import FastAPI
from model import DocumentInsert
from elasticsearch import Elasticsearch
import time

app = FastAPI()

es = Elasticsearch("http://elasticsearch:9200")

@app.post("/insertDocument/")
async def create_item(document: DocumentInsert):
    doc = document.dict()
    doc["updated_by"] = int(time.time())
    response = es.index(index="req_res_index", document=doc)
    return {
        "result": response['result']
    }
