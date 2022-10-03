from mailbox import Message
from random import *
from aiogram import types
from main import bot
from googletrans import Translator
banned_symbols = set('ыъё',)
list_of_messages = ['Ти чо сука? на мові балакай підріла. Ще раз побачу таке, дупу порву', 'Ще раз таке напишеш, кікну звідси', 'Вийшов звідси розбійник', 'Sticker']
async def checkruzzianChar(message:types.Message):
    t = Translator().detect(text = str(message.text))

    if any((c in banned_symbols) for c in message.text.lower()):
        text = choice(list_of_messages)
        if text == 'Sticker':
            await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEF83hjNUoP6hxP_zwlAqdxahqOjdsnFgACfSQAAgrA-EiyDkpnFi2uqioE' )
            return
        else:
            await message.reply(text=text)
            return
    if (t.lang == 'ru'):
        print(t.lang)
        print(t.confidence)
        
        index = t.lang.index('ru')
        if isinstance(t.confidence, list):
            if (t.confidence[index] >= 0.81):
                text = choice(list_of_messages)
                if text == 'Sticker':
                    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEF83hjNUoP6hxP_zwlAqdxahqOjdsnFgACfSQAAgrA-EiyDkpnFi2uqioE' )
                else:
                    await message.reply(text=text)
        else:
            if(t.confidence >= 0.81):
                text = choice(list_of_messages)
                if text == 'Sticker':
                    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEF83hjNUoP6hxP_zwlAqdxahqOjdsnFgACfSQAAgrA-EiyDkpnFi2uqioE' )
                else:
                    await message.reply(text=text)
    else:
        print(t.lang)

       
            


