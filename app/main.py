from fastapi import FastAPI
from app.schemas import user
from app.schemas.user import CreateUser
from app.services import user_service


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
    return user_service.create_user(user)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_service.get_user(user_id)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_service.delete_user(user_id)