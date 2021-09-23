from flask import Flask, request, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html')


app.run('localhost', port='2380')
