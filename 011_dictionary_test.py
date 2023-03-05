

def test_dictionaries():
    """Dictionaries (sometimes called 'dicts') store key-value pairs.
    You can create them using {} or the dict() function.
    Use [] to access the values in a dictionary."""
    value = None  # Replace this
    d = {"a": 10, "b": 20, "c": 30}
    assert value == d["b"]
    assert d == dict(a=10, b=value, c=30)
