#Entrada
#A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

#Saída
#Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

def isPrime(num: int) -> bool:
    if(num & 1):
        for i in range(3, int(num ** 0.5) + 1, 2):
            if(not(num % i)):
                return False
        return True
    else:
        if(num == 2):
            return True
        return False


n = int(input())
for i in range(n):
    entrada = int(input())
    if(isPrime(entrada)):
        print(f'{entrada} eh primo')
    else:
        print(f'{entrada} nao eh primo')