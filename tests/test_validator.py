from src.validator import validate

def test_validate():

    assert validate({
        "name": "App",
        "version": "1.0"
    })
