from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    links = [
        {"name": "GitHub", "url": "https://github.com"},
        {"name": "LinkedIn", "url": "https://www.linkedin.com"},
        {"name": "Python", "url": "https://www.python.org"},
    ]
    return render_template("index.html", links=links)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
