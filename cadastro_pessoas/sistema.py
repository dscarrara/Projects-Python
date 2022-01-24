from time import sleep

from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                    'Cadastrar Nova Pessoa', 'Sair  do Sistema'])
    if resposta == 1:
        # Opção para listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
