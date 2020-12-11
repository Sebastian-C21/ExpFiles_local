from db.user_db import get_usr_id
from pydantic import BaseModel

class UserIn(BaseModel):
    usr_id: str
    email: str

class UserOut(BaseModel):
    usr_in: str
    name: str