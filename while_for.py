# les 10 premiers nombres paires #
nobre = range(2,22,2)
for i in nobre:
    print(i)
print("voici les 10 premiers nombre paires ")

# les 10 premiers nombres impaires #
counter = 0
i=1
while counter < 10:
    print (i)
    counter +=1
    i+=2 
print("voici les 10 premiers nombre impaires ")

#les nombres entiers compris entre 1 et la valeur entré #
nobre_enter = input("""
        ▶▶entrer un nombre: """)
while not nobre_enter.isdigit():
    print( "🛑❌ entrer un nombre entier correct 🛑❌")
    nobre_enter = input("""
        ▶▶entrer un nombre: """)
liste = range(1,int(nobre_enter))
for i in liste:
    print(i)
print(f"voici les nombres entiers compris entre 1 et {nobre_enter}")
