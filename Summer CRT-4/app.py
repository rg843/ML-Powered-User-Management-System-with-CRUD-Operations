from flask import Flask, render_template, request, redirect, url_for
from model import predict_category

app = Flask(__name__)

records = [
    {"id": 1, "name": "Gopi", "age": 21, "category": predict_category(21)},
    {"id": 2, "name": "Ravi", "age": 20, "category": predict_category(20)},
]


def get_next_id():
    return max([record["id"] for record in records], default=0) + 1


@app.route("/")
def index():
    edit_id = request.args.get("edit_id", type=int)
    edit_record = None
    if edit_id is not None:
        edit_record = next((record for record in records if record["id"] == edit_id), None)
    return render_template("index.html", records=records, edit_record=edit_record)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    if not name or not age.isdigit():
        return redirect(url_for("index"))

    age_value = int(age)
    category = predict_category(age_value)
    new_record = {
        "id": get_next_id(),
        "name": name,
        "age": age_value,
        "category": category,
    }
    records.append(new_record)
    return redirect(url_for("index"))


@app.route("/edit/<int:record_id>")
def edit(record_id):
    return redirect(url_for("index", edit_id=record_id))


@app.route("/update/<int:record_id>", methods=["POST"])
def update(record_id):
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    if not name or not age.isdigit():
        return redirect(url_for("index"))

    age_value = int(age)
    category = predict_category(age_value)
    for record in records:
        if record["id"] == record_id:
            record["name"] = name
            record["age"] = age_value
            record["category"] = category
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:record_id>")
def delete(record_id):
    global records
    records = [record for record in records if record["id"] != record_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
