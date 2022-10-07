

print ("Projeto Calculadora Interativa -> Decimal | Binário | Octal | Hexa")
def calc(op):
    if op == 1:
            n1 = input('Digite um número inteiro: ')
            n1.replace(" ", "")
            if (n1.isnumeric() == False):
                print("Digitou algo errado")
                calc(1)
            else:
                inteiro = int(n1)
                bi = ''
                while inteiro > 0:
                    bi = "% s"%(inteiro % 2) + bi
                    inteiro //= 2
                print (f'O numéro decimal {n1} em binario é igual a: {bi}')
        
    elif op == 2:
            bi = input ("digite um número binário: ")
            bi.replace(" ", "")
            if (bi.isnumeric() == False):
                print("Digitou algo errado")
                calc(2)
            elif (bi.find("0") == -1):
                for i in (bi):
                    if (i != "1"):
                        print("Digitou algo errado")
                        calc(2)
                        sair()
            else:
                n = len(bi)-1
                soma = 0
                for digito in bi:
                    soma = soma + int(digito)*2**n
                    n = n-1
                print (f'O binario {bi} é igual a {soma} em decimal') 
                
                
    elif op == 3:
            ni = input('Digite um número inteiro: ')
            ni.replace(" ", "")
            if (ni.isnumeric() == False):
                    print("Digitou algo errado")
                    calc(3)
                    sair()
                    exit()
            else:
                inteiro = int(ni)
                octa = ''
                while (inteiro > 0):
                    octa = "%s"%(inteiro % 8) + octa
                    inteiro = inteiro//8
                print (f'O numéro decimal {ni} em octal é igual a: {octa}')

    elif op == 4:
                oct = input ("digite um número octal: ")
                oct.replace(" ", "")
                if (oct.isnumeric() == False):
                    print("Digitou algo errado")
                    calc(4)
                    sair()
                    exit()
                else:
                    n = len(oct)-1
                    decimal = 0
                    for d in oct:
                        decimal = decimal + int (d)*8**n
                        n = n-1
                    print (f'O numero octal {oct} em decimal é igual a: {decimal}') 
    elif op == 5:
            str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

            num = input('Digite um número inteiro: ')
            num.replace(" ", "")
            if (num.isnumeric() == False):
                    print("Digitou algo errado")
                    calc(5)
                    sair()
                    exit()
            else:
                inteiro = int(num)
                hexa = ''
                while(inteiro>0):
                    resto = inteiro%16
                    hexa = str[resto]+ hexa
                    inteiro = inteiro//16
                print(f"O numero decimal {num} em hexadecimal é igual a: ",hexa)

    elif op== 6:
            conversao = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            
            hex = input("digite o numero hexadecimal: ").upper()
            hex.replace(" ", "")

            dec = 0
            length = len(hex) -1
            
            for d in hex:
                dec = dec + conversao[d]*16**length
                length = length - 1
            print(f"O número hexadecimal {hex} em decimal é igual a:",dec)

    else: 
        print ("Comando Incorreto")
        operate()
def sair():
    print ("------------------------------------------------------------------")
    dec = input("[0] -> Sair\n[1] -> Voltar ao Menu\nDigite: ")
    if (dec == "0"):
        print ("------------------------------------------------------------------")
        print ("Obrigado por Utilizar Nossa Calculadora Conversora")
        print ("------------------------------------------------------------------")
        exit()
    elif (dec == "1"):
        operate()
    else:
        sair()
        exit()
        
def operate():
    print ("------------------------------------------------------------------")
    print ("[1] -> decimal para binário")
    print ("[2] -> binario para decimal")
    print ("[3] -> decimal para octal")
    print ("[4] -> octal para decimal")
    print ("[5] -> decimal para hexa")
    print ("[6] -> hexa para decimal")
    print ("------------------------------------------------------------------")
    op = int( input ("Digite a operação que será realizada: "))
    print ("------------------------------------------------------------------")
    calc(op)
    sair()
    
operate()
