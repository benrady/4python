
def test_list_methods():
    a = [1, 1, 2, 3]
    assert 2 == a.count(0)  # Replace me, hover for help!

    # Some methods change an existing object, instead of returning a new one
    a.insert(2, 1)
    assert a == []  # Replace me
