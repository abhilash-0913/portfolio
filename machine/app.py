from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
# machine/app.py
# This file sets up a simple Flask application with a single route that renders an HTML template.