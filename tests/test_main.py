from fastapi import testclient

import core.config as config
import main

settings = config.settings
client = testclient.TestClient(main.app)


def test_app() -> None:
    assert main.app.title == "Question Answer - RoBerta Base CUAD"
    assert main.app.version == settings.releaseId
