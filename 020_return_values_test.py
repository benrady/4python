
def test_return_values():
    """
    Functions can only return one value, but which value they return can be controlled with an if statement
    """

    def respond(greeting):
        if greeting == "hello":
            return "what?"  # replace this

        if len(greeting) > 10:
            return "what?"  # Also replace this

        return "what?"  # Also replace this

    assert "goodbye" == respond("hello")
    assert "I didn't understand" == respond("Do you like Python?")
    assert "what?" == respond("goodbye")
