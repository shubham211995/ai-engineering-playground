from fastapi import FastAPI
from app.schemas.user import CreateUser


app = FastAPI(title="AI Engineering Playground")

users: dict[int, dict] = {}
next_user_id = 1

@app.get("/")
def root():
    return {"message": "My first FastAPI application is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/users", status_code=201)
def create_user(user: CreateUser):
    global next_user_id
    user_id = next_user_id
    newuser={
        "id": user_id,
        **user.model_dump()
    }
    users[user_id] = newuser
    next_user_id += 1
    return newuser

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)
    if user is None:
        return {"error": "User not found"}
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users:
        del users[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"error": "User not found"}