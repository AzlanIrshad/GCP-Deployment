from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Retrieve values from form
        num1 = request.form.get("num1", type=float)
        num2 = request.form.get("num2", type=float)
        operator = request.form.get("operator")

        # Perform the calculation based on the operator
        if operator == "add":
            result = num1 + num2
        elif operator == "subtract":
            result = num1 - num2
        elif operator == "multiply":
            result = num1 * num2
        elif operator == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
