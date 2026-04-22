<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI(title="Sistema Faculdade API")

# "Banco" em memória
=======
>>>>>>> 34152862fc04255e2af29f6b53e70a9774cb9cf9
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

<<<<<<< HEAD
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
=======
def gerar_matricula(sigla):
    contadores_cursos[sigla] += 1
    return f"{sigla}{contadores_cursos[sigla]}"

def criar_aluno():
    print("\n--- Novo Cadastro ---")
    nome = input("Qual o nome do aluno? ")
    email = input("E o e-mail? ")
    
    print(f"Cursos: {', '.join(nomes_cursos.keys())}")
    sigla = input("Qual a sigla do curso? ").upper()
    
    if sigla in contadores_cursos:
        matricula = gerar_matricula(sigla)
        aluno = {
            "nome": nome,
            "email": email,
            "curso": nomes_cursos[sigla],
            "matricula": matricula
        }
        alunos.append(aluno)
        print(f"\nPronto! O aluno foi cadastrado com a matrícula: {matricula}")
    else:
        print("\nOps, esse curso não existe por aqui. Tente de novo!")

def listar_alunos():
    print("\n--- Alunos Cadastrados ---")
    if not alunos:
        print("Ainda não temos nenhum aluno na lista.")
    else:
        for a in alunos:
            print(f"[{a['matricula']}] {a['nome']} - {a['curso']} ({a['email']})")

def atualizar_aluno():
    print("\n--- Atualizar Dados ---")
    mat = input("Digite a matrícula de quem você quer alterar: ").upper()
    
    for a in alunos:
        if a['matricula'] == mat:
            print(f"Alterando dados de: {a['nome']}")
            a['nome'] = input("Novo nome: ")
            a['email'] = input("Novo e-mail: ")
            print("Feito! Os dados foram atualizados.")
            return
    print("Não encontrei ninguém com essa matrícula.")

def excluir_aluno():
    print("\n--- Remover Aluno ---")
    mat = input("Digite a matrícula de quem deseja remover: ").upper()
    
    for a in alunos:
        if a['matricula'] == mat:
            alunos.remove(a)
            print("O aluno foi removido com sucesso.")
            return
    print("Não achei essa matrícula no sistema.")

def menu():
    while True:
        print("\n--- GESTÃO ACADÊMICA ---")
        print("1. Cadastrar aluno")
        print("2. Ver todos os alunos")
        print("3. Editar um aluno")
        print("4. Remover um aluno")
        print("5. Sair")
        
        opcao = input("\nO que deseja fazer? ")
        
        if opcao == '1': criar_aluno()
        elif opcao == '2': listar_alunos()
        elif opcao == '3': atualizar_aluno()
        elif opcao == '4': excluir_aluno()
        elif opcao == '5': 
            print("Até logo! Fechando o sistema...")
            break
        else:
            print("Essa opção não é válida, escolha de 1 a 5.")

if __name__ == "__main__":
    menu()
>>>>>>> 34152862fc04255e2af29f6b53e70a9774cb9cf9
