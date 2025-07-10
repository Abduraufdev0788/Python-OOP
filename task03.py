class User:
    def __init__(self, username: str, email: str, is_active: bool):
        self.username = username
        self.email = email
        self.is_active = is_active

    def user_data(self):
        return f"sizning usernameingiz --- {self.username}\n" \
               f"sizning emailingiz --- {self.email}\n" \
               f"siz ayni paytda aktiv holatdasiz"

    def user_data_no_active(self):
        return f"sizning usernameingiz --- {self.username}\n" \
               f"sizning emailingiz --- {self.email}\n" \
               f"siz ayni paytda aktiv holatda emassiz"


user_data = User("@AbduraufNAsrullayev", "abduraufnasrullayev1210@gmail.com", 1023)

if user_data.is_active:
    print(user_data.user_data())
else:
    print(user_data.user_data_no_active())
