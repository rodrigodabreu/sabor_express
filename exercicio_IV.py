numeros_um_a_dez = [1,2,3,4,5,6,7,8,9,10]

lista_nomes = ['Rodrigo', 'João', 'Maria', 'José', 'Ana', 'Paulo', 'Pedro', 'Marcos', 'Carlos', 'Lucas']

lista_ano = [1986, 2024]

soma = 0

#2) Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
for numero in numeros_um_a_dez:
 if numero % 2 != 0:
   soma += numero
print(f'A soma dos números ímpares de 1 a 10 é: {soma}\n')

#3)Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
numeros_um_a_dez.reverse()
for numero in numeros_um_a_dez:
    print(numero)

# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
# Utilize um bloco try-except para lidar com possíveis exceções.

# Criando a lista de números
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

try:
    soma = 0
    for numero in numeros:
        soma += numero
    print(f"A soma dos números é: {soma}")
except TypeError:
    print("A lista contém elementos que não são números")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


# Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [1,2,3]
media = 0
try: 
    media = sum(numeros) / len(numeros)
    print(f"A média dos números é: {media}")
except ZeroDivisionError:
    print("A lista está vazia")
except Exception as e:
    print(f"Ocorreu um erro: {e}")