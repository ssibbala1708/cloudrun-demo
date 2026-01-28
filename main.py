from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from GitHub → GCP → Cloud Run 🚀"}
