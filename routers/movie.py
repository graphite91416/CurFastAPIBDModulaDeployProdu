from  fastapi import APIRouter
from fastapi import Path, Query,Depends
# Esta clase se utiliza para enviar la respuesta en html
from fastapi.responses import JSONResponse
#Esta libreria nos ayuda a validar datos 





from typing import List



from fastapi.encoders import jsonable_encoder
# base de datos
from config.database import Session
from models.movie import Movie as MovieModel
#Manejo de errores
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()


#Ruta pasandole un parameto para filtro
#Validando el parametro id
'''
@app.get('/movies/{id}', tags=['movies'])
def get_movies_parametro(id: int):

    for item in movies:
        if item['id']==id:

            return item

    return "No encontro la pelicula"

'''

@movie_router.get('/movi/{id}', tags=['movs'])
def get_movies_parametro(id: int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'mesaje': "No encontro registro"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    
#Ruta pasandole un Query para filtro
#sin validacion de query
'''
@app.get('/movies/',tags=['movies'])
def get_movies_by_query(category: str):

    for peli in movies:
        if peli['category']==category:
            return peli
    return "No se encontro pelicula"

'''    
#Validacion de query
@movie_router.get('/movies/',tags=['movies'])
def get_movies_by_query(category: str = Query(min_length=5,max_length=15)):

    db = Session()
    result = MovieService(db).get_movie_category(category)
    if not result:
        return JSONResponse(status_code=404,content={'mesaje': "No se encontro registo con esa categoria"})
    else:
        return JSONResponse(status_code=200,content=jsonable_encoder(result))

'''
Clase 8/19
Metodo POST con clase de esquema
'''

@movie_router.post('/movies',tags=['movies'])
def create_movie(movie: Movie):
    # se crea una secion de la base de dato
    db = Session()
    MovieService(db).create_movie(movie)

    return "movies"


'''

@app.post('/movies',tags=['movies'])
def create_movie(id: int = Body(),title: str = Body(),overview: str = Body(),year: int = Body(),year: float = Body(),category: str = Body()):
    movies.append({
        "id":id,
        "title": title,
        "overview": "overview,
        "year":year,
        "rating":rating,        
        "category": category 
    })

    return movies

'''

#Eliminar datos por id
@movie_router.delete('/movies/{id}',tags=['movies'])
def delete_movie(id: int):
    db =Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'mesaje': "No encontro la pelicula"})
    else:
        MovieService(db).delete_movie(id)

#Actualizar datos
@movie_router.put('/movies/{id}',tags=['movies'])
def put_monies(id: int, movie: Movie):
    db =Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'mesaje': "No encontro la pelicula"})
    else:
        MovieService(db).update_movie(id,movie)
# Utilizando la clase JSONResponse
# response_model se utiliza para especificar que dipode datos se va devolver
@movie_router.get('/mov',tags=['movies'],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer)])
def get_movies()-> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse (status_code=200, content=jsonable_encoder(result)) 

@movie_router.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWTBearer)])
def get_movies()-> List[Movie]:
    return JSONResponse (status_code=200, content="movies")