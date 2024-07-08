def menu():
    resultat = input("""Choisissez parmi les 5 options suivantes:
1- Ajouter un article dans le panier
2- Supprimer un article du panier
3- Afficher tous les articles
4- Vider le panier
5- Quitter
👉Quel est votre choix ?: """)
    return resultat 

def article_add( article_name , article_price ):
    while not article_price.isdigit():
        print ("⛔entrer un prix correcte⛔ ")
        article_price = input("💠entrer le prix de l'article: ")
    articles[f"name"] = article_name
    articles[f"price"] =article_price
    panier.append(articles)
    print("     💠article ajouté avec succes💠")

def article_delete(article_del):
    dictio_del = None
    for i in panier:      
             if article_del == i["name"]:
                dictio_del= i  
                break
             
    if dictio_del != None:
        panier.remove(dictio_del)
        print("     💠article supprimé avec succes💠")
    else:
        print("     ⛔aucun article avec ce nom⛔")

def panier_view():
    if panier == []:
        print("     💠votre panier ne contient aucun article💠")
    else:
        for i in panier:
            print(f"{i["name"]}: {i["price"]} CFA")
        print("     💠voici le contenu de votre panier💠")

def panier_clear():
    panier.clear()
    print("        💠panier vider avec succes💠")

def panier_exit():
     exit()

choix=[1,2,3,4,5]
panier = []

while True:
    choice = menu()
    while not choice.isdigit() or not int(choice) in choix: 
        print ("        ⛔ entrer un choix correct entre 1 et 5 ⛔")
        choice = menu()
    
    if int(choice) == 1:
            articles = {}
            article_name = input("💠entrer le nom de l'article: ")
            article_price = input("💠entrer le prix de l'article: ")
            article_add(article_name,article_price)    
              
    elif int(choice) == 2:
        article_del =input("💠entrer le nom de l'article que vous souhaiter supprimer: ")
        article_delete(article_del)

    elif int(choice) == 3:
         panier_view()
         
    elif int(choice) == 4:
        panier_clear()

    elif int(choice) == 5:
         panier_exit()
    print("x"* 50) 