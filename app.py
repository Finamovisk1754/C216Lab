from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI(title="Sistema Faculdade API")

# "Banco" em memória
alunos = []
contadores_cursos = {"GEC": 0, "GEA": 0, "GEB": 0, "GET": 0, "GES": 0, "GEE": 0, "GEP": 0}

nomes_cursos = {
    "GEC": "Engenharia de Computação",
    "GEA": "Engenharia de Controle e Automação",
    "GEB": "Engenharia Biomédica",
    "GET": "Engenharia de Telecomunicações",
    "GES": "Engenharia de Software",
    "GEE": "Engenharia Elétrica",
    "GEP": "Engenharia de Produção"
}

class AlunoIn(BaseModel):
    nome: str
    email: EmailStr
    curso: str  # sigla (ex: GEC)

class AlunoOut(BaseModel):
    nome: str
    email: EmailStr
    curso: str  # nome completo
    matricula: str

def gerar_matricula(sigla: str) -> str:
    contadores_cursos[sigla] += 1
    return f"{sigla}{contadores_cursos[sigla]:03d}"

# CREATE
@app.post("/alunos", response_model=AlunoOut, status_code=201)
def criar_aluno(aluno: AlunoIn):
    if aluno.curso not in contadores_cursos:
        raise HTTPException(status_code=400, detail="Curso inválido")

    # evita e-mail duplicado
    if any(a["email"] == aluno.email for a in alunos):
        raise HTTPException(status_code=409, detail="E-mail já cadastrado")

    matricula = gerar_matricula(aluno.curso)
    novo = {
        "nome": aluno.nome,
        "email": aluno.email,
        "curso": nomes_cursos[aluno.curso],
        "matricula": matricula
    }
    alunos.append(novo)
    return novo

# READ (lista)
@app.get("/alunos", response_model=List[AlunoOut])
def listar_alunos():
    return alunos

# READ (por matrícula)
@app.get("/alunos/{matricula}", response_model=AlunoOut)
def obter_aluno(matricula: str):
    for a in alunos:
        if a["matricula"] == matricula:
            return a
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

# UPDATE (parcial)
@app.put("/alunos/{matricula}", response_model=AlunoOut)
def atualizar_aluno(matricula: str, aluno: AlunoIn):
    for a in alunos:
        if a["matricula"] == matricula:
            a["nome"] = aluno.nome
            a["email"] = aluno.email
            # curso não altera matrícula; opcionalmente permitir troca:
            if aluno.curso in nomes_cursos:
                a["curso"] = nomes_cursos[aluno.curso]
            return a
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

# DELETE
@app.delete("/alunos/{matricula}")
def deletar_aluno(matricula: str):
    for a in alunos:
        if a["matricula"] == matricula:
            alunos.remove(a)
            return {"msg": "Removido"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado")