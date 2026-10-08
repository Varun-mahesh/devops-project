from fastapi import FastAPI

app = FastAPI(title="PEP Cloud DevOps Project")


@app.get("/")
def home():
    return {
        "message": "PEP Cloud DevOps CI/CD Project is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }