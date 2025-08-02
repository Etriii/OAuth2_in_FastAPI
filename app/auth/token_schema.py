from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    username: str | None = None

class RoleAndPermissions(BaseModel):
    role: str
    company_id: int
    permissions: list
    

class PermissionToken(BaseModel):
    permission_token: str
    token_type: str
    