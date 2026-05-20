from dao import db, User

class UserService:
    @staticmethod
    def get_all(): 
        return User.query.all()
    
    @staticmethod
    def create(username, email, city_id):
        u = User(username=username, email=email, city_id=city_id)
        db.session.add(u)
        db.session.commit()
        return u
        
    @staticmethod
    def update(uid, username, email, city_id):
        u = User.query.get(uid)
        if u: 
            u.username, u.email, u.city_id = username, email, city_id
            db.session.commit()
        return u
        
    @staticmethod
    def delete(uid):
        u = User.query.get(uid)
        if u: 
            db.session.delete(u)
            db.session.commit()
            return True
        return False
