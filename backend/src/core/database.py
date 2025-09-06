from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from src.core.settings import Settings

settings = Settings.load()


class Base(DeclarativeBase):
    """SQLAlchemy declarative base class.

    This class serves as the base class for all SQLAlchemy
    models in the application.
    It provides the basic functionality and configuration
    for model classes to interact
    with the database using SQLAlchemy's declarative mapping system.

    All database models should inherit from this class to ensure consistent
    behavior and proper database integration.
    """


engine = create_async_engine(
    settings.database_settings.database_url,
    echo=(settings.APP_MODE == 'dev'),  # Echo only in dev mode
)

async_db_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    """Provide an async database session generator.

    This dependency will create a new SQLAlchemy AsyncSession
    that can be used
    for database operations. The session is automatically
    closed when the request
    is finished.

    Yields:
        AsyncSession: A SQLAlchemy async database session.

    """
    session: AsyncSession = async_db_session()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
