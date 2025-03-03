# keyboards.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import get_cities_by_country, get_all_countries

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text="Заказать", callback_data="order_menu"),
        ],
        [
            InlineKeyboardButton(text="О нас", callback_data="about_us_menu"),
        ],
        [
            InlineKeyboardButton(text="Ответы и Вопросы", callback_data="faq_menu"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def order_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text="Связаться с оператором", callback_data="contact_operator"),
        ],
        [
            InlineKeyboardButton(text="Ознакомиться с Ассортиментом", callback_data="assortment_menu"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def assortment_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text="Женская одежда", callback_data="women_clothes"),
        ],
        [
            InlineKeyboardButton(text="Турция-Китай", callback_data="turkey_china"),
        ],
        [
            InlineKeyboardButton(text="Детское", callback_data="children"),
        ],
        [
            InlineKeyboardButton(text="Обувь", callback_data="shoes"),
        ],
        [
            InlineKeyboardButton(text="Мужское", callback_data="man_clothes"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back"),
            InlineKeyboardButton(text="Главное меню", callback_data="main_menu"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def about_us_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text="Контакты", callback_data="contacts"),
        ],
        [
            InlineKeyboardButton(text="Инстаграм", callback_data="instagram"),
        ],
        [
            InlineKeyboardButton(text="Телеграм", callback_data="telegram"),
        ],
        [
            InlineKeyboardButton(text="ВК", callback_data="vk"),
        ],
        [
            InlineKeyboardButton(text="Отзывы", callback_data="reviews"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def faq_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text="Условия заказа", callback_data="order_conditions"),
        ],
        [
            InlineKeyboardButton(text="Доставка", callback_data="delivery"),
        ],
        [
            InlineKeyboardButton(text="Договор", callback_data="dogovor_faq"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def countries_keyboard():
    countries = get_all_countries()
    keyboard = []
    for country in countries:
        keyboard.append([InlineKeyboardButton(text=country, callback_data=f"country_{country}")])
    keyboard.append([InlineKeyboardButton(text="Назад", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def cities_keyboard(country):
  """Клавиатура с городами для выбранной страны."""
  cities = get_cities_by_country(country)
  keyboard = []
  for city, delivery_time in cities:
      keyboard.append([InlineKeyboardButton(text=f"{city}", callback_data=f"city_{city}_{country}")])# изменено
  keyboard.append([InlineKeyboardButton(text="Назад", callback_data="back")])
  return InlineKeyboardMarkup(inline_keyboard=keyboard)
