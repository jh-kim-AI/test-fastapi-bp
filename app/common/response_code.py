from enum import Enum


class CustomCodeBase(Enum):

    @property
    def code(self):
        return self.value[0]

    @property    
    def msg(self):
        return self.value[1]


class CustomResponseCode(CustomCodeBase):
    HTTP_200 = (200,'Request successful')
    HTTP_400 = (400,'Request failed')


class CustomResponse:
    code: int
    msg: str
