from Database.repository import AbstractRepository
from Models.Users import SUserAdd


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_user(self, user: SUserAdd):
        user_dict = user.model_dump()
        if await self.users_repo.find_by_conditions({"login": user.login}) != []:
            return 0

        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def delete_user(self, id: int):
        res = await self.users_repo.delete_one(id)
        return res

    async def get_users(self):
        res = await self.users_repo.find_all()
        return res

    async def get_user(self, id: int):
        user = await self.users_repo.find_one(id)
        return user

    async def get_user_by_login(self, login: str):
        res = await self.users_repo.find_by_conditions({"login": login})
        if res != []:
            return res[0]
        return None