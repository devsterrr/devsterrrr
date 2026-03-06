import sqlite3


conn = sqlite3.connect("books.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")


cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("1984", "George Orwell"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Harry Potter", "J.K. Rowling"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("book","Author Name"))
conn.commit()


print("Список книг:")
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for book in books:
    print(book)


delete_id = int(input("Введіть id книги для видалення: "))
cursor.execute("DELETE FROM books WHERE id = ?", (delete_id,))
conn.commit()

print("Книгу видалено.")


print("Оновлений список:")
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for book in books:
    print(book)

conn.close()