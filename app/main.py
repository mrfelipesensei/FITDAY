from auth import login_user, register_user, registrar_treino

def main():
    while True:
        print("\n === FITDAY ===")
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            username = login_user() #Armazena o username retornado
            if username: #Só chama o menu de usuário se o login for bem-sucesido
                menu_usuario(username)
        elif opt == "2":
            register_user()
        elif opt == "3":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario(username):
    while True:
        print("\n=== MENU DO USUÁRIO ===")
        print("1. Registrar Treino")
        print("2. Ver Meus Treinos")
        print("3. Sair")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            registrar_treino(username)
        elif opt == "2":
            print("Aqui você verá Seus Treinos")
        elif opt == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()