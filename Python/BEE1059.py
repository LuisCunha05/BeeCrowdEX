#Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

print('\n'.join([str(num) for num in range(2, 101, 2)]))