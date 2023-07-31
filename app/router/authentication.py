from fastapi import APIRouter

router = APIRouter(prefix="/login", tags=["login"])

@router.get("/")
def get_posts ():
    return {"message": "this is to log in"}