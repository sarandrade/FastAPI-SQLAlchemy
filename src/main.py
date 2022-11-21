from fastapi import FastAPI

from .routers import user, blog, auth
from .utils.database import engine
from .models import models


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(blog.router)
