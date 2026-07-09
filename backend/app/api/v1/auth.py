from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)
from app.schemas.user import UserResponse
from app.services.auth_service import (
    register_user,
    login_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/health")
def auth_health():
    return {
        "message": "Authentication service is running."
    }


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db),
):
    created_user = register_user(db, user)

    if created_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    return created_user


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    user: LoginRequest,
    db: Session = Depends(get_db),
):
    token = login_user(
        db,
        user.email,
        user.password,
    )

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return token