from flask import Flask, render_template

app = Flask(__name__)

# Данные для сайта
mayor_data = {
    "name": "Дмитрий Анатольевич",
    "title": "Мер Киева",

    "news": [
    ]
}

@app.route('/')
def index():
    return render_template('index.html', mayor=mayor_data)

if __name__ == '__main__':
    # Запуск сервера
    app.run(debug=True)
