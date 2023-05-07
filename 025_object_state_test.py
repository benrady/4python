
class UserProfile:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def rename(self, first_name):
        pass  # Replace me


def test_modifying_state():
    """
    Since each object that you create with a class is separate, modifying one object's state doesn't affect the other.
    """

    profile_one = UserProfile("Bob", "Loblaw")
    profile_two = UserProfile("Alice", "Loblaw")

    profile_two.rename("Andrew")
    assert "Bob" == profile_one.first_name
    assert "Andrew" == profile_two.first_name
