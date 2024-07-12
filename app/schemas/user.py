from pydantic import BaseModel
from pydantic import EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    password: str
