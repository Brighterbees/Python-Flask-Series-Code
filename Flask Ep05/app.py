from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__) #Initialise app

# Config
from covid_india import states


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        state_name = request.form['name']
        
        cases = states.getdata(state_name)
       # print(cases)

        data = {
            'active' : cases['Active'],
            'cured' : cases['Cured'],
            'death' : cases['Death'],
        }
        print(data)
        return render_template('index.html', data = data)
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)