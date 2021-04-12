def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            
        except(ValueError, TypeError):
            print('\033[31m ERRO:Por favor digite um número inteiro!! \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m Entrada de dados interrompida pelo usuário \033[m]')
            return 0
        else:
            return n

def linha(tam=42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha() )
   

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1 
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m {item} \033[m')
        c+=1
    print(linha())
    opc= LeiaInt('\033[32m Sua Opção: \033[m ')
    return opc