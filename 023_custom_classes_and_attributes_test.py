
class UserProfile:
    def __init__(self, first, last):
        # Replace these
        # Any attributes you assign to "self" here will be available to the "profile" variable down below
        self.first_name = None
        self.last_name = None


def test_classes():
    """
    Classes are a way to make your own custom types of objects. These are similar to the built-in types of objects like
    integers, strings, and lists.

    One difference is that objects made from custom classes are created (also called "instantiated", since an object is
    an "instance" of a class) using a special method called a "constructor". Python constructors are kinda strange.
    They're always named __init__, and take a special parameter named "self".

    The "self" parameter is used to hold the variables that are attached to the object. These variables are called
    "attributes", and you can create attributes in Python simply by assigning variables in the constructor
    """

    # Each time you call the UserProfile constructor, you get a separate object
    alice_profile = UserProfile("Alice", "Loblaw")
    assert "Alice" == alice_profile.first_name
    assert "Loblaw" == alice_profile.last_name

    bob_profile = UserProfile("Bob", "Loblaw")
    assert "Bob" == bob_profile.first_name
    assert "Loblaw" == bob_profile.last_name

