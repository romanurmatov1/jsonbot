from app import bot, dp
from config import admin_id
import json

from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
   await bot.send_message(chat_id=admin_id, text="<i>Salom Raxmatjon bot ishga tushdi</i>", parse_mode='HTML')
@dp.message_handler()
async def echo(message: Message):
   chat_id = message["from"]["id"]
   msjson = str(message)
   parsed = json.loads(msjson)
   text = json.dumps(parsed, indent=4, sort_keys=True)
   mtext = message.text
   if mtext == '/start':
      await bot.send_message(chat_id=chat_id, text="Iltimos bir nima deb yozing!")
   else:
      await bot.send_message(chat_id=chat_id, text=f"<pre>{text}</pre>", parse_mode='HTML')
   
   # await message.answer(text=text)
