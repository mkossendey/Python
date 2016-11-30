def spAnzeigen(liste):
    print("Essen | Preis")
    for element in liste:
        liste2 = element.split(";")
        print(liste2[0] + " | " + liste2[1] + " cent")
    print()

def spDelete(liste):
    liste.clear()
    print(liste)

def neuesGericht(liste):
    name = input("Name :")
    preis = input("Preis :")
    neuesGericht = name + ";" + preis
    liste.append(neuesGericht)

def beenden(liste):
    speisekarte = open("speisekarte1.txt", "w")
    speisekarte.seek(0)
    speisekarte.truncate()
    for item in liste:
        speisekarte.write("%s\n" % item)
        ans = False
try:
    speisekarte = open("speisekarte1.txt","r")
    liste1 = speisekarte.read().split("\n")
        
except IOError:
    print("Speisekarte wurde nicht gefunden!")
ans=True
while ans:
    print("a = Speisekarte anzeigen\n"+"n = neue Speisekarte anlegen\n"+"s = Speisekarte erweitern\n"+"l = Gericht löschen\n" +"g = Gericht suchen\n" + "e = Speichern und Programmende\n")
    eingabe = input()

    if eingabe=="a":
        spAnzeigen(liste1)

    elif eingabe == "n":
        spDelete(liste1)

    elif eingabe == "s":
        neuesGericht(liste1)

    elif eingabe == "l":
        try:
            name = input("Name :")
            name2 = set(name)
            for word in liste1:
                if name2 && set(word):
                    print(word)
        except IOError:
            print("Nicht gefunden")
    elif eingabe == "g":
        pass
    elif eingabe == "e":
        beenden(liste1)

    else:
        print("Falsche eingabe!\n"+"Versuche es nochmal.\n"+"\n")










"""with open('speisekarte1.txt') as my_file:
    testsite_array = my_file.readlines().split(";")

print(testsite_array)"""
