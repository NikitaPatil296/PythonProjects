from flask import Flask

# Create instance of the Flask
# __name__ is a special variable in Python that represents the name of the current module.
# Flask uses __name__ to determine the location of resources (like templates and static files).
# This line initializes the web application and associates it with the current module. 
# app is the object that you'll use to define routes and handle HTTP requests.
app = Flask(__name__)  


# This is a decorator that maps the URL path / (the root of the web application) -
# to the function immediately following it (hello in this case).
# enabling the web application to respond to requests at that URL.
@app.route("/")


def hello():
    return "Welcome to WebApp."


# if __name__ == '__main__': ensures that the application runs only when the script is executed directly, -
# not when it is imported as a module in another script.
# app.run(debug=True) starts the Flask development server.
# debug=True enables debugging features, such as:
# Automatic reloading of the server when you make changes to the code.
# Detailed error messages if something goes wrong.
if __name__ == '__main__':
    app.run(debug=True)