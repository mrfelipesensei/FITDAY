import json
import os
from datetime import datetime

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
        return username #Retorna o username após o login bem-sucedido


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

def registrar_treino(username):
    if os.path.exists("treinos.json"):
        with open("treinos.json","r") as f:
            treinos = json.load(f)
    else:
        treinos = {}

    data_hoje = datetime.today().strftime("%Y-%m-%d")

    if username in treinos and any(t['data'] == data_hoje for t in treinos[username]):
        print("Treino de hoje já registrado.")
        return

    grupo_muscular = input("Digite o Grupo Muscular: ").strip().lower()
    nome_exercicio = input("Digite o Nome do Exercício: ").strip().lower()
    try:
        carga = float(input("Digite o Valor da Carga: "))
        repeticoes = int(input("Digite o Número de Repetições: "))
    except ValueError:
        print("Entrada inválida! Carga e repetições devem ser números.")
        return

    
    treino = {
        "data" : data_hoje,
        "grupo_muscular" : grupo_muscular,
        "nome_exercicio" : nome_exercicio,
        "carga" : carga,
        "repeticoes" : repeticoes
    }

    #Confirmação
    print(f"\n Treino realizado com sucesso!\n{treino}")


    #Armazenando o treino
    if username in treinos:
        treinos[username].append(treino)
    else:
        treinos[username] = [treino]

    #Salvando os dados de treino no arquivo
    with open("treinos.json","w") as f:
        json.dump(treinos,f,indent=4)

    print("Treino registrado com sucesso!")

