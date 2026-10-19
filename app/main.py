from fastapi import FastAPI

app = FastAPI(title="AI Engineering Playground")


@app.get("/")
def root():
    return {"message": "My first FastAPI application is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}