from src.converter import to_json

def test_converter():

    assert "{" in to_json({})
