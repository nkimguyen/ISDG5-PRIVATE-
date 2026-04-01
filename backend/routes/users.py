from flask import Blueprint, jsonify, request
from backend.models.db_crud import add_user,get_all_users,get_user_by_email,update_user,delete_user
from backend.routes.api_key_decorator import require_api_key

users_bp = Blueprint("users",__name__)

@users_bp.route("/list", methods=["GET"])
@require_api_key
def list():
    users = get_all_users()

    user_list = [
        {
            "id" : u[0],"
            "first_name": u[1],
            "last_name": u[2],"
            "email": u[3],
            "password": u[4],
            "phone_number": u[5],
            "address": u[6],
            "status": u[7],
            "type": u[8]
        }
        for u in users
    ]
    # returning a list of user dictionaries
    return jsonify({
        "status":"success",
        "message": "User list retrieved successfully",
        "user_list":user_list
    }), 200

@users_bp.route("/view",methods=["GET"])
@require_api_key
def view():
    data = request.json
    user_row = get_user_by_email(data["email"])

    if user_row is None:
        return jsonify({"status":"error", "message": f"User '{data['email']}' does not exist"}), 404
    
    # returning a single json object
    return jsonify({
        "status":"success",
        "message":f"User {user_row["name"]} retrieved successfully",
        "user": {
                "id" : user_row["id"],
                "first_name": user_row["first_name"],
                "last_name": user_row["last_name"],"
                "email": user_row["email"],
                "password": user_row["password"],
                "phone_number": user_row["phone_number"],
                "address": user_row["address"],
                "status": user_row["status"],
                "type": user_row["type"]
        }
    }), 200

@users_bp.route("/update",methods=["POST"])
@require_api_key
def update():
    data = request.json
    email = data["email"]
    user_row = get_user_by_email(email)

    if user_row is None:
        return jsonify({"status":"error", "message":f"User '{data['email']}' does not exist"}), 404
    
    id = data.get("id")
    name = data.get("name", user_row["name"])
    new_email = data.get("new_email", user_row["email"])
    password = data.get("password", user_row["password"])
    gender = data.get("gender", user_row["gender"])
    favcol = data.get("favcol", user_row["favcol"])

    update_user(email,name, new_email,password, gender, favcol)

    # skip password in the returned json
    return jsonify({
        "status":"success",
        "message": f"User {name} updated successfully",
        "user":{
            "id": id,
            "name": name,
            "email": email,
            "gender": gender,
            "favcol": favcol
        }
    }), 200

@users_bp.route("/add", methods=["POST"])
@require_api_key
def add():
    data = request.json

    user_row = get_user_by_email(data["email"])
    if user_row is not None:
        return jsonify({"status":"error", "message":f"Email '{data['email']}' already exists"}), 400
    
    name = data["name"]
    email = data["email"]
    password = data["password"]
    gender = data["gender"]
    favcol = data["favcol"]

    try:
        add_user(name,email,password,gender,favcol)
        return jsonify({
            "status":"success",
            "message": f"User {data['name']} added successfully",
            "user": {
                "name": name,
                "email": email,
                "gender": gender,
                "favcol": favcol
            }
        }), 201
    except ValueError as e:
        return jsonify({"status":"error", "message":str(e)}), 400
 
        """
@users_bp.route("/delete", methods=["DELETE"])
@require_api_key
def delete():
    data = request.json

    user_row = get_user_by_email(data["email"])
    if user_row is None:
        return jsonify({"status":"error", "message":f"Email '{data['email']}' does not exist"}), 400
    
    email = user_row["email"]
    delete_user(email)

    # skip password in the returned json
    return jsonify({
        "status":"success",
        "message": f"User {email} has been deleted successfully"
    }), 200
"""