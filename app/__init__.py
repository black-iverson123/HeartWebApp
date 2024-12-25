from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "wqwoe194321ejwqj"
bootstrap = Bootstrap(app)

from app import views