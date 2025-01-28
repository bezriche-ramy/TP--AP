liste=[1,2,3,4,5]
print(liste)
while True:#boucle pour s'assurer que l'index entree est un entier
    try:
        index=int(input("Entrer un index (-1 pour quitter): "))
        if index==-1:
            print("Programme Termine!")
            print(liste)
            break
        if not(0<=index<len(liste)):
            print("out-of-range! veuillez reessayer")
            continue
        """boucle pour s'assurer que la valeur entree est un entier, 
        pour ne demande pas a l'utilisateur de reentrer l'index une fois qu'il a entre un index valide"""
        while True:
            try:
                value=int(input("Entrez une nouvelle valeur: "))
                break
            except ValueError:
                print("non-integer! veuillez reessayer")
        liste[index-1]=value
        print(liste)
    except ValueError:
        print("non-integer! veuillez reessayer")        
