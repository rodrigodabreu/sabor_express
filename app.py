import os

# lista de restaurantes
restaurantes_old = ['Pizza', 'Esfira']

# dicionario de restaurantes
restaurantes = [ 
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False},
    {'nome': 'Subway', 'categoria': 'Lanche Rápido', 'ativo': False}
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Exibe as opções do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe a mensagem de finalização do app'''
    exibir_subtitulo('Finalizando o app')

def exibir_subtitulo(texto):
    '''Exibe um subtítulo com um texto personalizado
    Inputs:
    - texto: texto informado pelo usuário

    Outputs:
    - Exibe um subtítulo personalizado

    '''
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Exibe uma mensagem de opção inválida e volta ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Volta ao menu principal'''
    input('\nDigite ENTER para voltar ao menu inicial')
    main()

def cadastrar_novo_restaurante():
    '''Essa função é reponsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome: nome do restaurante a ser cadastrado
    - Categoria: categoria do restaurante a ser cadastrado

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome = input('Digite o nome do restaurante a ser cadastrado: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome}: ')
    # restaurantes.append(nome)
    dados_do_restaurante = {
        'nome':nome,
        'categoria':categoria,
        'ativo':False
        }
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é reponsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']

        ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_status_restaurante():
    '''Essa função é reponsável por alternar o status do restaurante'''
    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja modificar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #se o status for true vai ficar false e se for false vai ficar true
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante  {nome_restaurante} foi desativado com sucesso' #utilizando o operador ternário
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é reponsável por escolher a opção do menu principal'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_status_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''Essa função é reponsável por executar o programa'''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()