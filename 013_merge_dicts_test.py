

def test_combine_dicts():
    """You can combine two dictionaries without changing them using the ** operator"""
    dict2 = {"b": 20, "c": 30}
    value = None  # Replace this
    assert {"a": 10, "b": 20, "c": 30} == {**value, **dict2}
