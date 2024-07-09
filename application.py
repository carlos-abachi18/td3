from fonction_class import *

menu_list = range(1,4)
menu_cust_list = range(1,7)
menu_trans_list = range(1,6)

menu = """ 💠 choisissez parmi les 3  operations suivantes 💠 : 

          1 - gestion des clients
          2 - gestion des transactions
          3 - sortir 
          """

menu_customer = """💠choisissez parmi les 5  operations suivantes 💠:

            1- afficher la liste des clients
            2- ajouter un client
            3- supprimer un client
            4- modifier les informations d'un client
            5- afficher le solde d'un client 
            6- retour 
            """

menu_transaction = """ 💠 choisissez parmi les 4 operations suivantes 💠: 

            1- afficher toutes les transactions
            2- afficher les transactions d'un client
            3- ajouter la transaction entre deux clients
            4- modifier le solde d'un client 
            5- Retour 
            """

while True:
    print(menu)
    choice = input( "👉Quel est votre choix:  ")
    while not choice.isdigit() or not int(choice) in menu_list: 
        print ("        ⛔ entrer un choix correct entre 1 et 3 ⛔")
        print(menu)
        choice = input("👉quel est votre choix ?: ")

    if int(choice ) == 1:
        while True:
            print(menu_customer)
            choice_cust = input( "👉Quel est votre choix:  ")
            while not choice_cust.isdigit() or  not int(choice_cust) in menu_cust_list: 
                print ("        ⛔ entrer un choix correct entre 1 et 5 ⛔")
                print(menu_customer)
                choice_cust = input("👉quel est votre choix ?: ")

            if int(choice_cust) == 1:
                if customers_list == []:
                    print("     💠votre liste de client est vide 💠")
                else:
                    for cust in customers_list:
                        customer_display(cust)

            elif int(choice_cust) == 2:
                customer_add()

            elif int(choice_cust) == 3:
                 customers_del =input("💠entrer le nom du client que vous souhaiter supprimer: ")
                 indic_del = None
                 for cust in customers_list:
                    if customers_del == cust.nom:
                        indic_del= cust 
                        break
                    
                 if indic_del != None:
                    customers_list.remove(indic_del)
                    print("     💠client supprimé avec succes💠")
                 else:
                   print("     ⛔aucun client avec ce nom⛔")

            elif int(choice_cust) == 4:
                client_name = input("entrer le nom du client pour qui vous souhaitez modifier des informations: ")
                indic_change = None
                for cust in customers_list:
                    if client_name == cust.nom:
                        indic_change = cust 
                        break
                if indic_change != None:
                   customer_change(indic_change)
                else:
                   print("     ⛔aucun client ne porte ce nom ⛔")

            elif int(choice_cust) == 5:
                client_name = input("entrer le nom du client pour qui vous souhaiter afficher le solde : ")
                indic = None
                for cust in customers_list:
                    if client_name == cust.nom:
                        indic = cust 
                        break
                if indic != None:
                    customer_solde(indic)
                else:
                    print("     ⛔aucun client ne porte ce nom⛔")

            elif int(choice_cust) == 6:
                break 
             
                
    elif int(choice) == 2: 
         while True:
            print(menu_transaction)
            choice_transac = input( "👉Quel est votre choix:  ")
            while not choice_transac.isdigit() or  not int(choice_transac) in menu_trans_list: 
                print ("        ⛔ entrer un choix correct entre 1 et 5 ⛔")
                print(menu_transaction)
                choice_transac = input("👉quel est votre choix ?: ")

            if int(choice_transac) == 1:
                if transaction_list == []:
                    print("     💠 aucune transaction enregistrée 💠")
                else:
                    for trans in transaction_list:
                        transaction_view(trans)

            elif int(choice_transac) == 2:
                 code_customer = input(" entrez le code du client concerné : ")
                 trans_customer = []

                 for trans in transaction_list:
                     if  code_customer == trans.code_emmeteur or code_customer == trans.code_recepteur:
                         trans_customer.append(trans)
                        
                 if trans_customer == []:
                    print("     💠 aucune transaction enregistrée au nom de ce client 💠")
                 else:
                    for trans in trans_customer:     
                        transaction_view(trans)

            elif int(choice_transac) == 3:
                transction_add()
           
            elif int(choice_transac) == 4:

                client_code = input("💠 entrer le code du client pour qui vous souhaiter modifier le solde 💠: ")
                indic_change = None               
                trans_customer = []

                for trans in transaction_list:
                     if  client_code == trans.code_emmeteur or client_code == trans.code_recepteur:
                         trans_customer.append(trans)
                        
                if trans_customer == []:
                    print("     💠 aucune transaction enregistrée au nom de ce client 💠")
                else: 
                    for trans in trans_customer:     
                        transaction_view(trans)
                    print(" 🔼 voici les transactions effectuées par ce code client 🔼 ") 

                for cust in customers_list:
                    if client_code == cust.code:
                        indic_change = cust 
                        break
                if indic_change != None:
                  print (f"""
        👉 l'ancient solde de {cust.nom} etait de : {cust.solde} """)     
                  change_solde(indic_change)
                else:
                   print("     ⛔aucun client avec ce nom⛔")
                
            elif int(choice_transac) == 5:
                break 
    elif int(choice) == 3:
        exit()