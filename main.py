# Creating Classes
#   class Car:

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "blaire")

# Creating Attributes in a Class
#   user_1.id = "001"
#   user_1.username = "blaire"

# Constructor - part of the blueprint that specifies what should happen during initialization
#   def __init__(self, seats):
#       self.seats = seats
#   my_car = Car(5)

user_2 = User("002", "jack")

# Adding Methods to a Class
#   def enter_race_mode(self):
#       self.seats = 2
#   my_car.enter_race_mode()

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
