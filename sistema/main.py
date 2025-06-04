from dados import db
from utils import util
from time import sleep

cont = 0

while cont < 5:
    option = util.menu() #chama menu e retorna valor da option

    db.register()  
    cont += 1
    


