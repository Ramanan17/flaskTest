from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='cop4814'

from FDA_Project_Flask import routes