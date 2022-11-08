from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    idade:str
    cpf:str

