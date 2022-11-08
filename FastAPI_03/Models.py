from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int]=None
    titulo: str
    aula: int
    horas: int
