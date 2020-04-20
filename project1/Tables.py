from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Tables(db.Model):
    __tablename__="users"
    Username = db.Column(db.String,primary_key = True)
    psw =db.Column(db.String,nullable = False)
    timestamp = db.Column(db.DateTime(timezone=True))


    def __init__(self,Username,psw):
        self.Username = Username
        self.psw = psw
        self.timestamp = datetime.now()
