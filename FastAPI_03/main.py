from fastapi import FastAPI, HTTPException, status
from Models import Curso
app = FastAPI()

cursos = {
    1:{
        "titulo": "Termodinamica",
        "aulas": 64,
        "horas":60

    },
    2:{
        "Titulo": "PPQ",
        "aulas": 30,
        "horas": 60
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found')

@app.post('/cursos')
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        cursos[curso.id] = Curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Já existe um curso com esse id: {curso.id}')

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id:int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não existe')


@app.delete('/cursos/{curso_id}')
async def del_curso(curso_id:int):
    if curso_id in cursos:
        del cursos[curso_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não localizado')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)
