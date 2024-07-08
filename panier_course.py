menu ="""Choisissez parmi les 5 options suivantes:
1- Ajouter un article dans le panier
2- Supprimer un article du panier
3- Afficher tous les articles
4- Vider le panier
5- Quitter
"""

choix= range(1,6)
panier = []

while True:
    print(menu)
    choice= input("quel est votre choix ?: ")
    while not choice.isdigit() or not int(choice) in choix: 
        print ("        ⛔ entrer un choix correct entre 1 et 5 ⛔")
        print(menu)
        choice= input("quel est votre choix ?: ")
    
    if int(choice) == 1:
            articles = {}
            article_name = input("💠entrer le nom de l'article: ")
            article_price = input("💠entrer le prix de l'article: ")
        
            while not article_price.isdigit():
                print ("⛔entrer un prix correcte⛔ ")
                article_price = input("💠entrer le prix de l'article: ")

            articles["name"] = article_name
            articles["price"] =article_price
            panier.append(articles)
            print("     💠article ajouté avec succes💠")
            
    elif int(choice) == 2:
        article_del =input("💠entrer le nom de l'article que vous souhaiter supprimer: ")
        dictio_del = None
        for i in panier:
             if article_del== i["name"]:
                dictio_del= i 
                break
             
        if dictio_del != None:
            panier.remove(dictio_del)
            print("     💠article supprimé avec succes💠")
        else:
            print("     ⛔aucun article avec ce nom⛔")
        
    elif int(choice) == 3:
        if panier == []:
            print("     💠votre panier ne contient aucun article💠")
        else:
            for i in panier:
                print(f"{i["name"]}: {i["price"]} CFA")
            print("     💠voici le contenu de votre panier💠")

    elif int(choice) == 4:
         panier.clear()
         print("        💠panier vider avec succes💠")
    elif int(choice) == 5:
         exit()
    print("x"* 50) 