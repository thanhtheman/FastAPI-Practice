from fastapi import APIRouter

router = APIRouter(prefix="/likes", tags=["like"])

@router.get("/")
def get_posts ():
    return {"message": "this is to like a post"}