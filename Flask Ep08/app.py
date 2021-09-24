from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  # Initialise app

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db = SQLAlchemy(app)


# Database Table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200))
    email = db.Column(db.String(200))
    contact = db.Column(db.Integer)
    course = db.Column(db.String(200))

@app.route('/')
def index():
    students = Student.query.all()
    print(students)
    return render_template('index.html', students = students)


@app.route('/add', methods = ['GET', 'POST'])
def add():
        if request.method == 'POST':
               name = request.form['name']
               email = request.form['email']
               contact = request.form['contact']
               course = request.form['course']
               print(name, email, contact, course)

               new_student = Student(name = name, email = email, contact = contact, course = course)
               db.session.add(new_student)
               db.session.commit() 
               return render_template('add.html')

        else:
              return render_template('add.html')


# Delete Route
@app.route('/delete/<int:id>')
def deleteStudent(id):
    print(id)
    student = Student.query.get_or_404(id)
    print(student)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)