from pydantic import BaseModel, Field
from typing import Optional

#Esquema 
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5,max_length=15)
    overview: str
    year: int = Field(ge=1990,le=2022)
    rating: float
    category: str

#Para los datos por defetas la clase de debe llamar Config
    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "title": "mi pelicula",
                "overview": "Descripcion de la pelicula ",
                "year":2022,
                "rating":9.8,        
                "category": "Accion"      
            }
        }
