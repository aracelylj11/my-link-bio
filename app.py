from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

NOT_AVAILABLE = "Not Available"


def create_link(link_name, link_url):
    metadata = fetch_open_graph_metadata(link_url)
    return {"name": link_name, "url": link_url, **metadata}


def fetch_open_graph_metadata(link_url):
    import requests
    from bs4 import BeautifulSoup

    metadata = {
        "title": NOT_AVAILABLE,
        "description": NOT_AVAILABLE,
        "image_url": NOT_AVAILABLE,
    }

    try:
        response = requests.get(link_url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return metadata

    soup = BeautifulSoup(response.text, "html.parser")
    meta_fields = {
        "title": "og:title",
        "description": "og:description",
        "image_url": "og:image",
    }

    for metadata_key, meta_property in meta_fields.items():
        meta_tag = soup.find("meta", property=meta_property)
        # Empty content should be treated the same as a missing Open Graph tag.
        if meta_tag and meta_tag.get("content", "").strip():
            metadata[metadata_key] = meta_tag["content"].strip()

    return metadata


links = [
    {
        "name": "GitHub",
        "url": "https://github.com",
        "title": NOT_AVAILABLE,
        "description": NOT_AVAILABLE,
        "image_url": NOT_AVAILABLE,
    },
    {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com",
        "title": NOT_AVAILABLE,
        "description": NOT_AVAILABLE,
        "image_url": NOT_AVAILABLE,
    },
    {
        "name": "Python",
        "url": "https://www.python.org",
        "title": NOT_AVAILABLE,
        "description": NOT_AVAILABLE,
        "image_url": NOT_AVAILABLE,
    },
]


@app.route("/")
def home():
    return render_template("index.html", links=links)


@app.route("/add", methods=["POST"])
def add_link():
    link_name = request.form.get("name", "").strip()
    link_url = request.form.get("url", "").strip()

    if link_name and link_url:
        links.append(create_link(link_name, link_url))

    return redirect(url_for("home"))


@app.route("/edit/<int:link_index>", methods=["GET", "POST"])
def edit_link(link_index):
    if not 0 <= link_index < len(links):
        return redirect(url_for("home"))

    if request.method == "POST":
        link_name = request.form.get("name", "").strip()
        link_url = request.form.get("url", "").strip()
        links[link_index] = create_link(link_name, link_url)
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
