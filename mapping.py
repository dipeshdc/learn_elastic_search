from elasticsearch import Elasticsearch

es = Elasticsearch("http://elasticsearch:9200")

mapping = {
  "mappings": {
    "properties": {
      "conversation_id": {
        "type": "keyword"
      },
      "sql": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "response_text": {
        "type": "text",
        "analyzer": "standard"
      },
      "rating": {
        "type": "float"
      }
    }
  }
}

if not es.indices.exists(index="req_res_index"):
    es.indices.create(index="req_res_index", body=mapping)
    print("Index created")
else:
    print("Index already exists")