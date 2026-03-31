from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            description TEXT,
            year INTEGER,
            image_url TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/author')
def author():
    return render_template('author.html')


@app.route('/library')
def library():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('library.html', books=books)


@app.route('/book/<int:id>')
def book_detail(id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('book_detail.html', book=book)


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    description = request.form['description']
    year = request.form['year']
    image_url = request.form['image_url']

    conn = get_db_connection()
    conn.execute('''
        INSERT INTO books (title, author, description, year, image_url, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, author, description, year, image_url, datetime.now()))
    conn.commit()
    conn.close()

    return redirect(url_for('library'))


@app.route('/delete/<int:id>')
def delete_book(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('library'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    conn = get_db_connection()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        image_url = request.form['image_url']
        description = request.form['description']

        conn.execute('''
            UPDATE books
            SET title = ?, author = ?, year = ?, image_url = ?, description = ?
            WHERE id = ?
        ''', (title, author, year, image_url, description, id))
        conn.commit()
        conn.close()

        return redirect(url_for('library'))

    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    conn.close()

    return render_template('edit_book.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)