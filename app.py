from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

links = [
    {"name": "GitHub", "url": "https://github.com"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com"},
    {"name": "Python", "url": "https://www.python.org"},
]


@app.route("/")
def home():
    return render_template("index.html", links=links)


@app.route("/add", methods=["POST"])
def add_link():
    link_name = request.form.get("name", "").strip()
    link_url = request.form.get("url", "").strip()

    if link_name and link_url:
        links.append({"name": link_name, "url": link_url})

    return redirect(url_for("home"))


@app.route("/edit/<int:link_index>", methods=["GET", "POST"])
def edit_link(link_index):
    if not 0 <= link_index < len(links):
        return redirect(url_for("home"))

    if request.method == "POST":
        links[link_index]["name"] = request.form.get("name", "").strip()
        links[link_index]["url"] = request.form.get("url", "").strip()
        return redirect(url_for("home"))

    return render_template("edit.html", link=links[link_index], link_index=link_index)


@app.route("/delete/<int:link_index>", methods=["POST"])
def delete_link(link_index):
    if 0 <= link_index < len(links):
        links.pop(link_index)

    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
