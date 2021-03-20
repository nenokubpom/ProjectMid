from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class About(db.Model):
    __tablename__ = "About"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String())
    img = db.Column(db.String())
    description = db.Column(db.String())
    
    

