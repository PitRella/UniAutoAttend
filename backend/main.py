import logging

from fastapi import APIRouter, FastAPI

from src.core.middleware import GlobalExceptionMiddleware
from src.user.routers import user_router

logger = logging.getLogger(__name__)


app = FastAPI(
    title='University Auto Attend',
)
app.add_middleware(GlobalExceptionMiddleware)

main_api_router = APIRouter(prefix='/api/v1')
main_api_router.include_router(user_router)

app.include_router(main_api_router)


