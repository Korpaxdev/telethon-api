from telethon import TelegramClient
from telethon.types import Message

from utils.constants_utils import SESSIONS_PATH, Status
from utils.env_utils import ENV_SETTINGS


class TgService:
    __client: TelegramClient

    def __init__(self, session_name: str):
        SESSIONS_PATH.mkdir(parents=True, exist_ok=True)
        self.__client = TelegramClient(SESSIONS_PATH / session_name, ENV_SETTINGS.API_ID, ENV_SETTINGS.API_HASH)

    async def __aenter__(self):
        await self.__client.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__client.disconnect()

    async def generate_qr_url(self):
        return (await self.__client.qr_login()).url

    async def get_login_status(self):
        return Status.logged if await self.is_authorized() else Status.waiting_qr_login

    async def logout(self):
        return await self.__client.log_out()

    async def is_authorized(self):
        return await self.__client.is_user_authorized()

    async def get_messages(self, entity_name: str):
        entity = await self.__client.get_entity(entity_name)
        return [await self.__convert_message(message) for message in await self.__client.get_messages(entity, limit=50)]

    async def send_message(self, message: str, entity_name: str):
        entity = await self.__client.get_entity(entity_name)
        await self.__client.send_message(entity, message)

    async def __convert_message(self, message_object: Message):
        converted_data = dict()
        converted_data['username'] = message_object.sender.username
        converted_data['message'] = message_object.message
        converted_data['is_self'] = message_object.sender.id == (await self.__client.get_me()).id
        return converted_data
