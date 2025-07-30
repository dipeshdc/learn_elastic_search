from fastapi import FastAPI
from model import DocumentInsert
from elasticsearch import Elasticsearch

app = FastAPI()

es = Elasticsearch("http://elasticsearch:9200")

@app.post("/insertDocument/")
async def create_item(document: DocumentInsert):
    response = es.index(index="req_res_index", document=doc)
    return {
        "result": response['result']
    }
