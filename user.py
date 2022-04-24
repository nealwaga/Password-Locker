class User:
    user_list=[]
    def __init__(self,username,userpassword):
        self.username = username
        self.userpassword = userpassword
        # self.generated_password=generated_password 
        # saving user
    def save_user(self):
        
        User.user_list.append(self)
        
    def  login(self):
        if User in User.user_list:
            print(User)
            return User        