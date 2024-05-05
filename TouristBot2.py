#-----------------------------------------------imports--------------------------------------
from aiogram import types, Router, F, Bot, Dispatcher
from aiogram.filters import CommandStart, or_f, and_f
from aiogram.types import InlineKeyboardMarkup, FSInputFile, InputMediaPhoto

import asyncio
from datetime import datetime

from view_statistics import *
from keyboards import *
from config import *
from MyDataBase.ChangeData import *

#---------------------------------------------datadbase connect------------------------------------------------
import sqlite3
connection = sqlite3.connect("C:\\Users\\Artem\\PyCharm\\MyDataBase\\TouristBotStatistics_new.db")
cursor = connection.cursor()
from MyDataBase.ChangeData import count_ariph_mean_rating, AntyCityCode

#----------------------------------------------bot and routers begin-------------------------------------------
bot = Bot(token=TOKEN)

admin_router = Router()
user_router = Router()
common_router = Router()

dp = Dispatcher()
dp.include_router(common_router)

#----------------------------------------------main------------------------------------------------------------
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

#----------------------------------------------photos for statistics-------------------------------------------
Myphoto = types.FSInputFile(
            path='visit_diagram.png'
        )

#------------------------------------------------other parameters----------------------------------------------
change_citylist = []
change_typelist = []
user_citylist = []
user_typelist = []
ID = -1
mode = "fgh"
back_mode = 0
dt = datetime.now()
visit_flag = [dt.toordinal()]*42
flag = [True]*42

#=============================================================================================================#
#===================================================COMMON ROUTER=============================================#

#--------------------------------------------------/start handler----------------------------------------------
@common_router.message(CommandStart())
async def StartCmd(message: types.Message):
    await message.answer_photo(FSInputFile(path='img\\DefaultPhoto.jpg'), 'Выберете роль', reply_markup=super_start_kb)

@common_router.callback_query(F.data == "admin")
async def StartAdmin(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption="Введите пароль", reply_markup=common_back_kb)

@common_router.message(F.text == ADMIN_PASSWORD)
async def StartAdmWork(message: types.Message):
    await message.answer(text="Правильный пароль! Вы вошли как админ.", reply_markup=start_kb)
    dp.include_router(admin_router)

@common_router.callback_query(F.data == "back_2584")
async def CommonBack(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption='Выберете роль', reply_markup=super_start_kb)

@common_router.callback_query(F.data == "user")
async def StartUser(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=AgreeText, reply_markup=user_agree_kb)

@common_router.callback_query(F.data == "agree")
async def StartUsWork(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=DefaultText, reply_markup=user_start_kb)
    dp.include_router(user_router)

#=============================================================================================================#
#==================================================ADMIN ROUTER===============================================#


#----------------------------------------------data change handlers block--------------------------------------
@admin_router.message(F.text == "Обновить данные")
async def update_data(message: types.Message):
    await message.answer(text="Что именно вы хотите изменить? Выберете город.", reply_markup=city_kb)
#city choose
@admin_router.callback_query(F.data == "klgd")
@admin_router.callback_query(F.data == "zel")
@admin_router.callback_query(F.data == "sve")
@admin_router.callback_query(F.data == "pol")
@admin_router.callback_query(F.data == "yant")
@admin_router.callback_query(F.data == "cher")
@admin_router.callback_query(F.data == "Все города")
async def update_data_city(callback: types.CallbackQuery):
    global change_citylist
    txt = callback.data
    if txt == "Все города":
        change_citylist.append("klgd")
        change_citylist.append("zel")
        change_citylist.append("cher")
        change_citylist.append("yant")
        change_citylist.append("pol")
        change_citylist.append("sve")
    else:
        change_citylist.append(txt)
    await callback.message.answer(text="Что именно вы хотите изменить? Выберете тип.", reply_markup=type_kb)
#type choose and create inline keyboard of places
@admin_router.callback_query(F.data == "kult")
@admin_router.callback_query(F.data == "ent")
@admin_router.callback_query(F.data == "food")
@admin_router.callback_query(F.data == "liv")
@admin_router.callback_query(F.data == "driv")
@admin_router.callback_query(F.data == "SPA")
@admin_router.callback_query(F.data == "suv")
@admin_router.callback_query(F.data == "tur")
@admin_router.callback_query(F.data == "Все типы")
async def update_data_type(callback: types.CallbackQuery):
    global change_typelist, change_citylist
    if callback.data == "Все типы":
        change_typelist.append("kult")
        change_typelist.append("ent")
        change_typelist.append("food")
        change_typelist.append("liv")
        change_typelist.append("driv")
        change_typelist.append("SPA")
        change_typelist.append("suv")
        change_typelist.append("tur")
    else:
        change_typelist.append(callback.data)
    if len(name_kb_create(change_citylist, change_typelist)) > 1:
        await callback.message.answer(text="Выберете место", reply_markup=InlineKeyboardMarkup(inline_keyboard=name_kb_create(change_citylist, change_typelist)))
    else:
        await callback.message.answer(text="Подходящих объектов не найдено", reply_markup=back_kb)
    change_typelist = []
    change_citylist = []
#callbacks for change data
@admin_router.callback_query(F.data < '@')
async def change_data(callback: types.CallbackQuery):
    global ID
    ID = int(callback.data)
    cursor.execute('SELECT Name, Address, desc, link, sale, Pic FROM places WHERE id = ?', (ID, ))
    Loc = cursor.fetchone()
    plc_txt = f"{Loc[0]} - это {Loc[2]}\n Находится по адресу: {Loc[1]}. \n " \
                  f"Ссылка на официальный сайт: {Loc[3]}. \n Скидка - {Loc[4]}%!"
    await bot.send_photo(chat_id=callback.message.chat.id, photo=Loc[5])
    await callback.message.answer(text=plc_txt)
    await callback.message.answer(text="Что именно вы хотите изменить?", reply_markup=change_kb)

#----------------------------------------specific data change handlers block-----------------------------------
#Название
@admin_router.message(F.text == "Название")
async def change_data_name(message: types.Message):
    global mode
    await message.answer(text="Введите новое название")
    mode = "newname"

#Адрес
@admin_router.message(F.text == "Адрес")
async def change_data_address(message: types.Message):
    global mode
    await message.answer(text="Введите новый адрес - сначала напишите город, потом запятую, потом оставшийся адрес")
    mode = "newaddress"

#Описание
@admin_router.message(F.text == "Описание")
async def change_data_desc(message: types.Message):
    global mode
    await message.answer(text="Введите новое описание")
    mode = "newdesc"

#Ссылка
@admin_router.message(F.text == "Ссылка на сайт")
async def change_data_link(message: types.Message):
    global mode
    await message.answer(text="Введите новую ссылку")
    mode = "newlink"

#Скидка (целочисленная)
@admin_router.message(F.text == "Скидка")
async def change_data_sale(message: types.Message):
    global mode
    await message.answer(text="Введите новую скидку")
    mode = "newsale"

#Город
@admin_router.message(F.text == "Город")
async def change_data_city(message: types.Message):
    global mode
    await message.answer(text="Введите новый город", reply_markup=city_kb)
    mode = "newcity"

#Тип
@admin_router.message(F.text == "Тип")
async def change_data_type(message: types.Message):
    global mode
    await message.answer(text="Введите новый тип", reply_markup=type_kb)
    mode = "newtype"

#-----------------------------------------------statistics view handlers block---------------------------------
@admin_router.message(F.text == "Посмотреть статистику")
async def watch_stat(message: types.Message):
    await message.answer(text="Что именно вы хотите посмотреть?", reply_markup=stat_kb)
#visiting (top 10)
@admin_router.message(F.text == "Посещаемость (топ 5)")
async def watch_visit(message: types.Message):
    ShowTopVisiting()
    await bot.send_photo(chat_id = message.chat.id, photo=Myphoto)
#visiting (bottom 5)
@admin_router.message(F.text == "Самые непосещаемые (5)")
async def watch_bvisit(message: types.Message):
    ShowAntyTopVisiting()
    await bot.send_photo(chat_id=message.chat.id, photo=Myphoto)
#rating
@admin_router.message(F.text == "Оценка")
async def watch_mark(message: types.Message):
    ShowRating()
    await bot.send_photo(chat_id=message.chat.id, photo=Myphoto)

#--------------------------------------------back handlers------------------------------------------------------
@admin_router.message(F.text == "Назад")
async def back(message: types.Message):
    global ID
    ID = -1
    await message.answer(text="Back", reply_markup=start_kb)

@admin_router.callback_query(F.data == "Назад")
async def cback(callback: types.CallbackQuery):
    global ID
    ID = -1
    await callback.message.answer(text='Back', reply_markup=start_kb)

#Принимаем новые данные (для specific data change handlers block)
@admin_router.message(F.text)
async def change_data_end(message: types.Message):
    global mode
    if mode == "newname":
        change_name(ID, message.text)
        await message.answer(text="Название успешно изменено")
    if mode == "newaddress":
        change_address(ID, message.text)
        await message.answer(text="Адрес успешно изменён")
    if mode == "newdesc":
        change_desc(ID, message.text)
        await message.answer(text="Описание успешно изменено")
    if mode == "newlink":
        change_link(ID, message.text)
        await message.answer(text="Ссылка успешно изменена")
    if mode == "newsale":
        try:
            change_sale(ID, int(message.text.replace(" ", "").replace("%", "")))
            await message.answer(text="Скидка успешно изменена")
            mode = "fgh"
        except ValueError:
            await message.answer(text="Некорректная скидка")
    if mode == "newcity":
        change_city(ID, AntyCityCode(message.text))
        await message.answer(text="Город успешно изменён", reply_markup=change_kb)
    if mode == "newtype":
        change_type(ID, AntyTypeCode(message.text))
        await message.answer(text="Тип успешно изменён", reply_markup=change_kb)
    if mode != "newsale":
        mode = "fgh"

#=============================================================================================================#
#===================================================USER ROUTER===============================================#


#-----------------------------------------------------user handlers--------------------------------------------
@user_router.callback_query(F.data == "card_work")
async def remember(callback: types.CallbackQuery):
    global back_mode
    await callback.answer()
    await callback.message.edit_caption(caption=CardWork, reply_markup=inline_back_kb)
    back_mode = 0

@user_router.callback_query(F.data == "Назад")
async def bck(callback: types.CallbackQuery):
    global ID, back_mode, user_citylist, user_typelist
    ID = -1
    await callback.answer()
    if back_mode == 0:
        await callback.message.edit_caption(caption=DefaultText, reply_markup=user_start_kb)
    elif back_mode == 1:
        await callback.message.edit_caption(caption="Выберете город", reply_markup=city_kb)
        user_citylist = []
    elif back_mode == 2:
        await callback.message.edit_caption(caption="Выберете тип.", reply_markup=type_kb)
        user_typelist = []
    elif back_mode == 3:
        await callback.message.edit_media(media=InputMediaPhoto(type='photo', media=default_photo))
        await callback.message.edit_caption(caption="Выберете место", reply_markup=InlineKeyboardMarkup(inline_keyboard=name_kb_create(user_citylist, user_typelist)))
    back_mode -= 1

@user_router.callback_query(F.data == "rating")
async def Rating(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption="Оцените бот от 1 до 5:", reply_markup=rating_kb)

@user_router.callback_query(or_f(F.data == "1r", F.data == "2r", F.data == "3r", F.data == "4r", F.data == "5r"))
async def Rtng(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption="Успешно оценино")
    await asyncio.sleep(0.8)
    txt = callback.data
    add_rating(int(txt.replace("r", "")))
    await callback.message.edit_caption(caption=DefaultText, reply_markup=user_start_kb)

@user_router.callback_query(F.data == "choose_city")
async def csct(callback: types.CallbackQuery):
    global back_mode
    await callback.answer()
    await callback.message.edit_caption(caption="Выберете город", reply_markup=city_kb)
    back_mode = 0

#city choose
@user_router.callback_query(F.data == "klgd")
@user_router.callback_query(F.data == "zel")
@user_router.callback_query(F.data == "sve")
@user_router.callback_query(F.data == "pol")
@user_router.callback_query(F.data == "yant")
@user_router.callback_query(F.data == "cher")
@user_router.callback_query(F.data == "Все города")
async def user_city(callback: types.CallbackQuery):
    global user_citylist, back_mode
    txt = callback.data
    if txt == "Все города":
        user_citylist.append("klgd")
        user_citylist.append("zel")
        user_citylist.append("sve")
        user_citylist.append("yant")
        user_citylist.append("pol")
        user_citylist.append("sve")
    else:
        user_citylist.append(txt)
    await callback.answer()
    await callback.message.edit_caption(caption="Выберете тип.", reply_markup=type_kb)
    back_mode = 1

#type choose and create inline keyboard of places
@user_router.callback_query(F.data == "kult")
@user_router.callback_query(F.data == "ent")
@user_router.callback_query(F.data == "food")
@user_router.callback_query(F.data == "liv")
@user_router.callback_query(F.data == "driv")
@user_router.callback_query(F.data == "SPA")
@user_router.callback_query(F.data == "suv")
@user_router.callback_query(F.data == "tur")
@user_router.callback_query(F.data == "Все типы")
async def user_type(callback: types.CallbackQuery):
    global user_typelist, user_citylist, back_mode
    if callback.data == "Все типы":
        user_typelist.append("kult")
        user_typelist.append("ent")
        user_typelist.append("food")
        user_typelist.append("liv")
        user_typelist.append("driv")
        user_typelist.append("SPA")
        user_typelist.append("suv")
        user_typelist.append("tur")
    else:
        user_typelist.append(callback.data)
    await callback.answer()
    if len(name_kb_create(user_citylist, user_typelist)) > 1:
        await callback.answer()
        await callback.message.edit_caption(caption="Выберете место", reply_markup=InlineKeyboardMarkup(inline_keyboard=name_kb_create(user_citylist, user_typelist)))
    else:
        await callback.answer()
        await callback.message.edit_caption(caption="Подходящих объектов не найдено", reply_markup=inline_back_kb)
    back_mode = 2
@user_router.callback_query(F.data < '@')
async def user_data(callback: types.CallbackQuery):
    global ID, back_mode
    ID = int(callback.data)
    cursor.execute('SELECT Name, Address, desc, link, sale, Pic, City FROM places WHERE id = ?', (ID, ))
    Loc = cursor.fetchone()
    plc_txt = f"{Loc[0]} - это {Loc[2]}\n Находится по адресу: {Loc[1]}. \n " \
                  f"Ссылка на официальный сайт: {Loc[3]}. \n Скидка - {Loc[4]}%!"
    ddt = datetime.now()
    if visit_flag[ID] < ddt.toordinal():
        visit_flag[ID] =  ddt.toordinal()
        add_visit(Loc[0] + ' ' + CityCode(Loc[6]))
    if flag[ID]:
        add_visit(Loc[0] + ' ' + CityCode(Loc[6]))
        flag[ID] = False
    await callback.answer()
    await callback.message.edit_media(media=InputMediaPhoto(type='photo', media=Loc[5]))
    await callback.message.edit_caption(caption=plc_txt, reply_markup=inline_back_kb)
    back_mode = 3

#===============================================================================================================#
#=====================================================START WORKING=============================================#
asyncio.run(main())
