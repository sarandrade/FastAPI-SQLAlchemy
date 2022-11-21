from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..utils.oauth2 import get_current_user
from ..utils.database import get_db
from ..controllers import user
from ..views import schemas

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=schemas.ResponseUser)
def create_user(
    request: schemas.User,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return user.create(db, request)


@router.get("/{id}", response_model=schemas.ResponseUser)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return user.get_by_id(db, id)
