from fastapi import FastAPI
from routers import user, company, task, auth
import uvicorn

app = FastAPI()

app.include_router(user.router)
app.include_router(company.router)
app.include_router(task.router)
app.include_router(auth.router)

@app.get("/", tags=["Health Check"])
async def health_check():
    return "API Service is up and running!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)