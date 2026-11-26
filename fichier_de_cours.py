Montant_total = 0

def somme_commande (commande):
    Montant_total = 0
    for dic in commande :
        Montant_total += dic["montant"]
    return Montant_total 

def total_client(com, clt) :
    Total = 0 
    trouve = False
    for dic in com :
        if clt == dic["client"] :
            trouve = True
            Total += dic["montant"]
    if trouve == False : 
        return None 
    else : 
        return Total




def plus_grosse_commande(commande):
    if not commande :
        return None
    meilleure = commande[0]
    for dic in commande : 
        if meilleure["montant"] < dic["montant"] : 
            meilleure = dic# on relève l'indice de ce dictionnaire qui a actionné un nouveau max
    return meilleure # quand la boucle est finie, on a gardé la valeur d'indice du dictionnaire qui nous intéressse et on la retourne 

 

