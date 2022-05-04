from flask import Flask, redirect
from flask import render_template, request
import requests

app = Flask(__name__)

url = 'https://apitodolist-ibero.herokuapp.com/api/tasks'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        try:
            tasks = requests.get(url).json()['tasks']

            completed = []
            incompleted = []

            for task in tasks:
                print(task['check'])
                if task['check'] == True:
                    completed.append(task)
                else:
                    incompleted.append(task)

            print(f'COMPLETAS : {completed}')
            print(f'INCOMPLETAS : {incompleted}')
        except:
            print('Error...')
            tasks = []
        response = {'completed': completed,
                    'incompleted': incompleted,
                    'counter1': len(completed),
                    'counter2': len(incompleted)
                    }
        return render_template('index.html', response=response)
    else:
        name = request.form["name"]
        request.post(url, json={"name": name})
        try:
            print(f'\n{name}\n')

            return redirect('/')
        except:
            return render_template('error.html', response='response')

@app.route('/update/'+'<int:id>', methods=['GET'])
def update(id):
    print(f'\nActualizaras la tarea: {id}\n')
    try:
        requests.put(url + "/" + str(id), json={"check":True})
        return redirect('/')
    except:
        return render_template('error.html', response='response')

@app.route('/delete/'+'<int:id>', methods=['GET'])
def delete(id):
    print(f'\nBorraras la tarea\n')
    try:
        requests.delete(url+'/'+str(id))
        print('Tarea Eliminada...')
        return redirect('/')
    except:
        return render_template('error.html', response='response')
if __name__ == '__main__':
    app.run(debug=True)
