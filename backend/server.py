from fastapi import FastAPI, HTTPException
from auth import login_user, register_user
from schemas import UserLogin, UserRegister

app = FastAPI(title="Freelance Platform API")


@app.post("/register")
def register(user: UserRegister):
    result = register_user(
        username=user.username,
        password=user.password,
        email=user.email,
        role=user.role,
        address=user.address
    )

    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])

    return result


@app.post("/login")
def login(user: UserLogin):
    result = login_user(
        username=user.username,
        password=user.password
    )

    if result["status"] == "error":
            raise HTTPException(status_code=400, detail=result["message"])
    
    return result
