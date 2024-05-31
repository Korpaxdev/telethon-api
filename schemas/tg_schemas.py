from typing import Literal

from pydantic import BaseModel
from pydantic import Field

from utils.regexp_utils import PHONE_REGEXP_PATTERN


class LoginSchema(BaseModel):
    phone: str = Field(pattern=PHONE_REGEXP_PATTERN, examples=["79999999999"])


class LoginResponseSchema(BaseModel):
    qr_link_url: str | None


class CheckLoginResponseSchema(BaseModel):
    status: str


class LogoutResponseSchema(BaseModel):
    logout: bool


class MessagesResponseSchema(BaseModel):
    username: str
    message: str | None
    is_self: bool


class SendMessageSchema(BaseModel):
    message_text: str = Field(min_length=1)
    from_phone: str = Field(pattern=PHONE_REGEXP_PATTERN, examples=["79999999999"])
    username: str = Field(min_length=4)


class SendMessageResponseSchema(BaseModel):
    status: Literal["ok", "error"]
