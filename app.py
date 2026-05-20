from flask import Flask
from config import Config
from dao import db, City, Hobby, User
from controllers import user_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(user_bp)

with app.app_context():
    db.create_all() # Авто-створення таблиць в MySQL
    if not City.query.first(): # Генерація тестових даних
        c1 = City(name="Kyiv"); c2 = City(name="Lviv")
        h1 = Hobby(name="Football"); h2 = Hobby(name="Music")
        db.session.add_all([c1, c2, h1, h2]); db.session.commit()
        u = User(username="Andrii", email="test@test.com", city_id=c1.id)
        u.hobbies.append(h1); u.hobbies.append(h2)
        db.session.add(u); db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)