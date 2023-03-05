

def test_combine_dicts():
    """You can add the contents of one dictionary to the other using the update() method"""
    dict1 = {"a": 10, "b": 20}
    dict2 = {"b": 21, "c": 30}
    dict1.update(dict2)
    value = None  # Replace this
    assert value == dict1
