from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    # refresh_token: str
