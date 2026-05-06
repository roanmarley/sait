from flask import Flask, render_template

app = Flask(__name__)


mayor_data = {
    "name": "Дмитрий Анатольевич",
    "title": "Мер Киева",

    "news": [
    ]
}

@app.route('/')
def index():
    return render_template('index.html', mayor=mayor_data)

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')



if __name__ == '__main__':

    app.run(debug=True)
