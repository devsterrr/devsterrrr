from flask import Flask

app = Flask(__name__)
# @app.route('/')
# def home():
#     return "<h1>Мій профіль</h1> <p>Ласкаво просимо!</p>"

# @app.route('/about')
# def about():
#     return "<h2>Про мене</h2><p>Автор: Yarik</p>"

# @app.route('/skills')
# def skills():
#     return "<h2>Мої навички</h2><p>Python, Flask, HTML, SQL</p>"

# @app.route('/contact')
# def contact():
#     return "<h2>Контакти</h2><p>email@example.com</p>"
# if __name__ == '__main__':
#     app.run(debug=True)



@app.route('/temperature/<int:t>')

def temperature(t):

    if t < 0:
        return "<h2>Мороз</h2>"

    elif t < 20:
        return "<h2>Прохолодно</h2>"

    elif t < 30:
        return "<h2>Тепло</h2>"

    else:
        return "<h2>Спека</h2>"
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
@app.route('/math/<operation>/<int:a>/<int:b>')
def math(operation, a, b):

    if operation == "add":
        return f"<h2>Результат: {a + b}</h2>"

    elif operation == "sub":
        return f"<h2>Результат: {a - b}</h2>"

    elif operation == "mul":
        return f"<h2>Результат: {a * b}</h2>"

    elif operation == "div":
        if b == 0:
            return "<h2>Помилка: ділення на нуль</h2>"
        return f"<h2>Результат: {a / b}</h2>"

    else:
        return "<h2>Невідома операція</h2>"


if __name__ == '__main__':
    app.run(debug=True)
