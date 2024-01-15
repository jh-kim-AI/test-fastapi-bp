class UserService:
    @staticmethod
    async def register(*, obj: RegisterUser) -> None:
        async with async_db_session.begin() as db:
            username = await UserDao.get_by_username(db, obj.username)
            if username:
                raise errors.ForbiddenError(msg='Username already exists')
            email = await UserDao.check_email(db, obj.email)
            if email:
                raise errors.ForbiddenError(msg='Email already exists')
            await UserDao.create(db, obj)
