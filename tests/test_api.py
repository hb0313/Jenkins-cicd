from api.v1.routers import __version__


def test_api_version() -> None:
    assert __version__ == "0.1.0"
