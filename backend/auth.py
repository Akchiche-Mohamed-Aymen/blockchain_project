from backend.db_connection import cursor , db
def login_user(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    try:
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        return user
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error logging in user: {e} "
        }
def register_user(username, password, email ,role,address ):
    query = "INSERT INTO users (username, password, role, email, address) VALUES (%s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, (username, password, role, email, address))
        db.commit()
        return {
            "status": "success",
            "message": "User registered successfully",
            "user_id": cursor.lastrowid
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error registering user: {e}"
        }
        
#uvicorn server:app --reload
