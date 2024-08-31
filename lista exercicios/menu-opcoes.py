def menu():
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')

def obter_numeros():
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    return n1, n2

def main():
    n1, n2 = obter_numeros()

    while True:
        menu()
        opc = int(input('Qual a sua opção? '))

        if opc == 1:
            print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        elif opc == 2:
            print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        elif opc == 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}')
            elif n2 > n1:
                print(f'{n2} é maior que {n1}')
            else:
                print('Os dois números são iguais')
        elif opc == 4:
            n1, n2 = obter_numeros()  # Permite inserir novos números
        elif opc == 5:
            print('Fim do programa, até a próxima!')
            break  # Sai do loop e termina o programa
        else:
            print('Opção inválida! Tente novamente.')

main()
