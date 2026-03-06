# import sqlite3
# conn = sqlite3.connect("database.db") 
# cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL
#             )
# """)
# conn.commit()
# print('Виберіть дію:')
# print('1. Додати користувача')
# print('2.Видалити користувача')
# print('3. Показати всіх користувачів')
# choice=input('Введіть номер дії: ')
# if choice=='1':
#     name=input("Введіть ім'я користувача: ")
#     cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
#     conn.commit()
#     print(f"Користувач '{name}' доданий до бази даних.")
# elif choice=='2':
#     user_id=input("Введіть ID користувача для видалення: ")
#     cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
#     conn.commit()
#     print(f"Користувач з ID {user_id} видалений з бази даних.")
# elif choice=='3':
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     print("Користувачі в базі даних:")
#     for user in users:
#         print(f"ID: {user[0]}, Ім'я: {user[1]}")
# else:
#     print("Невірний вибір. Будь ласка, виберіть 1, 2 або 3.")
# conn.close()
# name=input("Enter your name: ")
# cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
# conn.commit()
# cursor.execute("SELECT * FROM users")
# users = cursor.fetchall()
# print("Users in the database:")
# for user in users:
#     print(f"ID: {user[0]}, Name: {user[1]}")
# conn.close()




import sqlite3
from datetime import datetime


conn = sqlite3.connect("events.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    event_date TEXT NOT NULL
)
""")


title = input("Введіть назву події: ")
date = input("Введіть дату події (YYYY-MM-DD): ")


cursor.execute(
    "INSERT INTO events (title, event_date) VALUES (?, ?)",
    (title, date)
)

conn.commit()


print("Усі події:")

cursor.execute("SELECT * FROM events")
events = cursor.fetchall()

for event in events:
    print(f"{event[0]} | {event[1]} | {event[2]}")


today = datetime.now().date()

print(" Майбутні події:")

for event in events:
    event_date = datetime.strptime(event[2], "%Y-%m-%d").date()

    if event_date >= today:
        print(f"{event[0]} | {event[1]} | {event[2]}")

conn.close()