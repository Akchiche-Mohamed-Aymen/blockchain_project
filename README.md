# Install the App
```bash
git clone https://github.com/Akchiche-Mohamed-Aymen/blockchain_project.git
```
# Go to the project 
```bash
cd blockchain_project
```
# Go to the backend folder
```bash
cd backend
```
# Install the required packages
```bash
pip install -r requirements.txt
```

# Start the Server

```bash
uvicorn server:app --reload
```

Open `http://127.0.0.1:8000/docs` in the browser to use the API documentation.

# Register API

**Endpoint:** `POST /register`

**Request body:**

```json
{
  "username": "my_username",
  "password": "Password123",
  "email": "user@example.com",
  "role": "client"
  }
```

`role` must be  `client`, or `freelancer`. The username must contain 4 to 50 letters, numbers, or underscores. The password must contain 8 to 128 characters, including uppercase, lowercase, and numeric characters.




# Login API

**Endpoint:** `POST /login`

**Request body:**

```json
{
  "username": "my_username",
  "password": "Password123"
}
```
The username must contain 4 to 50 letters, numbers, or underscores. The password must contain 8 to 128 characters, including uppercase, lowercase, and numeric characters.