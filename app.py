from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV
df = pd.read_csv("students_500.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]

    # Check if student name exists
    student = df[df["name"] == name]

    if student.empty:
        return render_template("index.html", message="Student not found!")

    mark1 = int(student["mark1"].values[0])
    mark2 = int(student["mark2"].values[0])
    mark3 = int(student["mark3"].values[0])
    total = mark1 + mark2 + mark3
    avg = round(total / 3, 2)

    return render_template("index.html",
                           name=name,
                           mark1=mark1,
                           mark2=mark2,
                           mark3=mark3,
                           total=total,
                           avg=avg)

if __name__ == "__main__":
    app.run(debug=True)
