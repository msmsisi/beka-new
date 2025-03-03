import sqlite3

def create_db():
    # Создаем подключение к базе данных (файл будет создан, если его нет)
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она еще не существует
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

def add_country_and_cities():
    # Данные для добавления в базу данных
    countries_and_cities = {
        'Россия': [
            ('Москва', '4-7 дней'),
            ('Санкт-Петербург', '5-8 дней'),
            ('Новосибирск', '5-7 дней'),
            ('Екатеринбург', '4-6 дней')
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

    # Создаем подключение к базе данных
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()

    # Добавляем данные в таблицу
    for country, cities in countries_and_cities.items():
        for city, delivery_time in cities:
            cursor.execute("""
                INSERT INTO delivery_countries (country, city, delivery_time)
                VALUES (?, ?, ?)
            """, (country, city, delivery_time))

    conn.commit()
    conn.close()

def get_cities_by_country(country):
    # Получаем города и сроки доставки по названию страны
    conn = sqlite3.connect('delivery_countries.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT city, delivery_time FROM delivery_countries WHERE country = ?
    """, (country,))
    
    cities = cursor.fetchall()
    conn.close()
    
    return [(city, delivery_time) for city, delivery_time in cities]

# Создаем базу данных и добавляем данные
create_db()
add_country_and_cities()

# Пример использования
print("Города России с сроками доставки:", get_cities_by_country("Россия"))
print("Города Казахстана с сроками доставки:", get_cities_by_country("Казахстан"))
