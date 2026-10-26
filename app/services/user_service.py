
from app.schemas.user import CreateUser


class UserService:
    def __init__(self):
        self.users: dict[int, dict] = {}
        self.next_user_id = 1

    def create_user(self, user_data: CreateUser) -> dict:
        user_id = self.next_user_id
        self.users[user_id] = user_data.dict()
        self.next_user_id += 1
        return {"id": user_id, **self.users[user_id]}

    def get_user(self, user_id: int) -> dict:
        return self.users.get(user_id, {"error": "User not found"})

    def delete_user(self, user_id: int) -> dict:
        if user_id in self.users:
            del self.users[user_id]
            return {"message": "User deleted successfully"}
        else:
            return {"error": "User not found"}

user_service = UserService()