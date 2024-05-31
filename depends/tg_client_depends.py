from typing import Annotated

from fastapi import Query

from schemas.tg_schemas import LoginSchema
from services.tg_services import TgService
from utils.regexp_utils import PHONE_REGEXP_PATTERN


async def get_client_with_post(login_data: LoginSchema):
    async with TgService(login_data.phone) as client:
        yield client


async def get_client_with_query(phone: Annotated[str, Query(regex=PHONE_REGEXP_PATTERN, example="79999999999")]):
    async with TgService(phone) as client:
        yield client
