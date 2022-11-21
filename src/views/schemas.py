from typing import Optional, List, Union
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

    class Config:
        orm_mode = True


class ResponseUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ResponseBlog(BaseModel):
    title: str
    body: str
    creator: ResponseUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
