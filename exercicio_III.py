print('====================================')
print('Informe uma das opções abaixo:')
print('1 - Verificador de número par ou ímpar')
print('2 - Verificador idade')
numero = int(input('Digite a sua opção: '))
seleciona_opcao(numero)
print('====================================')

def seleciona_opcao(numero):
    if numero == 1:
        verificador_numero()
    elif numero == 2:
        verificador_idade()
    else:
        print('Opção inválida')

def verificador_numero():
    if (numero%2 == 0):
        print('O número ' + str(numero) + ' é par')
    else:
        print('O número ' + str(numero) + ' é ímpar')

def verificador_idade():
    if(idade >= 0 and idade <= 12):
        print('Você é uma criança')
    elif(idade>= 13 and idade <=18):
        print('Você é um adolescente')
    else:
        print('Você é um adulto')
print('====================================')

