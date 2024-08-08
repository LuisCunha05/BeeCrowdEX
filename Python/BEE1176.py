#A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste.
#  Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo
#  da série de Fibonacci.
fibo = [ 0,1]
for n in range(2, 61):
    fibo.append(fibo[n-2]+fibo[n-1])


n = int(input())
for i in range(n):
    entrada = int(input())
    print(f'Fib({entrada}) = {fibo[entrada]}')

