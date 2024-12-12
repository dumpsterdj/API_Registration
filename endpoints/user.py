from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def user_dashboard():
    return {"message": "Welcome to the User Dashboard"}
