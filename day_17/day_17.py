# Classes


# social media account
class User:
    def __init__(self, user_id, username):
        print("new user is being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Anup")
print(user_1.id + " --> " + user_1.username)

user_2 = User("002", "Jack")
print(user_2.id + " --> " + user_2.username)


user_1.follow(user_2)
print("followers: ", user_1.followers)
print("following: ", user_1.following)
print("followers: ", user_2.followers)
print("following: ", user_2.following)
