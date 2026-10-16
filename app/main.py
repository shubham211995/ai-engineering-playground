from fastapi import FastAPI

app = FastAPI(title="AI Engineering Playground")


@app.get("/")
def root():
    return {"message": "My first FastAPI application is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}