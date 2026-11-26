import csv
with open("commandes.csv", encoding="utf-8") as f:
    commandes = list(csv.DictReader(f, delimiter = ','))  # le texte du fichier devient une liste de dictionnaires

for dic in commandes : 
    dic["montant"] = float(dic["montant"])

def rapport_client(commande):
    rapport = {}                   #initialisation d'un rapport vide
    for ligne in commande :         #   une seule itération de toute la liste commande
        if ligne["client"] in rapport :#si le client existe déjà dans rapport
            rapport[ligne["client"]] += ligne["montant"] #on ajoute simplement le montant de la ligne en cours a la valeur stockée avec la clé du client
        else  :                                            #sinon
            rapport[ligne["client"]] = ligne["montant"]   # on crée une nouvelle clé à laquelle on associe sa première valeur
    return rapport

rapport = rapport_client(commandes)
        
with open("rapport.csv", "w", encoding='utf-8', newline="") as rpt :
    writer = csv.writer( rpt, delimiter = ',')
    writer.writerow(["client", "total"])
    for nom, total in rapport.items() :
        writer.writerow([nom, total])

print("Rapport écrit", rapport)