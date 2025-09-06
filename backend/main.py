import logging

from fastapi import APIRouter, FastAPI

from src.core.middleware import GlobalExceptionMiddleware

logger = logging.getLogger(__name__)


app = FastAPI(
    title='University Auto Attend',
)
app.add_middleware(GlobalExceptionMiddleware)

main_api_router = APIRouter(prefix='/api/v1')

app.include_router(main_api_router)


