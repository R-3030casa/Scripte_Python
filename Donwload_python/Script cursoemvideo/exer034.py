'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10% Para salários inferiores ou iguais, o aumento é de 15%.'''

'''salario = float(input('Digite o salário do funcionário: '))
if salario <= 1250:
    print('Se salário foi corrigdo, seu novo salário é R$',salario + (salario * 15/100))
if salario > 1250:
    print('Se salário foi corrigdo, seu novo salário é R$', salario + (salario * 10/100))'''
# Solução do Guanabara
salario = float(input('Qual é o salario do funcionário: '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar \033[32mR${:.2f}\033[m agora.'.format(salario,novo))