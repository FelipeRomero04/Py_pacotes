from .dados import db
from .utils import util
from time import sleep

cont = 0

while cont < 5:
    try:
        option = util.menu().strip()  #chama menu e retorna valor da option

        if not option.isnumeric() or not option in (('1'), ('2'), ('3')):
            print('ERRO! valor inválido')
            continue
    except KeyboardInterrupt:
        print('O programa foi interrompido pelo usúario...')
        break

    
    
    try:  #TESTAR COLOCAR O NOME E IDADE NO MESMO TRY TO CANSADO
        name = input('Informe o nome: ')
        if any(l for l in name if l.isnumeric):
            print('Erro Va')
        old = input('Informe idade: ')
        



    db.options(option, name, old) 
    sleep(2)
    
    

# try:
    #     option = int(util.menu().strip())
    # except Exception or 1 <= option <= 3:
    #     print('Valor invalido')
    #     continue
    # except KeyboardInterrupt:
    #     print('O programa foi interrompido pelo usuário...')
    #     break