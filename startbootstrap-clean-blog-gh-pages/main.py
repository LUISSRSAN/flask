from flask import Flask, render_template
import requests
from flask import request
app = Flask(__name__)
@app.route("/")
def get_home():
    api_url = "https://api.npoint.io/c093d0d9edaa35110906"
    response = requests.get(api_url)
    blog_posts = response.json()

    return render_template("index.html",posts = blog_posts)

@app.route("/about")
def get_about():
    return render_template("about.html")
@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/post")
def get_post():
    return render_template("post.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"

    return render_template("contact.html")

if __name__ =="__main__":
    app.run(debug=True)