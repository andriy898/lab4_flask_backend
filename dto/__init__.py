def user_dto(user):
    return {"id": user.id, "username": user.username, "email": user.email, "city_id": user.city_id}

def city_dto(city):
    return {"id": city.id, "name": city.name}

def hobby_dto(hobby):
    return {"id": hobby.id, "name": hobby.name}
