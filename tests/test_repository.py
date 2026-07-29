from src.repository import load

def test_load():

    assert isinstance(
        load("data/configs/development.json"),
        dict
    )
