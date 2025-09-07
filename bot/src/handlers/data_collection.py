from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..core.locales import MessageKey, get_text
from ..core.models import UserState
from ..core.user_service import user_service
from ..core.api_service import api_service

data_collection_router = Router(name="data_collection")


@data_collection_router.message(F.text)
async def text_message_handler(message: Message, state: FSMContext) -> None:
    """Handle text messages for data collection."""
    user_id = message.from_user.id
    user = user_service.get_user(user_id)
    
    if not user:
        return
    
    text = message.text.strip()
    
    if user.state == UserState.EMAIL_INPUT:
        await handle_email_input(message, user, text)
    elif user.state == UserState.PASSWORD_INPUT:
        await handle_password_input(message, user, text)


async def handle_email_input(message: Message, user, email: str) -> None:
    """Handle email input."""
    if not user_service.is_valid_email(email):
        await message.answer(
            get_text(user.language, MessageKey.INVALID_EMAIL)
        )
        return
    
    # Save email and ask for password
    user_service.set_user_email(user.user_id, email)
    user_service.update_user_state(user.user_id, UserState.PASSWORD_INPUT)
    
    await message.answer(
        get_text(user.language, MessageKey.ENTER_PASSWORD)
    )


async def handle_password_input(message: Message, user, password: str) -> None:
    """Handle password input."""
    # Save password
    user_service.set_user_password(user.user_id, password)
    
    # Send data to API
    await message.answer(
        get_text(user.language, MessageKey.DATA_SENT)
    )
    
    try:
        success = await api_service.send_user_data(user)
        
        if success:
            await message.answer(
                get_text(user.language, MessageKey.EMAIL_SENT_SUCCESS)
            )
            user_service.update_user_state(user.user_id, UserState.COMPLETED)
        else:
            await message.answer(
                get_text(user.language, MessageKey.ERROR_OCCURRED)
            )
            
    except Exception as e:
        await message.answer(
            get_text(user.language, MessageKey.ERROR_OCCURRED)
        )
    
    # Clear sensitive data after sending
    user_service.clear_user_data(user.user_id)
