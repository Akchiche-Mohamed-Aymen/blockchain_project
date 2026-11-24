from backend.db_connection import cursor , db

def add_project(title, description, budget, client_id):
    query = "INSERT INTO projects (title, description, budget, client_id) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(query, (title, description, budget, client_id))
        db.commit()
        return {
            "status": "success",
            "message": "Project added successfully",
            "project_id": cursor.lastrowid
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error adding project: {e}"
        }