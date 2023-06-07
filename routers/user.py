from fastapi import APIRouter
# Esta clase se utiliza para enviar la respuesta en html
from fastapi.responses import  JSONResponse
#Esta libreria nos ayuda a validar datos 

from utils.jwt_manager import create_token

from schemas.user import User

# metodo de router


user_router = APIRouter()

#Ruta
#Se añada una nueva etiqueta 'Home' con tags, antes estaba 'dafault'




@user_router.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = str = create_token(user.dict())
        return JSONResponse(status_code=200,content= token)