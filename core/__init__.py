from flask import Flask 
app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
#app.config.from_object('core.config.ProductionConfig')

config = app.config

from core.controller.StudentController import app as student

app.register_blueprint(student, url_prefix='')