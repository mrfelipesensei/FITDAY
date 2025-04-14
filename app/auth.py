import json
import os

def login_user():
    username = input("Digite o nome de usuário: ")
    password = input("Digite sua senha: ")

    if not os.path.exists("users.json"):
        print("Nenhum usuário cadastrado ainda. Por favor, cadastre-se.")
        return

    
    with open("users.json","r") as f:
        users = json.load(f)

    if username not in users:
        print("Usuário inexistente. Por favor, cadastre-se.")
    elif users[username] != password:
        print("Senha incorreta.")
    else:
        print("Login bem-sucedido. Bem-vindo {}!".format(username))


def register_user():
    username = input("Digite o nome de usuário: ")
    password = input("Digite sua senha: ")

    if not os.path.exists("users.json"):
        with open("users.json","w") as f:
            json.dump({},f)
        
    with open("users.json","r") as f:
        users = json.load(f)
    
    if username in users:
        print("Usuário já cadastrado.")
    else:
        users[username] = password
        with open("users.json","w") as f:
            json.dump(users,f)
        print("Cadastro realizado com sucesso.")

def registrar_treino():
    if os.path.exists("treinos.json"):
        with open("treinos.json","r") as f:
            treinos = json.load(f)
    else:
        treinos = {}
        

'''Função registrar_treino(usuario):
    Tentar abrir o arquivo "treinos.json" para leitura
        Se o arquivo existir:
            Carregar os dados do JSON em uma variável chamada "treinos"
        Se o arquivo não existir:
            Criar uma variável "treinos" como dicionário vazio

    Obter a data atual no formato "YYYY-MM-DD"

    Solicitar ao usuário:
        - Grupo muscular
        - Nome do exercício
        - Peso (converter para float)
        - Repetições (converter para int)

    Criar um dicionário com os dados do treino:
        {
            "data": data_atual,
            "grupo_muscular": valor digitado,
            "exercicio": valor digitado,
            "peso": valor digitado,
            "repeticoes": valor digitado
        }

    Se o nome de usuário estiver em "treinos":
        Adicionar o novo treino à lista do usuário com .append()
    Senão:
        Criar uma nova lista com esse treino como primeiro item e associar ao usuário

    Abrir o arquivo "treinos.json" para escrita
        Salvar os dados atualizados com json.dump()

    Exibir mensagem: "Treino registrado com sucesso!"
'''