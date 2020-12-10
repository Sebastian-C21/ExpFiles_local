from typing import Dict
from pydantic import BaseModel
from pydantic.errors import EmailError
from pprint import pprint

class UserInDB(BaseModel): #así se hace la herencia le python
    username: str
    password: str
    nombre: str
    apellido: str
    correo: str
    celular: int
    rol: str
 
class UserOut(BaseModel):
    nombre: str
    apellido: str
    correo: str

class passUpdate(BaseModel):
    nombre: str
    password: str

class passOut(BaseModel):
    password: str

database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "nombre":"Camilo",
                            "apellido":"Perez",
                            "correo":"camper@gmail.com",
                            "celular":3146785643,
                            "rol":"admin"}),
    "esteban15": UserInDB(**{"username":"esteban15",
                            "password":"root1",
                            "nombre":"Esteban",
                            "apellido":"Perez",
                            "correo":"esteper@gmail.com",
                            "celular":3146975643,
                            "rol":"guest"}),
    "Jaime12": UserInDB(**{"username":"Jaime12",
                           "password":"Jaime123",
                           "nombre":"Jaime",
                           "apellido":"Hernandez",
                           "correo":"jaime123@hotmail.com",
                           "celular":3102582585,
                           "rol":"admin"}),
    "Julio987":UserInDB(**{"username":"Julio987",
                           "password":"Julio987",
                           "nombre":"Julio",
                           "apellido":"Comesaña",
                           "correo":"julio.comesana@gmail.com",
                           "celular":3109876543,
                           "rol":"user"}),
    "Hernan.Perez":UserInDB(**{"username":"Hernan.Perez", 
                               "password":"Pereceras",
                               "nombre":"Hernan",
                               "apellido":"Perez",
                               "correo":"hernan.perez@hotmail.com",
                               "celular":3009877845,
                               "rol":"guest"}),
    "FreeLunch":UserInDB(**{"username":"FreeLunch",
                            "password":"987654321",
                            "nombre":"Duvan",
                            "apellido":"Camelo",
                            "correo":"Duvan@yahoo.es",
                            "celular":3153698754,
                            "rol":"user"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_password(name: str, contra: str):
    database_users[name].password = contra
    return contra

def create_user(new_user: UserInDB):
    if new_user in database_users.keys():
        return "El usuario ya existe"
    else:
        database_users[new_user].username = new_user

def login(name: str, contra: str):
    for i,j in database_users.items():
        #print(i, j.password)
        if name == i and contra == j.password:
            print("Match")