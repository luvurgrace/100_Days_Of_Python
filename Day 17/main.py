class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0 # кол-во подписчиков по дефолту будет равнятся 0 (можно не писать в параметрах)
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Nikita")
user_2 = User("002","Julia")

print(f"{user_2.username} followers = {user_2.followers}")
user_1.follow(user_2)
print(f"{user_2.username} followers = {user_2.followers}")