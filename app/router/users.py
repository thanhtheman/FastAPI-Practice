from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["user"])

@router.get("/register")
def get_posts ():
    return {"message": "this is to create a user"}