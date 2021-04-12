from modulos import *
from arquivo import *
from time import sleep

arq='ex115/cursoemvideo.txt'

if not arquivoExiste(arq):
        criarArquivo(arq)

while True:
        
    resposta=menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta==1:
        #opção de listar conteúdo do arquivo
        lerArquivo(arq)
    elif resposta==2:
        #opção de  cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome:'))
        idade=LeiaInt('Idade:')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        #opção de sair do sistema
        cabecalho('\033[1;34m Saindo sistema.. \033[m')
        sleep(1)
        break
    else:
        print('\033[31m ERRO Opção inválida \033[m')
    sleep(2)

