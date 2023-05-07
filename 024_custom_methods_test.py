
class UserProfile:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def full_name(self):
        return self.first_name + None  # Replace Me!


def test_classes():
    """
    In addition to attributes, custom objects can have methods just like the built-in ones.

    In Python, all methods have a special variable called "self" as the first parameter (just like in the constructor).
    This variable refers to the individual object instance.
    """

    profile = UserProfile("Bob", "Loblaw")
    assert "Bob Loblaw" == profile.full_name()
