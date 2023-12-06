"""
This file contains the FastAPI server that will be used to add and search documents.
By default, it will wrap the LanceDB database, but you can swap it out for any other database.

To run this server, run the following command:
uvicorn fast_api_server:app --reload --port 8002
(reload can be removed)
"""

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from embedders.embedders import SentenceTransformerEmbedder
from dbs.lancedb import LanceDB

class Documents(BaseModel):
    text: str
    id: str
class Query(BaseModel):
    text: str

class ListOfIds(BaseModel):
    ids: List[int]

class DocumentList(BaseModel):
    items: List[Documents]


app = FastAPI()
encoder = SentenceTransformerEmbedder("paraphrase-MiniLM-L6-v2", device="cpu")
db = LanceDB()


@app.post("/add/")
def add(item: DocumentList):
    ids = [i.id for i in item.items]
    docs = [i.text for i in item.items]

    embeddings = encoder.embed(docs)
    db.add(ids, embeddings, [{"text": d} for d in docs])
    return item


@app.post("/search/")
def search(query: Query):
    text = query.text
    embeddings = encoder.embed([text])[0]
    result = db.vector_search(embeddings, k=1)
    print(result)

@app.post("/delete/")
def delete(list_of_ids: ListOfIds):
    ids = list_of_ids.ids
    result = db.delete(ids)
    print(result)




