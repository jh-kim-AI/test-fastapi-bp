from fastapi import APIRouter

from app.common.response_schema import response_base, ResponseModel
from app.schemas.user import RegisterUser

router = APIRouter()


@router.post('/register', summary='Register')
async def user_register(obj: RegisterUser) -> ResponseModel:
    await UserService.register(obj=obj)
    return await response_base.success()


@router.get('/{username}', summary='Get user info', dependencies=[DependsJwtAuth])
async def get_user(username: str) -> ResponseModel:
    current_user = await UserService.get_userinfo(username=username)
    data = GetAllUserInfo(**await select_as_dict(current_user))
    return await response_base.success(data=data)
