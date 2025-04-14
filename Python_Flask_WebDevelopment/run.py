from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
# initialze the app with extention
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    content=db.Column(db.String(700),nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} {self.title}"


@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        title= request.form['title']
        content= request.form['content']
        todos = Todo(title=title,content=content)
        db.session.add(todos)
        db.session.commit()
    allTodos = Todo.query.all()
    return render_template('index.html',allTodos=allTodos)


@app.route('/delete/<int:sno>')
def delete(sno):
    todos= Todo.query.filter_by(sno=sno).first()
    db.session.delete(todos)
    db.session.commit()
    return redirect("/")

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/documentation")
def documentation():
    return render_template('documentation.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)