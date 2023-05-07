
def test_string_methods():
    """
    Strings, integers, lists, and dictionaries, and pretty much everything else are all "objects" in Python. Objects are
    often used as a way to group variables and functions together, so that the functions always have access to the
    variables whenever they're called. When you attach functions to an object like this, they're called "methods".
    """

    a = "this is a string object"

    # Hint, you've seen this method before
    assert "THIS IS A STRING OBJECT" == a.replace_me()

    # Like functions, methods can take arguments. Hover for help!
    assert a.startswith("replace me")

    # Some methods return a new object of the same type
    assert "THIS IS ALSO A STRING OBJECT" == a.replace()
