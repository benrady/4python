

def test_append():
    """The + operator can also be used to combine lists"""
    value = [1, 2, 3, 4]  # Replace this
    assert value == [1] + [2, 3, 4]
    assert value == [1, 2] + [3, 4]
