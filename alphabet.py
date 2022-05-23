##EXO 1 : Afficher une liste d'alphabet
def ListAlphabet():
    print([chr(ord('a') + i) for i in range(26)])
        

##EXO 2 : Afficher les trible croisssante <10
def triplet(n):
    L = []
    for i in range(1, n+1):
        for j in range(i+1, n):
            for k in range(j+1, n):
                L.append((i, j, k))
    return(L)
                
print(triplet(10))      
    
    
##EXO 2 : creer la liste [(’a’, 0), (’b’, 1), (’a’, 2),
##                           (’b’, 3), ..., (’a’, 18), (’b’, 19)]

def ListeAlphabetChiffre(n):
    maListe = []
    for i in range (0, n):
        if (i%2) == 0:
            a = ('a', i)
            maListe.append(a)
        else:
            b = ('b', i)
            maListe.append(b)
    return(maListe)

print(ListeAlphabetChiffre(19))

##EXO 3 : afficher l’ensemble des nombres premiers inferieurs a 100

def NombrePremier(n):
    
    ListePremiere = []
    for i in range(2, n+1):
        trouve = 0
        for j in range(2, i):
            if i%j ==0:
                trouve = 1
        if trouve ==0:
            ListePremiere.append(i)
    print(ListePremiere)
    
Liste_premiers = NombrePremier(100)
Liste_premiers


    

