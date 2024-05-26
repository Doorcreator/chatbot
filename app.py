from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"
@app.route('/user/<name>')
def user_page(name):
    return f'Your name is {escape(name)}'
@app.route("/test")
def test_url_for():
    print(url_for("hello"))
    print(url_for("user_page", name="Apple"))
    print(url_for("test_url_for", xxnum=2, page="88"))
    return "test Page"
    
# (venv) D:\python3.7.0\venv\watchlist
# flask run
