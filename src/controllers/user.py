from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..utils.hashing import Hash
from ..models import models
from ..views import schemas


def create(db: Session, request: schemas.User):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_by_id(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} was not found in the DataBase.",
        )

    return user
