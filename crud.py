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