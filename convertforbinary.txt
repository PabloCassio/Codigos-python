def transf_binario(num):
    quant = 0
    cont = 0
    onesandzeroes = ''
    while num > quant:
        quant = 2 ** cont
        if quant < num:
            cont += 1
        if 2 ** cont > num:
            cont -= 1
            break
    
    binario = []
    result = num
    
    while True:
        if 2 ** cont <= result:
            result -= 2**cont
            binario.append(True)
        else:
            binario.append(False)
        cont -= 1
        if cont < 0 :
            break
        if result == 0:
            if num % 2 == 0:
                binario.append(False)
            
            for nums in range(cont):
                binario.append(False)
            break
    print(binario)
    for ele in binario:
        if ele == True:
            onesandzeroes += '1'
        else:
            onesandzeroes += '0'
    return onesandzeroes        

while True:        
    try:
        num = int(input('Digite um número inteiro na base decimal: '))
        print(f"O valor de {num} em binário é: {transf_binario(num)}")
    except ValueError:
        print('VERIFIQUE O VALOR DIGITADO')
