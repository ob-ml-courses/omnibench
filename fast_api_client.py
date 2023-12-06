"""
Very simple set of examples to show how to use the client.
"""

if __name__ == "__main__":
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
