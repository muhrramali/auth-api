from fastapi import Header, HTTPException
from .supabase_client import supabase

async def get_current_user(authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Access token required")

    token = authorization[7:].strip()
    if not token:
        raise HTTPException(status_code=401, detail="Access token required")

    try:
        result = supabase.auth.get_user(token)
        user = result.user
        if not user:
            raise Exception("No user")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
