from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from app.common.response_code import CustomResponse, CustomResponseCode
from app.core.conf import settings


class ResponseModel(BaseModel):
    model_config = ConfigDict(json_encoders={datetime: lambda x: x.strftime(settings.DATETIME_FORMAT)})

    code: int = CustomResponseCode.HTTP_200.code
    msg: str = CustomResponseCode.HTTP_200.msg
    data: Any | None = None


class ResponseBase:

    @staticmethod
    async def _response(*, res: CustomResponseCode | CustomResponse = None, data: Any | None = None) -> ResponseModel:
        return ResponseModel(code=res.code, msg=res.msg, data=data)

    async def success(
        self,
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_200,
        data: Any | None = None,
    ) -> ResponseModel:
        return await self._response(res=res, data=data)
    
    async def fail(
        self,
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_400,
        data: Any | None = None,
    ) -> ResponseModel:
        return await self._response(res=res, data=data)
    

response_base = ResponseBase()
