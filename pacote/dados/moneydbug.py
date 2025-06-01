from decimal import Decimal
    

def leia_dinheiro(msg):

    while True:
        p = input(msg).strip().replace(',', '.')
        try:
            return Decimal(p)
        except Exception:
            print(f'Erro! "{p}" não é um valor válido.')       

                


    


