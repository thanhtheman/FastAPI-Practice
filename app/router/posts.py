from fastapi import APIRouter

router = APIRouter(prefix="/posts", tags=["post"])

@router.get("/")
def get_posts ():
    return {"message": "this is to get all posts"}