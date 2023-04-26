#Programm macht eine Ausgabe auf der Konsole

name = str(input("Geben Sie Ihr Name ein: "))

#Programm macht Konsolenausgabe einer Liste von String Elementen (12 Elemente)

countdown = ["1","2","3","4","5","6","7","8","9","10","11","12"]
x=11
while x >= 0 :
    print(countdown[x])
    x = x-1
print("Haloo " + name + " !")

#Programm liest Datei aus (text) und macht Konsolenausgabe des gesamten Inhalts

answer = input("Wollen Sie ein kleines Pythonprogramm propieren?(y/n)" )
if answer == "y" :
    with open ('lorem ipsum.txt') as f:
        file = f.read()
        print(file)

    #Der Inhalt wird nach Leerzeichen in einzelne Wörter getrennt und die Gesamtzahl aller Wörter auf der Konsole ausgegeben

        words = file.split(" ")
        print("Es gibt",len(words),"wörter im Text.")

    #bestimmtes Wort aus der Datei zählen

    antwort = input("welches Wort aus der Datei soll gezählt werden ?")
    zäller=0
    for x in range(len(words)):

        if words[x] == antwort:
            zäller = zäller+1
    print("Es gibt ",zäller,antwort, "im Text.")

else:
    print("Danke für Ihre Zeit.")
    exit()