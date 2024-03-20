def AbcCacBdd():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    abc=100*a+10*b+c
                    cac=101*c+10*a
                    bdd=100*b+11*d
                
                    if abc+cac==bdd:
                        print(f'{abc}+{cac}={bdd}')

AbcCacBdd()