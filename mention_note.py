
note = input("entrez votre note =  ") 

while not note.isdigit():
    print("❌❌entrez une note correcte entre 0 et 20 ")
    note = input ("entrez votre note = ")

note = int(note)
if note >= 18 and note <=20:
 print("Excellent")
elif note >= 16 and  note < 18:
     print("Très bien")
elif note >= 14 and  note < 16:
     print("Bien")
elif note >= 12 and  note < 14:
     print("Satisfaisant")
elif note >= 10 and  note < 12:
     print("passable")
else:
    print("echec")
