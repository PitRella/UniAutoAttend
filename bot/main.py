import asyncio
import logging
import sys
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.core.settings import Settings
from src.handlers import start_router, data_collection_router, cancel_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# Load settings
settings = Settings.load()
TOKEN = settings.telegram_settings.API_TOKEN

if not TOKEN:
    logger.error("Telegram API token is not set! Please set TG_API_TOKEN environment variable.")
    sys.exit(1)


@asynccontextmanager
async def lifespan():
    """Application lifespan manager."""
    logger.info("Starting bot...")
    yield
    logger.info("Bot stopped.")


async def main() -> None:
    """Main function to run the bot."""
    # Initialize bot and dispatcher
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    # Use memory storage for FSM
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Include routers
    dp.include_router(start_router)
    dp.include_router(data_collection_router)
    dp.include_router(cancel_router)
    
    # Start polling
    try:
        async with lifespan():
            await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error during bot execution: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)