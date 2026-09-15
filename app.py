from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html")

if _name_ == "_main_":
    app.run(debug=True)
