from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model import consulta_alunos, consultar_id, add_aluno, update_aluno


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"context":consulta_alunos()})
    
@app.get("/edit/{id}")
async def editar(id: int, request: Request):
    aluno = consultar_id(id)
    return templates.TemplateResponse(
        request=request,
        name="edit.html",
        context={"aluno": aluno}
    )

@app.get("/view/{id}")
async def visualizar(id: int, request: Request):
    aluno = consultar_id(id)
    
    return templates.TemplateResponse(
        request=request,
        name="view.html",
        context={"aluno": aluno}
    )

@app.post("/add")
async def adicionar(request: Request):
    form = await request.form()

    nome = form.get("nome")
    email = form.get("email")
    curso_id = int(form.get("curso_id"))
    
    add_aluno(nome, email, curso_id) 

    return RedirectResponse(url="/", status_code=303)

@app.post("/update/{id}")
async def atualizar(id: int, request: Request):
    form = await request.form()

    nome = form.get("nome")
    email = form.get("email")
    curso_id = int(form.get("curso_id"))

    update_aluno(id, nome, email, curso_id)

    return RedirectResponse(url="/", status_code=303)


# ve o que esta pedindo no notion e destingua a funçao de cada um no git hub
# agora vai precisar integrar o banco de dados com o python, criar tabelas