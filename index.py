import menu

def operate():
    while True:
        menu.display_menu()
        op = menu.get_user_input()
        if op == "0":
            return
        num = input('Digite um número: ')
        menu.perform_conversion(op, num)

def main():
    print("Projeto Calculadora Interativa -> Decimal | Binário | Octal | Hexa")
    operate()
    print("------------------------------------------------------------------")
    print("Obrigado por Utilizar Nossa Calculadora Conversora")
    print("------------------------------------------------------------------")

if __name__ == "__main__":
    main()
