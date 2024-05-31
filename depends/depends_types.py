from typing import Annotated

from fastapi import Depends

from depends.tg_client_depends import get_client_with_post, get_client_with_query
from services.tg_services import TgService

post_client_type = Annotated[TgService, Depends(get_client_with_post)]
query_client_type = Annotated[TgService, Depends(get_client_with_query)]
