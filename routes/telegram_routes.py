from fastapi import APIRouter

tg_router = APIRouter(
    prefix="/tg",
    tags=["Telegram"],
)


@tg_router.get("/test/")
async def test():
    return {"message": "Hello World"}
