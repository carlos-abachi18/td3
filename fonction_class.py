from gettext import translation


customers_list = []
transaction_list = []
class Customers:
    num_customers = 1
    def __init__(self, p_code, p_nom, p_phone, p_address,p_email,p_solde):
        self.code = p_code
        self.nom  = p_nom
        self.phone = p_phone
        self.address = p_address
        self.email = p_email
        self.solde = p_solde 
        Customers.num_customers = Customers.num_customers + 1



def customer_add2():

    client = {}
    
    code = input("entrer le code du client: ")
    name = input("entrer le nom du client: ")
    phone =input("entrer le telephone du client: ")
    address=input("entrer l'adress du client:  ")
    mail  =input("entrer l'email du client: ")
    solde =input("entrer le solde du client: ")
    client["code"] = code 
    client["name"] = name
    client["phone"] = phone
    client["address"] = address
    client["mail"] = mail
    client["solde"] = solde
    customers_list.append(client)
    print( f"       ✅ le client {client.nom} a bien été ajouté ✅ "  )   

def customer_add():

    code = f"00{Customers.num_customers}"
    name = input("entrer le nom du client: ")
    phone =input("entrer le telephone du client: ")
    address=input("entrer l'adress du client:  ")
    mail  =input("entrer l'email du client: ")
    solde =input("entrer le solde du client: ")
    client = Customers(code,name,phone,address,mail,solde)
    customers_list.append(client)
    print( f"       ✅ le client {client.nom} a bien été ajouté ✅ "  )   
    

def customer_display(self):

    print(f"""client_{self.code}     
            code = {self.code} 
            nom  = {self.nom} 
       téléphone = {self.phone}
          adress = {self.address} 
            mail = {self.email} 
           solde = {self.solde} """)
    print(f"{ "-" *35}" )

def customer_change(self):
    change_list = range(1,6)
    menu_change ="""quelle information souhaitez vous modifier ?:
                1- le code
                2- le nom
                3- le téléphone
                4- l'adresse 
                5- l'email 
                6- le solde """
    print(menu_change)
    change_choice = input("👉entrez votre choix :  ")
    while not (change_choice.isdigit() or int(change_choice) in change_list): 
        print ("        ⛔ entrer un choix correct entre 1 et 5 ⛔")
        print(menu_change)
        change_choice = input("quel est votre choix ?: ")
    if int(change_choice) == 1:
        new_code = input(" entrez le nouveau code du client ")
        self.code = new_code
        print("     ✅ changement effectué avec succès ✅ ")
    elif int(change_choice) == 2:
        new_name = input(" entrez le nouveau nom du client ")
        self.name = new_name
        print("     ✅ changement effectué avec succès ✅ ")
    elif int(change_choice) == 3:
         new_phone = input(" entrez le nouveau téléphone du client ")
         self.phone = new_phone
         print("    ✅ changement effectué avec succès ✅ ")
    elif int(change_choice) == 4:
         new_address = input(" entrez le nouvel adresse  du client ")
         self.address = new_address
         print("    ✅ changement effectué avec succès ✅ ")
    elif int(change_choice) == 5:
         new_email = input(" entrez le nouveau email du client ")
         self.email = new_email
         print("    ✅ changement effectué avec succès ✅ ")
    elif int(change_choice) == 6:
         new_solde = input(" entrez le nouveau solde du client ")
         self.solde = new_solde
         print("    ✅ changement effectué avec succès ✅ ")

def customer_solde(self):
    print(f"le solde de {self.nom} est de {self.solde}")

class Transaction:
     num_transaction = 1 
     def __init__ (self, p_ref_paiement,p_code_emmeteur, p_code_recepteur, p_date_transaction,p_montant, p_canal):
       self.ref = p_ref_paiement
       self.code_emmeteur = p_code_emmeteur 
       self.code_recepteur = p_code_recepteur
       self.date = p_date_transaction
       self.montant = p_montant
       self.canal = p_canal
       Transaction.num_transaction = Transaction.num_transaction + 1 

def transaction_view(self) :
    print(f"""transaction_{self.ref}     
            ref_paiement = {self.ref} 
            code_emmeteur= {self.code_emmeteur} 
          code_recepteur = {self.code_recepteur}
         date_transaction= {self.date} 
                 montant = { self.montant} 
                   canal = {self.canal} """)
    print(f"{ "-" *35}" )

def transction_add():
    canal         =input("entrer le canal utilisé pour la transaction : ")
    ref           = f"{canal}_00A{Transaction.num_transaction}"
    code_emeteur  = input("entrer le code du client emeteur : ")
    code_recepteur= input("entrer le code du client recepteur : ")
    date_trans    =input("entrer la date de la transaction :  ")
    montant       =input("entrer le montant de la transaction : ")
    transaction   = Transaction(ref,code_emeteur,code_recepteur,date_trans,montant,canal)
    transaction_list.append(transaction)
    print( f"       ✅ la transaction  {transaction.ref} a bien été ajouté ✅ "  )   
    
def change_solde(self):
    new_solde = input(" entrez le nouveau solde du client ")
    self.solde = new_solde
    print("    ✅ changement effectué avec succès ✅ ")
