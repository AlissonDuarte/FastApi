from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def mensagem():
    return {"msg": "FastAPI response"}


#comando: uvicorn FastAPI:app
"""Abre uma pagina no servidor uvicorn rodando o código"""

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)

#gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

"""Cria quatro servidores para trabalharem como cluster
-w: comando que cria o servidor, seguido da quantidade
-k se refere a classe de desempenho
"""