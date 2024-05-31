from fastapi import FastAPI

from routes.telegram_routes import tg_router
from utils.constants_utils import API_V1_PREFIX
from utils.env_utils import ENV_SETTINGS

app = FastAPI(title="Telethon FastAPI", debug=ENV_SETTINGS.DEBUG)

v1_routes = (tg_router,)

for router in v1_routes:
    app.include_router(router, prefix=API_V1_PREFIX)
