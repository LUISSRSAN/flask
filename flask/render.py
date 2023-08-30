from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello world!</h1>'\
            '<img src ="https://media.giphy.com/media/3o7TKuAfCHifvPdcxG/giphy.gif" width=500 height=500>'\
            '<img src = "https://media.giphy.com/media/yGLA1z4KSOPxFIDTJx/giphy.gif" width =700 height=500>'
@app.route('/bye')
def bye():
    return "bye"
if __name__ == '__main__':
    app.run()