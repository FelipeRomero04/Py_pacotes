def aumentar(preco, porcent, f=True):
    more = preco + (preco * porcent / 100)

    if f:
        return (f'${more:.2f}')
    return more

def diminuir(preco, porcent, f=True):
    less = preco - (preco * porcent / 100)
    if f:
        return (f'${less:.2f}')
    return less

def dobro(preco, f=True):
    double = preco * 2

    if f:
        return(f'${double:.2f}')
    return double

def metade(preco, f=True):
    half = preco / 2

    if f: #formatar com cifrão ou não
        return (f'${half:.2f}')
    return half


def resumo(p, porc_more, porc_less, f=True):

    list = [
        ('Preco Analisado:', f'${p}'), 
        ('Dobro do preco', dobro(p)), 
        ('Metade do preco', metade(p)), 
        (f'{porc_more}% de aumento', aumentar(p, porc_more)), 
        (f'{porc_less}% de redução', diminuir(p, porc_less))
        ]

    print('-' * 30)
    print(f'{'RESUMO DO VALOR':>22}')
    
    print('-' * 30)
    for k, v in list:
        v = str(v).replace('.', ',')
      
        print(f'{k:<20} {v}')
    print('-' * 30)
    

