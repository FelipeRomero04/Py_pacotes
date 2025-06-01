def aumentar(price, porcent, f=True):
    more = price + (price * porcent / 100)
    
    return more 


def diminuir(price, porcent, f=True):
    less = price - (price * porcent / 100)

    return less 


def dobro(price, f=True):
    double = price * 2
    
    return double 


def metade(price, f=True):
    half = price / 2

    return half 


def type_currency(price, moeda='R$'):
    return f'{moeda}{price:.2f}'.replace('.', ',')


def resumo(p, porc_more, porc_less, f=True):

    list = [
        ('Preco Analisado:', p), 
        ('Dobro do preco', dobro(p, f)), 
        ('Metade do preco', metade(p, f)), 
        (f'{porc_more}% de aumento', aumentar(p, porc_more, f)), 
        (f'{porc_less}% de redução', diminuir(p, porc_less, f))
        ]

    print('-' * 30)
    print(f'{'RESUMO DO VALOR':>22}')
    print('-' * 30)

    for k, v in list:
       
        print(f'{k:<20} {v if not f else type_currency(v)}')
    print('-' * 30)
    

