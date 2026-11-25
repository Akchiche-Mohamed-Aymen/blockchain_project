import json
import uuid
users = json.loads(open("./data/users.json").read())
def login_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
        return {
        "user_id" : user["user_id"],
        "status": "success",
        "message": "User registered successfully"
    }
   
    return {
            "status": "error",
            "message": "Invalid username or password"
        }
def register_user(username, password, email ,role,address = "" ):
    # Check if user already exists
    for user in users:
        if user["username"] == username:
            return {
                "status": "error",
                "message": "Username already exists"
            }
        if role not in ["freelancer", "client" , "admin"]:
            return {
                "status": "error",
                "message": "Invalid role."
            }
    user_id = str(uuid.uuid4())
    new_user = {
        "user_id": user_id,
        "username": username,
        "password": password,
        "email": email,
        "role": role,
        "address": address
    }
    users.append(new_user)
    with open("./data/users.json", "w" , encoding="utf-8") as f:
        json.dump(users, f , indent=4)

    return {
        "user_id" : user_id,
        "status": "success",
        "message": "User registered successfully"
    }
       
#uvicorn server:app --reload
