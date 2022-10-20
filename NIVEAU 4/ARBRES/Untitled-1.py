def valide(noeud,masque):
    noeud = str(noeud)
    print(noeud)
    lenNoeud = len(noeud)
    print(lenNoeud)
    lenMasque = len(masque)
    if lenNoeud != lenMasque:
        return False
    for i in range(lenMasque):
        if masque[lenMasque-1-i] == '?':
            continue
        elif masque[lenMasque-1-i] != noeud[lenMasque-1-i]:
            return False
    return True

print(valide(12,'?'))