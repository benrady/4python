

def test_keys_and_values():
    """You can use the keys() method to get a list-like-object of all the keys in a dictionary.
    Also works for values()"""
    keys = None  # Replace this
    d = {"a": 10, "b": 20, "c": 30}
    assert keys == list(d.keys())
    assert list(d.values())[2] == d[keys[2]]
