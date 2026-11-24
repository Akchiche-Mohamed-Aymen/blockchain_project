import mysql.connector 
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="freelance"
    )
    

    cursor = db.cursor()
    print("Connected to MySQL database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")