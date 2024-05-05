from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import sqlite3
connection = sqlite3.connect("C:\\Users\\Artem\\PyCharm\\MyDataBase\\TouristBotStatistics_new.db")
cursor = connection.cursor()

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обновить данные"),
            KeyboardButton(text="Посмотреть статистику")
        ]
    ],
    resize_keyboard=True
)
back_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

inline_back_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="Назад")]]
)

common_back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_2584")]])

city_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Калининград", callback_data="klgd"),
            InlineKeyboardButton(text="Зеленоградск", callback_data="zel")
        ],
        [
            InlineKeyboardButton(text="Светлогорск", callback_data="sve"),
            InlineKeyboardButton(text="Янтарный", callback_data="yant")
        ],
        [
            InlineKeyboardButton(text="Полесск", callback_data="pol"),
            InlineKeyboardButton(text="Черняховск", callback_data="cher")
        ],
        [
            InlineKeyboardButton(text="Все города", callback_data="Все города"),
            InlineKeyboardButton(text="Назад", callback_data="Назад")
        ]
    ],
    resize_keyboard=True
)
type_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Культурный досуг", callback_data="kult"),
            InlineKeyboardButton(text="Развлечения", callback_data="ent")
        ],
        [
            InlineKeyboardButton(text="Питание", callback_data="food"),
            InlineKeyboardButton(text="Проживание", callback_data="liv"),
            InlineKeyboardButton(text="Прокат", callback_data="driv")
        ],
        [
            InlineKeyboardButton(text="СПА", callback_data="SPA"),
            InlineKeyboardButton(text="Сувениры", callback_data="suv")
        ],
        [
            InlineKeyboardButton(text="Туристические фирмы", callback_data="tur")
        ],
        [
            InlineKeyboardButton(text="Все типы", callback_data="Все типы"),
            InlineKeyboardButton(text="Назад", callback_data="Назад")
        ]
    ],
    resize_keyboard=True
)
stat_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оценка"),
            KeyboardButton(text="Посещаемость (топ 5)")
        ],
        [
            KeyboardButton(text="Самые непосещаемые (5)")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
change_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Название"),
            KeyboardButton(text="Адрес"),
            KeyboardButton(text="Описание")
        ],
        [
            KeyboardButton(text="Ссылка на сайт"),
            KeyboardButton(text="Скидка")
        ],
        [
            KeyboardButton(text="Город"),
            KeyboardButton(text="Тип"),
            KeyboardButton(text="Назад")
        ]
    ]
)

user_start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Напомнить, как работает карта", callback_data="card_work")],
        [InlineKeyboardButton(text="Узнать информацию о месте", callback_data="choose_city")],
        [InlineKeyboardButton(text="Оценить работу бота", callback_data="rating")]
    ]

)

rating_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1r"),
            InlineKeyboardButton(text="2", callback_data="2r"),
            InlineKeyboardButton(text="3", callback_data="3r"),
            InlineKeyboardButton(text="4", callback_data="4r"),
            InlineKeyboardButton(text="5", callback_data="5r")
        ]
    ]
)

def name_kb_create(citylist, typelist):
    cursor.execute('SELECT * FROM places')
    pls = cursor.fetchall()
    button_names = []
    for pl in pls:
        if (pl[7] in citylist) and (pl[8] in typelist):
            button_names.append([InlineKeyboardButton(text=pl[2], callback_data=str(pl[0]))])
    button_names.append([InlineKeyboardButton(text="Назад", callback_data="Назад")])
    return button_names

user_agree_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Прочитано", callback_data="agree")],
        [InlineKeyboardButton(text="Назад", callback_data="back_2584")]
                     ]
)

super_start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Администратор", callback_data="admin")],
        [InlineKeyboardButton(text="Пользователь", callback_data="user")]
    ]
)
