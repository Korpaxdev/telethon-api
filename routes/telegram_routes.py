from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Query, Response

from depends.depends_types import post_client_type, query_client_type
from schemas.tg_schemas import LoginResponseSchema, CheckLoginResponseSchema, LogoutResponseSchema, \
    MessagesResponseSchema, SendMessageSchema, SendMessageResponseSchema
from services.tg_services import TgService
from utils.exceptions_utils import NotAuthorizedException

tg_router = APIRouter(
    prefix="/tg",
    tags=["Telegram", "API-V1"],
)


@tg_router.post("/login", response_model=LoginResponseSchema)
async def login(client: post_client_type):
    return {"qr_link_url": await client.generate_qr_url()}


@tg_router.post("/logout", response_model=LogoutResponseSchema)
async def logout(client: post_client_type):
    if not client.is_authorized():
        raise NotAuthorizedException
    return {"logout": await client.logout()}


@tg_router.get("/check/login", response_model=CheckLoginResponseSchema)
async def check_login(client: query_client_type):
    return {"status": await client.get_login_status()}


@tg_router.get("/messages", response_model=list[MessagesResponseSchema])
async def get_messages(client: query_client_type, uname: Annotated[str, Query(min_length=4)]):
    if not await client.is_authorized():
        raise NotAuthorizedException
    try:
        messages = await client.get_messages(uname)
        return messages
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Uname not found")


@tg_router.post("/messages", response_model=SendMessageResponseSchema)
async def post_message(data: SendMessageSchema, response: Response):
    async with TgService(data.from_phone) as client:
        if not await client.is_authorized():
            raise NotAuthorizedException
        try:
            await client.send_message(data.message_text, data.username)
            return {'status': 'ok'}
        except ValueError:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {'status': 'error'}
