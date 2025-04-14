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

        data_hoje = datetime.today().strftime("%Y-%m-%d")

        if data_hoje in treinos:
            print("Treino de hoje já registrado.")
        else:
            grupo_muscular = input("Digite o Grupo Muscular: ")
            nome_exercicio = input("Digite o Nome do Exercício: ")
            carga = float(input("Digite o Valor da Carga: "))
            repeticoes = int(input("Digite o Número de Repetições: "))

            treino = {
                "data" : data_hoje,
                "grupo_muscular" : grupo_muscular,
                "nome_exercicio" : nome_exercicio,
                "carga" : carga,
                "repeticoes" : repeticoes
            }

            #Adiciona esse treino ao dicionário de treinos
            treinos[data_hoje] = treino



'''
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