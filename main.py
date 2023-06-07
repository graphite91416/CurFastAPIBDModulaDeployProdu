
from fastapi import FastAPI
# Esta clase se utiliza para enviar la respuesta en html
from fastapi.responses import HTMLResponse
# base de datos
from config.database import engine, Base
#Manejo de errores
from middlewares.error_handler import ErrorHandler 
# metodo de router
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()

#Cambia el titulo de la documentacion antes estaba 'FastAPI'
app.title ='Mi aplicacion'
#Cambia la version de la documentacion antes estaba '0.1.0'
app.version = '0.1.1'

#Llamada a middlewares

app.add_middleware(ErrorHandler)

#llamar a el router
app.include_router(movie_router)
app.include_router(user_router)

#inicializacion de la base de dato

Base.metadata.create_all (bind=engine)



movies = [
    {
        "id":1,
        "title": "Avatar",
        "overview": "Em un exuberante planeta llamado Pandora viven ",
        "year":2009,
        "rating":7.8,        
        "category": "Accion"        
    },
    {
        "id":2,
        "title": "Rambo",
        "overview": "Batalla en la selva",
        "year":1982,
        "rating":9,        
        "category": "Accion"        
    },
    {
        "id":3,
        "title": "Toy Story",
        "overview": "Historia de jugetes en una casa",
        "year":1995,
        "rating":8.5,        
        "category": "Animada"        
    }

]



@app.get('/', tags=['home'])
def  message():
    return HTMLResponse('<h1>hello world!</h1>')