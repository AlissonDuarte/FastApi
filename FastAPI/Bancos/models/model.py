from Bancos.core.configs import settings
from sqlalchemy import Column, Integer, String

class model(settings.DBBaseModel):
    __tablename__='pacientes'
    id: Column(Integer, primary_key=True, autoincrement=True)
    Nome: str=Column(String(100))
    idade: str=Column(String(10))
    cpf:str =Column(String(11))


    
