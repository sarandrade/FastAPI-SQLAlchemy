from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ..utils.oauth2 import get_current_user
from ..utils.database import get_db
from ..controllers import blog
from ..views import schemas

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get("/", response_model=List[schemas.ResponseBlog])
def get_blogs(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.get_all(db)


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseBlog
)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return blog.get_by_id(db, id)


@router.post("/{user_id}", status_code=status.HTTP_201_CREATED)
def create_blog(user_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(db, request, user_id)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(db, request, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete(db, id)
