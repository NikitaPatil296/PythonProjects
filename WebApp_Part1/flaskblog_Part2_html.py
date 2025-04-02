from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return ''' <!DOCTYPE html>
    <html>
    <head>
        <title>Simple HTML Page</title>
    </head>
    <body>
        <h1>Welcome to My Webpage</h1>
        <p>This is a simple HTML page.</p>
        <ul>
            <li>HTML is easy to learn.</li>
            <li>It is used to structure web content.</li>
        </ul>
        <a href="https://www.w3schools.com/html/" target="_blank">Visit w3schools.com</a>
    </body>
    </html>
    '''

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)