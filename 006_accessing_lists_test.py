

def test_accessing_list():
    """The [] operator can be used to create list, but also access the values in them.
    Like most programming languages, we start counting at 0"""
    value = None  # Replace this
    simple_list = [1, 2, 3, 4]
    assert value == simple_list[2]
    assert 4 == simple_list[value]
