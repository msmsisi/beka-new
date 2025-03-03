# db.py
import sqlite3

def create_db():
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS delivery_countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            delivery_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_tariffs_table():
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tariffs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            service TEXT NOT NULL,
            price REAL NOT NULL,
            unit TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_country_and_cities():
    countries_and_cities = {
        'Россия': [
            ('Москва', '4-7 дней (без учета задержек)'),
            ('Санкт-Петербург', '5-8 дней (без учета задержек)'),
            ('Казань', '5-8 дней (без учета задержек)'),
            ('Уфа', '5-8 дней (без учета задержек)'),
            ('Самара', '5-8 дней (без учета задержек)'),
            ('Оренбург', '6-9 дней (без учета задержек)'),
            ('Челябинск', '7-10 дней (без учета задержек)'),
            ('Красноярск', '6-9 дней (без учета задержек)'),


            
            ('Новосибирск', '5-7 дней (без учета задержек)'),
            ('Екатеринбург', '4-6 дней (без учета задержек)')

        ],
        'Казахстан': [
            ('Алматы', '1 день'),
            ('Нур-Султан', '2-3 дня'),
            ('Шымкент', '2-3 дня'),
            ('Караганда', '2-3 дня')
        ],
        'Узбекистан': [
            ('Ташкент', '5-8 дней'),
            ('Самарканд', '5-8 дней'),
            ('Бухара', '5-8 дней'),
        ],
        'Таджикистан': [
            ('Душанбе', '3-5 дней'),
            ('Худжанд', '4-6 дней'),
            ('Бохтар', '4-6 дней'),
            ('Куляб', '5-7 дней')
        ]
    }

    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()
    for country, cities in countries_and_cities.items():
        for city, delivery_time in cities:
            cursor.execute("""
                INSERT INTO delivery_countries (country, city, delivery_time)
                VALUES (?, ?, ?)
            """, (country, city, delivery_time))
    conn.commit()
    conn.close()

def add_tariffs():
    tariffs = [
        ('Россия', 'Москва', 'Пошив', 50, 'р/кг'),
        ('Россия', 'Москва', 'Привозные', 55, 'р/кг'),
        ('Россия', 'Москва', 'Маркированный товар', 65, 'р/кг'),
        ('Россия', 'Москва', 'Бренд', 65, 'р/кг'),
        ('Россия', 'Москва', 'Обувь', 170, 'р/кг'),

        ('Россия', 'Казань', 'Пошив', 45, 'р/кг'),
        ('Россия', 'Казань', 'Привозные', 55, 'р/кг'),
        ('Россия', 'Казань', 'Маркированный товар', 65, 'р/кг'),
        ('Россия', 'Казань', 'Бренд', 65, 'р/кг'),
        ('Россия', 'Казань', 'Обувь', 170, 'р/кг'),


        ('Россия', 'Уфа', 'Пошив', 45, 'р/кг'),
        ('Россия', 'Уфа', 'Привозные', 55, 'р/кг'),
        ('Россия', 'Уфа', 'Маркированный товар', 55, 'р/кг'),
        ('Россия', 'Уфа', 'Бренд', 65, 'р/кг'),
        ('Россия', 'Уфа', 'Обувь', 170, 'р/кг'),

        ('Россия', 'Самара', 'Пошив', 55, 'р/кг'),
        ('Россия', 'Самара', 'Привозные', 55, 'р/кг'),
        ('Россия', 'Самара', 'Маркированный товар', 65, 'р/кг'),
        ('Россия', 'Самара', 'Бренд', 65, 'р/кг'),
        ('Россия', 'Самара', 'Обувь', 170, 'р/кг'),

        ('Россия', 'Самара', 'Пошив', 55, 'р/кг'),
        ('Россия', 'Самара', 'Привозные', 55, 'р/кг'),
        ('Россия', 'Самара', 'Маркированный товар', 65, 'р/кг'),
        ('Россия', 'Самара', 'Бренд', 65, 'р/кг'),
        ('Россия', 'Самара', 'Обувь', 170, 'р/кг'),

        ('Россия', 'Оренбург', 'Пошив', 60, 'р/кг'),
        ('Россия', 'Оренбург', 'Привозные', 60, 'р/кг'),
        ('Россия', 'Оренбург', 'Маркированный товар', 70, 'р/кг'),
        ('Россия', 'Оренбург', 'Бренд', 70, 'р/кг'),
        ('Россия', 'Оренбург', 'Обувь', 170, 'р/кг'),

        ('Россия', 'Челябинск', 'Пошив', 50, 'р/кг'),
        ('Россия', 'Челябинск', 'Привозные', 55, 'р/кг'),
        ('Россия', 'Челябинск', 'Маркированный товар', 65, 'р/кг'),
        ('Россия', 'Челябинск', 'Бренд', 65, 'р/кг'),
        ('Россия', 'Челябинск', 'Обувь', 170, 'р/кг'),


        ('Казахстан', 'Алматы', 'Ред бир карго', 180, 'тенге/кг'),
        ('Казахстан', 'Алматы', 'Частники берут за объём от 1000-8000 тенге', "", 'тенге/объем'),

        ('Узбекистан', 'Ташкент', 'Пошив', 55, 'р/кг'),
        ('Узбекистан', 'Ташкент', 'Привозные', 60, 'р/кг'),
        ('Узбекистан', 'Ташкент', 'Маркированный товар', 75, 'р/кг'),
        ('Узбекистан', 'Ташкент', 'Бренд', 75, 'р/кг'),
        ('Узбекистан', 'Ташкент', 'Обувь', 160, 'р/кг'),

        ('Таджикистан', 'Душанбе', 'Пошив', 65, 'р/кг'),
        ('Таджикистан', 'Душанбе', 'Привозные', 70, 'р/кг'),
        ('Таджикистан', 'Душанбе', 'Маркированный товар', 80, 'р/кг'),
        ('Таджикистан', 'Душанбе', 'Бренд', 80, 'р/кг'),
        ('Таджикистан', 'Душанбе', 'Обувь', 190, 'р/кг')
    ]

    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO tariffs (country, city, service, price, unit)
        VALUES (?, ?, ?, ?, ?)
    """, tariffs)
    conn.commit()
    conn.close()

def get_tariffs_by_city_and_country(country, city):
  conn = sqlite3.connect('delivery_countries.db')
  cursor = conn.cursor()
  cursor.execute("SELECT service, price, unit FROM tariffs WHERE country = ? AND city = ?", (country, city))
  tariffs = cursor.fetchall()
  conn.close()
  return tariffs


def get_cities_by_country(country):
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT city, delivery_time FROM delivery_countries WHERE country = ?
    """, (country,))
    cities = cursor.fetchall()
    conn.close()
    return [(city, delivery_time) for city, delivery_time in cities]

def get_all_countries():
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT country FROM delivery_countries")
    countries = [row[0] for row in cursor.fetchall()]
    conn.close()
    return countries
