from db.db import UserInDB, get_user, update_password, UserOut, passUpdate, passOut

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
async def update_pass(name: passUpdate):
    user_in_db = get_user(name.nombre)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    update_password(user_in_db.nombre,user_in_db.password)
    pass_out = passOut(**user_in_db.dict())
    return pass_out