from fastapi import testclient

import core
import main

#client = testclient.TestClient(main.app)


def test_application_code() -> None:
    assert main.app.title == "Image Classification - Vissl (RegnetY-60)"
    assert main.app.version == core.settings.releaseId
