from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Стикувальна таблиця для зв'язку M:M (Користувачі <-> Хобі)
user_hobby = db.Table('user_hobby',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('hobby_id', db.Integer, db.ForeignKey('hobby.id'), primary_key=True)
)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='city', lazy=True) # Зв'язок M:1

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    hobbies = db.relationship('Hobby', secondary=user_hobby, backref=db.backref('users', lazy='dynamic')) # Зв'язок M:M
