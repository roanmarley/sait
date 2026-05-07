from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# --- ЛОГИКА ГОЛОСОВАНИЯ ---
DB_FILE = 'votes.json'

def load_votes():
    """Загружает количество голосов из файла"""
    if not os.path.exists(DB_FILE):
        return 0
    with open(DB_FILE, 'r') as f:
        data = json.load(f)
        return data.get('count', 0)

def save_votes(count):
    """Сохраняет количество голосов в файл"""
    with open(DB_FILE, 'w') as f:
        json.dump({'count': count}, f)

# --- ДАННЫЕ МЭРА ---
mayor_data = {
    "name": "Дмитрий Анатольевич",
    "title": "Мэр Киева",
    "news": []
}

@app.route('/')
def index():
    # Подгружаем актуальное количество голосов перед рендерингом
    current_votes = load_votes()
    return render_template('index.html', mayor=mayor_data, votes=current_votes)

@app.route('/vote', methods=['POST'])
def vote():
    """Маршрут для обработки нажатия кнопки"""
    current_votes = load_votes()
    current_votes += 1
    save_votes(current_votes)
    return jsonify(success=True, new_count=current_votes)

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.run(debug=True)
