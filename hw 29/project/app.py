import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/planner')
def planner():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY id DESC')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('planner.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if title:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description, created_at) VALUES (?, ?, ?)',
                       (title, description, created_at))
        conn.commit()
        conn.close()
    return redirect(url_for('planner'))

@app.route('/delete/<int:id>')
def delete_task(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('planner'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)