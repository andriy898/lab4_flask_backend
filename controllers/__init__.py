from flask import Blueprint, request, jsonify
from services import UserService
from dao import City, User
from dto import user_dto, hobby_dto

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users(): 
    return jsonify([user_dto(u) for u in UserService.get_all()]), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    d = request.json
    return jsonify(user_dto(UserService.create(d['username'], d['email'], d['city_id']))), 201

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    d = request.json
    u = UserService.update(id, d['username'], d['email'], d['city_id'])
    return jsonify(user_dto(u)) if u else (jsonify({"err": "404"}), 404)

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return (jsonify({"msg": "OK"}), 200) if UserService.delete(id) else (jsonify({"err": "404"}), 404)

# Запит M:1 (Для міста вивести людей)
@user_bp.route('/cities/<int:city_id>/users', methods=['GET'])
def get_city_users(city_id):
    c = City.query.get(city_id)
    return jsonify([user_dto(u) for u in c.users]) if c else (jsonify({"err": "404"}), 404)

# Запит для стикувальної таблиці M:M (Для користувача вивести хобі)
@user_bp.route('/users/<int:user_id>/hobbies', methods=['GET'])
def get_user_hobbies(user_id):
    u = User.query.get(user_id)
    return jsonify([hobby_dto(h) for h in u.hobbies]) if u else (jsonify({"err": "404"}), 404)
