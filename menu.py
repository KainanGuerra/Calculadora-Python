import conversoes

conversion_functions = {
    '1': conversoes.decimal_para_binario,
    '2': conversoes.binario_para_decimal,
    '3': conversoes.decimal_para_octal,
    '4': conversoes.octal_para_decimal,
    '5': conversoes.decimal_para_hexadecimal,
    '6': conversoes.hexadecimal_para_decimal
}

def perform_conversion(op, num):
    conversion_function = conversion_functions.get(op)
    if conversion_function:
        resultado = conversion_function(num)
        if resultado is not None:
            print(f'O resultado da conversão é: {resultado}')
        else:
            print("Entrada inválida. Por favor, verifique seu número.")
    else:
        print("Opção inválida.")

def display_menu():
    print("------------------------------------------------------------------")
    print("[1] -> Decimal para binário")
    print("[2] -> Binário para decimal")
    print("[3] -> Decimal para octal")
    print("[4] -> Octal para decimal")
    print("[5] -> Decimal para hexadecimal")
    print("[6] -> Hexadecimal para decimal")
    print("[0] -> Sair")
    print("------------------------------------------------------------------")

def get_user_input():
    op = input("Digite a operação que será realizada: ")
    return op

