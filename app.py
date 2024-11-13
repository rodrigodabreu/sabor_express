#nome da aplicação
print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

print('1. Cadastrar Restaurante')
print('2. Listar Restaurante')
print('3. Ativar Restaurante')
print('4. Sair\n')

# snake_case utilizado para definir nomes de variáveis
opcao_escolhida = int(input('Escolha uma opção: \n')) 
#print('Você escolheu a opção: ',opcao_escolhida)
print(f'Você escolheu a opção: {opcao_escolhida}\n')

#convertendo a string para inteiro
# opcao_escolhida = int(opcao_escolhida)

if opcao_escolhida == 1: 
    print('Cadastrar Restaurante\n')
elif opcao_escolhida == 2:
    print('Listar Restaurante\n')
elif opcao_escolhida == 3:
    print('Ativar Restaurante\n')
else: 
  print('Encerrando o programa\n')