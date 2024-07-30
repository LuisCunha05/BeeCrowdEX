#Iniciamente, há uma string vazia. Seu programa deve realizar dois tipos de instruções:
#
#Adicionar um caractere entre 'a' e 'z' ao final da string.
#Calcular quantas substrings diferentes a string possui.
#Por exemplo, a string "aba" possui 5 substrings diferentes: "a", "ab", "aba", "b", "ba".
#
#Entrada
#A entrada é composta por vários casos de teste. Cada caso de teste consiste de uma linha contendo uma sequência com até 2.105 caracteres. 
# Cada caractere representa uma instrução que deve ser feita. Um caractere entre 'a' e 'z' indica que deve ser realizado uma instrução do tipo 
# 1 com esse caractere. Um caractere '?' representa uma instrução do tipo 2.


def subAmount( val: str) -> int:
    save = []
    val = val.replace('?', '')
    for idx in range(1, len(val) + 1):
        save.append(val[:idx])
    return save

opa = input()

for item in subAmount(opa):
    print(item)