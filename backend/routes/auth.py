from fastapi import APIRouter, HTTPException, Depends
from auth import authenticate_user, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags = ["authentication"]
)

@router.post('/token')
def authenticate_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not (authenticate_user(username=form_data.username, password=form_data.password)):
        raise HTTPException(
            status_code=401,
            detail="Non authorized user."
        )
    else:
        token = create_access_token(data={"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}


    
