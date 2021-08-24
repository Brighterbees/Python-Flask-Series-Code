from flask import Flask

app = Flask(__name__) #Initialise app


@app.route('/')
def home():
    return '<h1 style="color:red">Home Page</h1>'

@app.route('/about')
def about():
    return 'About'

@app.route('/contact')
def contact():
    return 'Contact'



if __name__ == '__main__':
    app.run(debug=True)