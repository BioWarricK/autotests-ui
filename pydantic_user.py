from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    


user_data = {
    "id": 1,
    "username": "Zara",
    "email": "zara.test@gmail.com"
}

user = User(**user_data)
print(user)
print(user.username)

invalid_user = {
    "id": "one",
    "username": "Zara",
    "email": "zara@zrmail.com"
}

invalid_user = User(**invalid_user)
print(invalid_user)