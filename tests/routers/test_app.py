import json

from fastapi import testclient

import core.config as config
import main

settings = config.settings
client = testclient.TestClient(main.app)


def test_qa_prediction() -> None:
    question = {
        "question": "Where do I live?",
        "context": "My name is Harshad. I live in New York.",
    }
    response = client.post("/predict/qa", json.dumps(question))
    assert response.status_code == 200
