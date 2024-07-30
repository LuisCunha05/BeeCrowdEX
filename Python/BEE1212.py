#As crianças são ensinadas a adicionar vários dígitos da direita para a esquerda, um dígito de cada vez. Muitos acham a operação "vai 1" (em inglês chamada de "carry",
# na qual o valor 1 é carregado de uma posição para ser adicionado ao dígito seguinte) um desafio significativo. Seu trabalho é para contar o número de operações de carry
# para cada um dos problemas de adição apresentados para que os educadores possam avaliar a sua dificuldade.

a = b = ''

while(a != 0 and b != 0):
    a , b = map(int, input().split(' '))

    print(a, b)

