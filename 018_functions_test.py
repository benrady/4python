
def add_numbers(argument_1, argument_2):
    """Functions are defined using the 'def' keyword, followed by the function name,
    followed by the argument names in parentheses"""
    return argument_1 + argument_2


def test_functions():
    """Functions are callable bits of code that take zero or more 'arguments' and can return a value."""
    value = None  # Replace this

    assert value == add_numbers(3, 1)
    assert 10 == add_numbers(6, value)
