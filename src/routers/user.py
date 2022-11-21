from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..utils.database import get_db
from ..controllers import user
from ..views import schemas

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=schemas.ResponseUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db, request)


@router.get("/{id}", response_model=schemas.ResponseUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_by_id(db, id)
