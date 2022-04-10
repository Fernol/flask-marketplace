from datetime import datetime

from marketplace.__init__ import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=1)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True)
    content = db.Column(db.String(10000), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roleId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=1)
    firstName = db.Column(db.String(50), nullable=True)
    lastName = db.Column(db.String(50), nullable=True)
    mobile = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    passwordHash = db.Column(db.String(300), nullable=False)
    registeredAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    lastLogin = db.Column(db.DateTime, nullable=True)
    intro = db.Column(db.String(255), nullable=True)
    profile = db.Column(db.String(10000), nullable=True)
