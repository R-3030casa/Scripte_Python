'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
'''numero =list()
for c in range(0,5):
    n = (int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        numero.append(n)
    elif n > numero[len(numero)-1]:
        numero.append(n)
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
                numero.insert(pos,n)
                break
            pos += 1
print('=-='*30)
print(f'Os valores digitados em ordem foram = {numero}.')
print('=-='*30)'''
# encurtando o código
numero =list()
for c in range(0,5):
    n = (int(input(f'Digite o {c+1}º número: ')))
    if c == 0 or n > numero[-1]:
        numero.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
                numero.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('=-='*30)
print(f'Os valores digitados em ordem foram = {numero}.')
print('=-='*30)