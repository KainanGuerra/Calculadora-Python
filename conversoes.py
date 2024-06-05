def decimal_para_binario(num):
    if not num.isdigit():
        return None
    inteiro = int(num)
    binario = ''
    while inteiro > 0:
        binario = str(inteiro % 2) + binario
        inteiro //= 2
    return binario

def binario_para_decimal(num):
    num = num.replace(" ", "")
    if not all(digit in '01' for digit in num):
        return None
    
    return sum(int(digit) * 2**i for i, digit in enumerate(num[::-1]))

def decimal_para_octal(num):
    if not num.isdigit():
        return None
    inteiro = int(num)
    octal = ''
    while inteiro > 0:
        octal = str(inteiro % 8) + octal
        inteiro //= 8
    return octal

def octal_para_decimal(num):
    if not num.isdigit():
        return None
    return sum(int(digit) * 8**i for i, digit in enumerate(num[::-1]))

def decimal_para_hexadecimal(num):
    if not num.isdigit():
        return None
    inteiro = int(num)
    hexa = ''
    while inteiro > 0:
        resto = inteiro % 16
        if resto < 10:
            hexa = str(resto) + hexa
        else:
            hexa = chr(65 + resto - 10) + hexa
        inteiro //= 16
    return hexa

def hexadecimal_para_decimal(num):
    hexa = num.upper()
    dec = 0
    length = len(hexa) - 1
    for d in hexa:
        if '0' <= d <= '9':
            dec += int(d) * 16**length
        elif 'A' <= d <= 'F':
            dec += (ord(d) - 55) * 16**length
        else:
            return None
        length -= 1
    return dec
