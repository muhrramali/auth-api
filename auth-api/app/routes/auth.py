from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel, EmailStr
from ..supabase_client import supabase
from ..dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

class Credentials(BaseModel):
    email: EmailStr
    password: str

@router.post("/signup", status_code=201)
def signup(data: Credentials):
    if not data.password:
        raise HTTPException(status_code=400, detail="Email and password are required")
    try:
        result = supabase.auth.sign_up({"email": data.email, "password": data.password})
        return {"user": result.user.model_dump() if result.user else None}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(data: Credentials):
    if not data.password:
        raise HTTPException(status_code=400, detail="Email and password are required")
    try:
        result = supabase.auth.sign_in_with_password(
            {"email": data.email, "password": data.password}
        )
        return {
            "access_token": result.session.access_token,
            "refresh_token": result.session.refresh_token,
            "token_type": "bearer"
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid login credentials")

@router.post("/logout", status_code=204, dependencies=[Depends(get_current_user)])
def logout():
    return Response(status_code=204)
