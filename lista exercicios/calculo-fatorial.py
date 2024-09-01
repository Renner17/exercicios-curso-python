n = int(input('Digite um número para calcular seu fatorial '))
c = n 
f = 1 
print(f'Calculando o fatorial de {n}')
while c > 0:
    f *= c
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1