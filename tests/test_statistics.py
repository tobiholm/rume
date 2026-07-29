from src.statistics import summary

def test_statistics():

    assert summary([1, 2])["total"] == 2
