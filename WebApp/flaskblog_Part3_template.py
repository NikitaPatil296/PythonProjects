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
    },
    {
        'author': 'Marco Pozol',
        'title': 'The importance of the AI for big companies',
        'content': 'During the last years, the advancements in technology helped us to discover...',
        'date_posted': 'March 23, 2025'
    },
    {
        'author': 'John Parker',
        'title': 'How to revenue our ID for first time?',
        'content': 'Read this post if you wanna discover how to deal with this very stressfull situation...',
        'date_posted': 'January 17 , 2025'
    },
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='AboutPage')

if __name__ == '__main__':
    app.run(debug=True)