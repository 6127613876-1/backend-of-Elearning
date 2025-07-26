from flask import Flask
from quiz import app as quiz_app
from doubtclarification import app as doubt_app
from summary import app as summary_app
from simulation import app as simulation_app
from meet2 import app as meet2_app

main_app = Flask(__name__)

main_app.register_blueprint(quiz_app, url_prefix='/quiz')
main_app.register_blueprint(doubt_app, url_prefix='/doubt')
main_app.register_blueprint(summary_app, url_prefix='/summary')
main_app.register_blueprint(simulation_app, url_prefix='/simulation')
main_app.register_blueprint(meet2_app, url_prefix='/meet')
