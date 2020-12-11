from pydantic import BaseModel

class UserIn(BaseModel):
    usr_id: str
    email: str

class UserOut(BaseModel):
    usr_id: str
    name: str