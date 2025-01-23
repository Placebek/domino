from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    access_token_expire_time: str