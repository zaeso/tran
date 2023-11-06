
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'h1 Этот сайт выдаёт рандомно арла или решку. <a href="/additional">Перейти на второй сайт</a>'

@app.route('/additional')
def additional():
    result = coin_flip()
    return 'Второй сайт. Результат монетки: {}'.format(result)

def coin_flip():
    return random.choice(['Орёл', 'Решка'])

if __name__ == '__main__':
    app.run()
