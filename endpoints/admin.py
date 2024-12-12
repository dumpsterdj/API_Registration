from fastapi import APIRouter

router = APIRouter()

@router.get("/admin")
def admin_dashboard():
    return {"message": "Welcome to the Admin Dashboard"}
