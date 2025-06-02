from modulos import moeda
from dados.moneydbug import leia_dinheiro
 

p = leia_dinheiro('Digite o preço: ')
moeda.resumo(p, 85, 30, f=True)


'''
-m: executa como modulo

-m: 'dentro do modulo 'pacote''
.main: execute esse arquivo

sempre deve estar atento as importações do arquivo que esta executando, se elas estão sempre referenciando a raiz



Ler mais sobre  diferença das importações(relativas, absolutas) e descobrir que diferença faz executar pelo start do vscode ou manualmente, e o por que não e possivel executar das duas formas

'''