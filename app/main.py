from fastapi import FastAPI
from .router import authentication, posts, likes, users

app = FastAPI()

app.include_router(authentication.router)
app.include_router(likes.router)
app.include_router(posts.router)
app.include_router(users.router)

@app.get("/")
def home ():
    return {"message": "This is home page my fren"}