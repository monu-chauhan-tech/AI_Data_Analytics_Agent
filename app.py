from flask import Flask, render_template, request, jsonify
from data_engine import DataEngine
from agent import AnalyticsAgent

app = Flask(__name__)

DATA_FILE = "data/employees.csv"

engine = DataEngine(DATA_FILE)
agent = AnalyticsAgent(engine)


@app.route("/")
def home():

    return render_template(
        "index.html",
        data=engine.get_data().to_dict(orient="records"),
        columns=list(engine.get_data().columns)
    )


# -------------------------
# DATA INFORMATION
# -------------------------

@app.route("/info")
def info():

    return jsonify(engine.get_info())


# -------------------------
# SEARCH
# -------------------------

@app.route("/search", methods=["POST"])
def search():

    data = request.json

    column = data.get("column")
    value = data.get("value")

    result = engine.search(column, value)

    if result is None:
        return jsonify({
            "success": False,
            "message": "Column not found"
        })

    return jsonify({
        "success": True,
        "data": result.to_dict(orient="records")
    })


# -------------------------
# CALCULATE
# -------------------------

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json

    operation = data.get("operation")
    column = data.get("column")

    if operation == "average":
        result = engine.calculate_average(column)

    elif operation == "sum":
        result = engine.calculate_sum(column)

    elif operation == "max":
        result = engine.calculate_max(column)

    elif operation == "min":
        result = engine.calculate_min(column)

    else:
        return jsonify({
            "success": False,
            "message": "Unknown calculation"
        })

    return jsonify({
        "success": True,
        "result": result
    })


# -------------------------
# ADD
# -------------------------

@app.route("/add", methods=["POST"])
def add():

    data = request.json

    engine.add_row(data)

    return jsonify({
        "success": True,
        "message": "Row added successfully"
    })


# -------------------------
# UPDATE
# -------------------------

@app.route("/update", methods=["POST"])
def update():

    data = request.json

    success = engine.update_row(
        data.get("id"),
        data.get("column"),
        data.get("value")
    )

    return jsonify({
        "success": success
    })


# -------------------------
# DELETE
# -------------------------

@app.route("/delete", methods=["POST"])
def delete():

    data = request.json

    success = engine.delete_row(
        data.get("id")
    )

    return jsonify({
        "success": success
    })

# -------------------------
# AI AGENT COMMAND
# -------------------------

@app.route("/command", methods=["POST"])
def command():

    data = request.json

    user_command = data.get("command", "")

    result = agent.process(user_command)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

