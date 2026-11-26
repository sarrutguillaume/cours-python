import json
with open("commandes.json", encoding="utf-8") as f:
    commandes = json.load(f)   # le texte du fichier devient une liste de dictionnaires


def rapport_client(commande):
    rapport = {}                   #initialisation d'un rapport vide
    for ligne in commande :         #   une seule itération de toute la liste commande
        if ligne["client"] in rapport :#si le client existe déjà dans rapport
            rapport[ligne["client"]] += ligne["montant"] #on ajoute simplement le montant de la ligne en cours a la valeur stockée avec la clé du client
        else  :                                            #sinon
            rapport[ligne["client"]] = ligne["montant"]   # on crée une nouvelle clé à laquelle on associe sa première valeur
    return rapport

rapport = rapport_client(commandes)
        
with open("rapport.json", "w", encoding="utf-8") as f:
    json.dump(rapport, f, indent=2, ensure_ascii=False)

print("Rapport écrit", rapport)