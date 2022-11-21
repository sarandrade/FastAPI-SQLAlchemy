from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import models
from ..views import schemas


def create(db: Session, request: schemas.Blog, user_id: int):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=user_id,
        published=request.published,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()

    return blogs


def get_by_id(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} was not found in the DataBase.",
        )

    return blog


def update(db: Session, request: schemas.Blog, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} was not found in the DataBase.",
        )

    blog.update(
        {models.Blog.title: request.title, models.Blog.body: request.body},
        synchronize_session=False,
    )
    db.commit()

    return {"message": f"Blog with id {id} updated."}


def delete(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} was not found in the DataBase.",
        )

    blog.delete(synchronize_session=False)
    db.commit()

    return {"message": f"Blog with id {id} deleted."}
