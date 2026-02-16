from fastapi import FastAPI

app = FastAPI(title="Reddit Moderator Governance Archive")

@app.get("/")
def health_check():
    return {"status": "RMGA running"}
