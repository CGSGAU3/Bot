from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
import keyboards as kb



bot = Bot("1654299247:AAHNGx7zD6m1NX20iFqydWFGaroHcEd-0gQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, дорогой друг! Здесь ты можешь узнать расписание "
                        "на любой день недели, просто выбери его в меню ниже:", reply_markup=kb.markup5)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Выбери пункт меню:", reply_markup=kb.markup5)

@dp.message_handler()
async def echo_message(msg: types.Message):
    if (msg.text == 'Понедельник'):
        await bot.send_message(msg.from_user.id, "1 - \n"
                                                 "2 - Английский язык\n"
                                                 "3 - Алгебра\n"
                                                 "4 - Алгебра\n"
                                                 "5 - Программирование\n"
                                                 "6 - Программирование\n"
                                                 "7 - Физика\n"
                                                 "8 - Физика")
    elif (msg.text == 'Вторник'):
        await bot.send_message(msg.from_user.id, "1 - Физкультура\n"
                                                 "2 - Геометрия\n"
                                                 "3 - Геометрия\n"
                                                 "4 - Геометрия\n"
                                                 "5 - Химия\n"
                                                 "6 - Химия")
    elif (msg.text == 'Среда'):
        await bot.send_message(msg.from_user.id, "1 - Русский язык\n"
                                                 "2 - Литература\n"
                                                 "3 - История\n"
                                                 "4 - История\n"
                                                 "5 - Физика\n"
                                                 "6 - Физика")
    elif (msg.text == 'Четверг'):
        await bot.send_message(msg.from_user.id, "1 - \n"
                                                 "2 - История\n"
                                                 "3 - Физкультура\n"
                                                 "4 - Физкультура\n"
                                                 "5 - География\n"
                                                 "6 - География\n"
                                                 "7 - Обществознание")
    elif (msg.text == 'Пятница'):
        await bot.send_message(msg.from_user.id, "1 - \n"
                                                 "2 - Биология\n"
                                                 "3 - Русский язык\n"
                                                 "4 - Литература\n"
                                                 "5 - Алгебра\n"
                                                 "6 - Алгебра\n"
                                                 "7 - Алгебра")
    elif (msg.text == 'Суббота'):
        await bot.send_message(msg.from_user.id, "1 - Алгебра\n"
                                                 "2 - Алгебра\n"
                                                 "3 - Литература\n"
                                                 "4 - Русский язык\n"
                                                 "5 - Биология\n"
                                                 "6 - Английский язык\n"
                                                 "7 - Английский язык")
    elif (msg.text == 'Воскресенье'):
        await bot.send_message(msg.from_user.id, "Что ты забыл в школе в воскресенье? Уйди оттуда!!!")
    else:
        await bot.send_message(msg.from_user.id, "Выбери день недели! Для подробной информации нажми /help")

if __name__ == '__main__':
    executor.start_polling(dp)