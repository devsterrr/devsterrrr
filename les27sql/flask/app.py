from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

app = Flask(__name__)
db_path = "tasks.db"
def get_db():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(db_path):
        conn = get_db()
        conn.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            date TEXT,
            country TEXT,
            priority TEXT
        )
        """)
        conn.commit()
        conn.close()

init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()

    if request.method == "POST":
        task = request.form.get("task")
        date = request.form.get("date")
        country = request.form.get("country")
        priority = request.form.get("priority")

        if task:
            conn.execute(
                "INSERT INTO tasks (task, date, country, priority) VALUES (?, ?, ?, ?)",
                (task, date, country, priority)
            )
            conn.commit()

        return redirect(url_for("index"))

    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)