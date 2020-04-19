class User():
    """Represent a simple user profile."""


    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()


    def descirbe_user(self):
        """Display a summary of the user's information."""

        print("\n" + self.first_name + " " + self.last_name)
        print(" Username: " + self.username)
        print(" Email: " + self.email)
        print(" Location: " + self.location)

    
    def greet_user(self):
        """Display a personalized greeting to the user."""

        print("\nWelcome back, " + self.username + "!")


eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.descirbe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com','alaska')
willie.descirbe_user()
willie.greet_user()