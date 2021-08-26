from flask import Flask, render_template

app = Flask(__name__) #Initialise app


@app.route('/result/<int:marks>')
def result(marks):
    return render_template('result.html',marks=marks)


if __name__ == '__main__':
    app.run(debug=True)