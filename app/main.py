from auth import login_user, register_user

def main():
    while True:
        print("\n === FITDAY ===")
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            login_user()
        elif opt == "2":
            register_user()
        elif opt == "3":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()