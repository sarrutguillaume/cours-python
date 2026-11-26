import csv
def rapport_client(commande):
    rapport = {}                   #initialisation d'un rapport vide
    for ligne in commande :         #   une seule itération de toute la liste commande
        if ligne["client"] in rapport :#si le client existe déjà dans rapport
            rapport[ligne["client"]] += ligne["montant"] #on ajoute simplement le montant de la ligne en cours a la valeur stockée avec la clé du client
        else  :                                            #sinon
            rapport[ligne["client"]] = ligne["montant"]   # on crée une nouvelle clé à laquelle on associe sa première valeur
    return rapport
def somme_commande (commande):
    Montant_total = 0
    for dic in commande :
        Montant_total += dic["montant"]
    return Montant_total 

try :
    with open("commandes_sales.csv", encoding="utf-8") as f:
        commandes_sales = list(csv.DictReader(f, delimiter = ','))  # le texte du fichier devient une liste de dictionnaires
except FileNotFoundError:
    print(f"Fichier introuvable : commandes_sales.csv")
    exit()

commandes_valides=[]

for dic in commandes_sales : 
    try :
        dic["montant"] = float(dic["montant"])
        commandes_valides.append(dic)
    except ValueError :
        print(f"Ligne ignorée({dic['id']}): montant '{dic["montant"]}' invalide ")
            
 
rapport = rapport_client(commandes_valides)
TOTAL = somme_commande(commandes_valides)           
with open("rapport.csv", "w", encoding='utf-8', newline="") as rpt :
    writer = csv.writer( rpt, delimiter = ',')
    writer.writerow(["client", "montant_total"])
    for nom, total in rapport.items() :
        writer.writerow([nom, total])
    writer.writerow(["TOTAL", TOTAL] )

print("Rapport écrit", rapport)
