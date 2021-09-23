from flask import Flask, request, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    with open('favicon.ico', 'rb') as f:
        return f.read()


app.run('localhost', port='2380')
