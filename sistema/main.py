from .dados import db
from .utils import util
from time import sleep

while True:
    try:
        name = util.debug_dados_name
        old = util.debug_dados_old

        op = util.menu()

        db.options(op, name, old) 
        
        sleep(2)
        
        if op == '3':
            break

    except KeyboardInterrupt:
        print('\nERRO! O usuário interrompeu o programa...')
        break