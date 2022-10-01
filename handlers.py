from re import I
from aiogram import Dispatcher
import client
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(client.checkruzzianChar)
