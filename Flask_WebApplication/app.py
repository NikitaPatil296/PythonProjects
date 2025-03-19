from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask Web App Rohan More!"

# Example of an API route
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # Get 'name' parameter from query string
    return jsonify(message=f"Hello, {name}!")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
