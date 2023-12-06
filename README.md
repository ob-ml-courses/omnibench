# Make an environment

```
conda create -n omnibench
conda activate omnibench
conda install python=3.9.10 pip -y
pip install -U outerbounds
```


# Embedding Server

```bash
uvicorn fast_api_server:app --port 8002 --reload
```

By default this will open a server wrapping on top of LanceDB.

Insert, search, and delete data using the following commands:

```python
import requests

requests.post("http://127.0.0.1:8002/add/",
              json={"items":
                        [{"text": "The cat is on the table",
                          "id": "1"},
                         {"text": "Hello world",
                          "id": "2"},
                         {"text": "The dog is not on the table",
                          "id": "3"}]})

requests.post("http://127.0.0.1:8002/search/",
              json={"text": "The cat is on the table"})

requests.post("http://127.0.0.1:8002/delete/",
              json={"ids": [1, 2, 3, 4] })
```

# Implemented DBs

These are found in the `omnibench/dbs` folder.

- [x] LanceDB
- [x] ChromaDB
- [x] Pinecone
- [x] Weaviate

# Configure Outerbounds platform access
Go [here](https://ui.dev-content.outerbounds.xyz/) and find your setup key!

# Run flows
```
python flow.py --environment=pypi run --with kubernetes
```