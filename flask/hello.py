from flask import Flask
from pywebio.platform.flask import webio_view  # import the WebioHandler class

app = Flask(__name__)

@app.route("/")
def hello_world():
    view1 = webio_view(url="http://localhost:5000/data-creator.py")
    return view1
