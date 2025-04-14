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