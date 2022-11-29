from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_name = db.Column(db.String(20), nullable=False)
