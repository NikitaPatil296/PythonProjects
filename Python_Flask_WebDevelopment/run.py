from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/documentation")
def documentation():
    return render_template('documentation.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)