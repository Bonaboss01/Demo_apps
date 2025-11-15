from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
@app.route("/")
def home_1():
    return render_template('index.html')
# Home route
@app.route("/")
def home():
    return {"message": "Welcome to Bona's API!"}

# Dynamic route example
@app.route("/hello/<name>")
def hello(name):
    return {"message": f"Hello, {name}!"}

# API endpoint using POST
@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.json
    if "a" not in data or "b" not in data:
        return {"error": "Both 'a' and 'b' are required"}, 400
    return {"result": data["a"] + data["b"]}

# 404 error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Route not found"), 404

# 500 error handler
@app.errorhandler(500)
def server_error(e):
    return jsonify(error="Server error occurred"), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
