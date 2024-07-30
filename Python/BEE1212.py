#As crianças são ensinadas a adicionar vários dígitos da direita para a esquerda, um dígito de cada vez. Muitos acham a operação "vai 1" (em inglês chamada de "carry",
# na qual o valor 1 é carregado de uma posição para ser adicionado ao dígito seguinte) um desafio significativo. Seu trabalho é para contar o número de operações de carry
# para cada um dos problemas de adição apresentados para que os educadores possam avaliar a sua dificuldade.

a , b = map(int, input().split(' '))

while(not(a == 0 and b == 0)):
    

    carryCount = 0
    lastA = 0
    lastB = 0
    carry = 0

    while(not(a == 0 and b == 0)):
        
        lastA = a % 10
        lastB = b % 10
        a //= 10
        b //= 10

        if(lastA + lastB + carry >= 10):
            carry = 1
            carryCount += 1
        else:
            carry = 0
    if(carryCount == 0):
        print('No carry operation.')
    elif(carryCount == 1):
        print(f'1 carry operation.')
    else:
        print(f'{carryCount} carry operations.')
    a , b = map(int, input().split(' '))
