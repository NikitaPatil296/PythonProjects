from flask import Flask,render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Nikita Patil',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2025'
    },
    {
        'author': 'Rohan More',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2025'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='AboutPage')

if __name__ == '__main__':
    app.run(debug=True)