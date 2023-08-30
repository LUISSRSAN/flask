from flask import Flask
app = Flask(__name__)
import random


answer = random.randint(0,9)
@app.route('/')
def hello_world():
    return '<h1 >Guess a number between 0 and 9</h1>'\
            '<img  src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif" width=600 height=600>'
@app.route('/<int:number>')
def guess(number):
    if number > answer:
        return '<h1> Too High ,Try Again </h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" > '
    elif number < answer:
        return '<h1>Too Low,Try Again</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1>correct</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == '__main__':
    app.run()