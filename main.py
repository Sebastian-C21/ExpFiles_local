from db.user_db import User, get_user
from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/user/leerUsuario/{username}")
async def get_data(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/updateUser/")
async def update_email(name: User):
    user_in_db = get_user(name.usr_id)
