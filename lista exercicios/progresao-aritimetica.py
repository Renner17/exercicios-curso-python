pritermo = int(input('Digite o primeiro termo da PA '))
razao = int(input('Digite a razão da PA '))
termo = pritermo
c = 1
print('Os 10 primeiros termos da PA são: ')
while c <= 10:
    print(f'{termo} -> ', end= '')
    termo += razao
    c += 1
print('FIM')