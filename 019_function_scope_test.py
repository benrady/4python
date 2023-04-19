def add_two(value):  # Move this somewhere
    return add_one(add_one(value))


def test_function_scope():
    """Like all variables, functions have a 'scope' which controls where they can be used. Functions declared outside
    the current scope can't be used."""
    def add_one(value):
        return value + 1

    assert 5 == add_two(3)