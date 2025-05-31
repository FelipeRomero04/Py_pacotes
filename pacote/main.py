import modulos.moeda as moeda
from dados.moneydbug import leia_dinheiro

p = leia_dinheiro('Digite o preço: ')
moeda.resumo(p, 85, 30, f=True)