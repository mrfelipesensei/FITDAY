import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

def login_user():
    username = input("Digite o nome de usuário: ").strip().lower()
    password = input("Digite sua senha: ").strip().lower()

    '''print("Caminho atual: ",os.getcwd())
    print("Existe users.json?",os.path.exists("users.json"))'''

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
        opt = input("Treino de hoje já registrado. Gostaria de registrar outro? (s/n)")
        if opt != "s":
            print("Processo encerrado.")
            return
            
    
    try:
        qtd_exercicios = int(input("Quantos exercícios você irá registrar? "))
    except ValueError:
        print("Quantidade de Exercícios deve ser um número inteiro.")
        return

    treinos_do_dia = []

    for i in range(qtd_exercicios):
        print(f"\nExercício {i+1} de {qtd_exercicios}")
        grupo_muscular = input("Digite o Grupo Muscular: ").strip().lower()
        nome_exercicio = input("Digite o Nome do Exercício: ").strip().lower()
        try:
            carga = float(input("Digite o Valor da Carga: "))
            repeticoes = int(input("Digite o Número de Repetições: "))
        except ValueError:
            print("Entrada inválida! Carga e repetições devem ser números.")
            continue

    
        treino = {
            "data" : data_hoje,
            "grupo_muscular" : grupo_muscular,
            "nome_exercicio" : nome_exercicio,
            "carga" : carga,
            "repeticoes" : repeticoes
        }

    #Adiciona treino à lista treinos_do_dia
    treinos_do_dia.append(treino)

    #Armazenando o treino
    if username in treinos:
        treinos[username].extend(treinos_do_dia) #adiciona todos
    else:
        treinos[username] = treinos_do_dia

    #Salvando os dados de treino no arquivo
    with open("treinos.json","w") as f:
        json.dump(treinos,f,indent=4)

    print(f"\n{len(treinos_do_dia)} exercícios(s) registrado(s) com sucesso!")

def ver_treinos_por_data(username):
    if os.path.exists("treinos.json"):
        with open("treinos.json","r") as f:
            treinos = json.load(f)
    else:
        print("Nenhum treino registrado.")
        return
    
    select_data = input("Digite a data desejada (formato: yyyy-mm-dd): ")

    if username not in treinos:
        print("Nenhum treino registrado para esse usuário.")
        return
    
    
    #Filtrar os treinos pela data fornecdia
    treinos_do_usuario = [t for t in treinos[username] if t['data'] == select_data]

    if treinos_do_usuario:
        for treino in treinos_do_usuario:
            print(f"Data: {treino['data']}")
            print(f"Grupo Muscular: {treino['grupo_muscular']}")
            print(f"Nome do Exercício: {treino['nome_exercicio']}")
            print(f"Carfa: {treino['carga']}")
            print(f"Repetições: {treino['repeticoes']}")
            print("-" * 20) #Separador entre os treinos
    else:
        print("Nenhum treino encontrado para essa data.")

def gerar_grafico_frequencia(username):
    if os.path.exists("treinos.json"):
        with open("treinos.json") as f:
            treinos = json.load(f)
    else:
        print("Nenhum treino encontrado")
        return

    if username not in treinos:
        print("Nenhum treino registrado para esse usuário.")
        return
    
    frequencia_por_data = {}

    for treino in treinos[username]:
        data = treino["data"]
        if data in frequencia_por_data:
            frequencia_por_data[data] += 1
        else:
            frequencia_por_data[data] = 1

    #Separar dados
    datas = list(frequencia_por_data.keys())
    frequencias = list(frequencia_por_data.values())

    #Criar o gráfico
    plt.figure(figsize=(10,5))
    plt.bar(datas, frequencias, color='skyblue')
    plt.title("Frequência de Treino por Data")
    plt.xlabel("Data")
    plt.ylabel("Número de Exercícios")
    plt.xticks(rotation=45)
    plt.tight_layout() #Ajusta o layout para não cortar os textos
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    #Mostrar o gráfico
    plt.show()
    