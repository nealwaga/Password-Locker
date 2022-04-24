class User:
    user_list = []

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

#saving user
    def save_user (self):

        User.user_list.append (self):

                