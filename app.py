from flask import Flask,Blueprint, render_template
from blueprints.Exchange import Exchange
from blueprints.graph import graph
from blueprints.tableCurren import tableCurren
from blueprints.news import news
from blueprints.about import about
from models import db,About

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///About.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()


app.register_blueprint(Exchange)
app.register_blueprint(graph)
app.register_blueprint(tableCurren)
app.register_blueprint(news)
app.register_blueprint(about)



