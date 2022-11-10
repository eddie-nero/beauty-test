from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "result": "ok",
    }


@app.route("/some-function")
def some_function():
    return "Some function"


@app.route("/another-function")
def another_function():
    return "Another function"


@app.route("/Datalore", methods=("GET", "POST"))
def webhook():
    if request.method == "GET":
        return "Simple webhook route"
    if request.method == "POST":
        request_data = request.get_json()
        function_to_call = request_data["function"]
        return redirect(url_for(function_to_call))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
