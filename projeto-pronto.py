print ("\033[7;34;40mKAINAN GUERRA SILVA - CIENCIA DA COMPUTAÇÃO - UNICSUL SÃO MIGUEL\033[m")
print ("\033[4;30;44mTrabalho Programação de Computadores e Organização e Arquiterura\033[m")
print ("Projeto Calculadora Interativa -> decimal | binário | octal | hexa")
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
if op == 1:
        n1 = input('Digite um número inteiro: ')
        print ("------------------------------------------------------------------")
        n1 = n1.replace(" ", "")
        inteiro = int(n1)
        bi = ''
        while inteiro > 0:
            bi = str(inteiro % 2) + bi
            inteiro = inteiro // 2
        print (f'O numéro decimal {n1} em binario é igual a: {bi}')

elif op == 2:
        bi = input ("digite um número binário: ")
        print ("------------------------------------------------------------------")
        bi = bi.replace(" ", "")
        
        n = len(bi)-1
        soma = 0
        for digito in bi:
            soma = soma + int (digito)*2**n
            n = n-1
        print (f'O número binario {bi} é igual a {soma} em decimal') 

elif op == 3:
        ni = input('Digite um número inteiro: ')
        print ("------------------------------------------------------------------")
        ni = ni.replace(" ", "")
        
        inteiro = int(ni)
        octa = ''
        while (inteiro > 0):
            octa = str(inteiro % 8) + octa
            inteiro = inteiro//8
        print (f'O numéro decimal {ni} em octal é igual a: {octa}')

elif op == 4:
            oct = input ("Digite um número octal: ")
            print ("------------------------------------------------------------------")
            oct = oct.replace(" ", "")
            
            n = len(oct)-1
            decimal = 0
            for d in oct:
                decimal = decimal + int (d)*8**n
                n = n-1
            print (f'O numero octal {oct} em decimal é igual a: {decimal}') 
elif op == 5:
        conversao = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
        
        num = input('Digite um número inteiro: ')
        print ("------------------------------------------------------------------")
        num = num.replace(" ", "")

        inteiro = int(num)
        hexa = ''
        while(inteiro>0):
            resto = inteiro%16
            hexa = conversao[resto]+ hexa
            inteiro = inteiro//16          
        print(f"O número decimal {num} em hexadecimal é igual a: ",hexa)

elif op== 6:
        conversao = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15} 
  
        hex = input("Digite um número hexadecimal: ").upper()
        hex = hex.replace(" ", "")
        print ("------------------------------------------------------------------")

        dec = 0
        n = len(hex) -1
        for d in hex:
            dec = dec + conversao[d]*16**n
            n = n - 1
        print(f"O número hexadecimal {hex} em decimal é igual a:", dec)

else: 
    print ("Comando Incorreto")