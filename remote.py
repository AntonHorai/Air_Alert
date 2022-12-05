from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
import dosomething

API_TOKEN = '...' # Telegram bot token
users = ['...','...'] #Telegram @userinfobot to see an ID
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
#interface
@dp.message_handler(filters.IDFilter(user_id=users), commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="/Тривога!"),
           types.KeyboardButton(text="/Відбій"),
           types.KeyboardButton(text="/Сирена_ON"),
           types.KeyboardButton(text="/Сирена_OFF"),
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard = True)
   await message.reply("Вітаю!\nЦе бот для керування системою оповіщення.\nБудьте уважні.", reply_markup=keyboard)
#just for ping
@dp.message_handler(filters.IDFilter(user_id=users), commands=['ping'])
async def send_welcome(message: types.Message):
   await message.reply("pong")

#actions
@dp.message_handler(commands=['Тривога!'])
async def dosome(arg):
   print('Alert_START')
   dosomething.action(1)
@dp.message_handler(commands=['Відбій'])
async def dosome(arg):
   print('Alert_STOP')
   dosomething.action(2)
@dp.message_handler(commands=['Сирена_ON'])
async def dosome(arg):
   print('Siren_ON')
   dosomething.action(3)
@dp.message_handler(commands=['Сирена_OFF'])
async def dosome(arg):
   print('Siren_OFF')
   dosomething.action(4)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
