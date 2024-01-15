from app.schemas.base import SchemaBase


class Auth(SchemaBase):
    username: str
    password: str


class RegisterUser(Auth):
    nickname: str | None = None