from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Engineering Playground")

class CreateUser(BaseModel):
    username: str
    email: str
@app.get("/")
def root():
    return {"message": "My first FastAPI application is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/users")
def create_user(user: CreateUser):
    return {"message": f"User {user.username} with email {user.email} created successfully!"}