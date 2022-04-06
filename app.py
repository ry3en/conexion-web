from urllib import request
from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

url = 'https://apitodolist-ibero.herokuapp.com/api/tasks'
@app.route('/')
def home():
    try:
        response = request.get(url).json()['task']
    except:
        print("Error...")
        response = []

    return render_template('index.html', tasks = response)

if __name__ == '__main__':
    app.run(debug=True)
