from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton('Понедельник')
button2 = KeyboardButton('Вторник')
button3 = KeyboardButton('Среда')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Воскресенье'))

button4 = KeyboardButton('Четверг')
button5 = KeyboardButton('Пятница')
button6 = KeyboardButton('Суббота')
markup5.row(button4, button5)
markup5.insert(button6)

