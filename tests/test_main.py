from api.v1.routers import __version__


def test_app() -> None:
    assert __version__ == "0.1.0"
