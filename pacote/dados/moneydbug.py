from decimal import Decimal
    

def leia_dinheiro(msg):

    while True:
        p = input(msg).strip()
        if ',' in p:
            p_split = p.split(',')
        
            for v in p_split:
                if v.isnumeric:
                    continue
                print('Erro')
                break
            p = Decimal('.'.join(p_split)) #Junta e transf em decimal
            return p
        try:
            return Decimal(p)
        except ValueError:
            print(f'Erro! "{p}" não é um valor válido.')       

                
            
    

    


