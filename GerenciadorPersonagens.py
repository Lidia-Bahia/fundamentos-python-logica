"""
Sistema simples de gerenciamento de personagens.

Funcionalidades:
- Cadastro de personagens
- Consulta de personagens
- Consulta por ID
- Consulta por função
- Remoção de personagens

Projeto desenvolvido como exercício de lógica de programação em Python.
"""

print('Seja bem-vindo(a) ao Gerenciador de Personagens!')

lista_personagens = []
id_global = 1


# função para exibir personagem
def mostrar_personagem(personagem):
    for chave, valor in personagem.items():
        print(f'{chave}: {valor}')
    print('-' * 20)


# função cadastro de personagem
def cadastrar_personagem(personagem_id):
    print('\n', '-' * 10, 'CADASTRO DE PERSONAGENS', '-' * 10, '\n')
    print(f'ID do Personagem: {personagem_id}')

    nome = input('Nome: ')
    funcao = input('Função: ')
    poderes = input('Poderes (separados por vírgula): ').split(',')

    
    personagem = {
        'id': personagem_id,
        'nome': nome,
        'função': funcao,
        'poderes': poderes
    }

    lista_personagens.append(personagem)


# função consulta de personagens
def consultar_personagem():
    print('\n', '-' * 10, 'CONSULTA DE PERSONAGENS', '-' * 10, '\n')
    print('1. Consultar todos')
    print('2. Consultar por ID')
    print('3. Consultar por função')
    print('4. Retornar ao menu\n')

    while True:
        consulta = input('Informe a opção desejada: ')

        if consulta == '1':
            for personagem in lista_personagens:
                mostrar_personagem(personagem)

        elif consulta == '2':
            busca_id = int(input('ID: '))

            for personagem in lista_personagens:
                if personagem['id'] == busca_id:
                    mostrar_personagem(personagem)
                    break
            else:
                print('Personagem não encontrado.')

        elif consulta == '3':
            busca_funcao = input('Função: ')

            for personagem in lista_personagens:
                if personagem['função'] == busca_funcao:
                    mostrar_personagem(personagem)

        elif consulta == '4':
            return

        else:
            print('Opção inválida. Tente novamente.')


# função remover personagem
def remover_personagem():
    print('\n', '-' * 10, 'REMOVER PERSONAGEM', '-' * 10, '\n')

    while True:
        try:
            apaga = int(input('ID: '))
        except ValueError:
            print('Entrada aceita apenas valores numéricos.')
            continue

        for personagem in lista_personagens:
            if personagem['id'] == apaga:
                lista_personagens.remove(personagem)
                print('Personagem removido com sucesso!')
                return

        print('ID não encontrado.')


# código principal
while True:
    print('\n', '-' * 10, 'MENU PRINCIPAL', '-' * 10, '\n')
    print('1 - Cadastrar personagens')
    print('2 - Consultar personagens')
    print('3 - Remover personagem')
    print('4 - Sair\n')

    try:
        program = int(input('Escolha a opção desejada: '))
    except ValueError:
        print('Insira apenas números inteiros.')
        continue

    if program == 1:
        cadastrar_personagem(id_global)
        id_global += 1

    elif program == 2:
        consultar_personagem()

    elif program == 3:
        remover_personagem()

    elif program == 4:
        print('Atendimento finalizado!')
        break

    else:
        print('Seleção inválida. Tente novamente.')