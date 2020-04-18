from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tables(db.Model):
    __tablename__="tables"
    Username = db.Column(db.String,primary_key = True)
    psw =db.Column(db.String,nullable = False)

    def __init__(self,Username,psw):
        self.Username = Username
        self.psw = psw
