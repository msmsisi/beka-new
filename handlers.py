# handlers.py
from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
from keyboards import (
    main_menu_keyboard,
    order_menu_keyboard,
    assortment_menu_keyboard,
    about_us_menu_keyboard,
    faq_menu_keyboard,
    countries_keyboard,
    cities_keyboard,
)
from config import OPERATOR_CHAT_ID
from db import get_cities_by_country, get_tariffs_by_city_and_country

# Создаем роутер
router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=main_menu_keyboard())

# Обработчик нажатий на инлайн кнопки
@router.callback_query()
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == "order_menu":
        await callback_query.message.edit_text("Меню 'Заказать'", reply_markup=order_menu_keyboard())
    elif callback_query.data == "contact_operator":
        await callback_query.bot.send_message(OPERATOR_CHAT_ID, f"Пользователь {callback_query.message.chat.id} хочет связаться с вами")
        await callback_query.message.edit_text("Сейчас с вами свяжется оператор")
    elif callback_query.data == "assortment_menu":
        await callback_query.message.edit_text("Ознакомьтесь с нашим ассортиментом:", reply_markup=assortment_menu_keyboard())
    elif callback_query.data == "about_us_menu":
        await callback_query.message.edit_text("О нас", reply_markup=about_us_menu_keyboard())
    elif callback_query.data == "faq_menu":
        await callback_query.message.edit_text("Ответы и Вопросы", reply_markup=faq_menu_keyboard())
    elif callback_query.data == "order_conditions":
        text = """
        Условия заказа / комиссия за услуги:
        (организационный сбор)

        Нет ограничения по сумме, от 1-упаковок (линией)

        До $99 - фиксированная комиссия 600 сом

        От $140 - 6% от суммы перевода (не израсходованный остаток - не учитывается)

        От $999 - торгуемо (учитывается сложность заказа) 🤝

        Выше $1999 - на усмотрение клиента в нижних пределах рыночных цен 🥳

        Дополнительно: Сохранность денежных средств и выкупленного товара, до момента сдачи перевозчику (если перевозчик согласован с заказчиком) гарантируется коллективом (команда из более 200 человек) Фэшн Рынок - только в случае перевода / исполнения заказа в рабочем чате заказчика (WhatsApp & Telegram) в присутствии номера wa.me/996500996500, wa.me/996501996501, @marketplacekg, @marketplace_kg

        От 10.12.2024 ©️ Лидер команды - Кайрат М.М.
        """
        await callback_query.message.answer(text, reply_markup=main_menu_keyboard())#изменено
    elif callback_query.data == "delivery":
        await callback_query.message.edit_text("Выберите страну:", reply_markup=countries_keyboard())
    elif callback_query.data.startswith("country_"):
        country = callback_query.data.split("_")[1]
        cities = get_cities_by_country(country)
        if cities:
            await callback_query.message.edit_text(f"Города {country}:", reply_markup=cities_keyboard(country))
        else:
            await callback_query.message.edit_text(f"В стране {country} пока нет доступных городов.")
    elif callback_query.data.startswith("city_"):#изменено
        city = callback_query.data.split("_")[1] #изменено
        country = callback_query.data.split("_")[2]#изменено
        delivery_info = get_cities_by_country(country)
        tariffs = get_tariffs_by_city_and_country(country, city)
        for city_db, delivery_time in delivery_info:
            if city_db == city:
                text = f"Доставка в город {city}: {delivery_time}\n\nТарифы:\n"
                for service, price, unit in tariffs:
                    text += f"{service}: {price} {unit}\n"
                await callback_query.message.edit_text(text)
        await callback_query.message.answer("Меню 'Заказать'", reply_markup=order_menu_keyboard())
    elif callback_query.data == "dogovor_about" or callback_query.data == "dogovor_faq":
        await callback_query.message.edit_text("Загружаю договор...")

        file_path = "C:/Users/SenetUser/Downloads/bot-beka/dogovor_final_corrected_v2.pdf"  # Укажите путь к вашему файлу
        file = FSInputFile(file_path) # Вот тут и есть изменение
        await callback_query.message.answer_document(file)# Вот тут и есть изменение
        await callback_query.message.edit_text("Договор загружается") # Поменял сообщение
        await callback_query.message.answer("Главное меню", reply_markup=main_menu_keyboard())



    
    elif callback_query.data == "back":
        if callback_query.message.text == "Меню 'Заказать'" or callback_query.message.text == "О нас" or callback_query.message.text == "Ответы и Вопросы":
            await callback_query.message.edit_text("Главное меню", reply_markup=main_menu_keyboard())
        elif callback_query.message.text == "Ознакомьтесь с нашим ассортиментом:":
            await callback_query.message.edit_text("Меню 'Заказать'", reply_markup=order_menu_keyboard())
        elif callback_query.message.text.startswith("Города"):
            await callback_query.message.edit_text("Выберите страну:", reply_markup=countries_keyboard())
        elif callback_query.message.text == "Выберите страну:":
            await callback_query.message.edit_text("Ответы и Вопросы", reply_markup=faq_menu_keyboard())
        else:
            await callback_query.message.edit_text("Главное меню", reply_markup=main_menu_keyboard())

    elif callback_query.data == "main_menu":
      await callback_query.message.edit_text("Главное меню", reply_markup=main_menu_keyboard())
    else:
        await callback_query.message.edit_text("Функционал в разработке")
