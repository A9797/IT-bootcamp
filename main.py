def buchstaben():
    buchstaben = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #buchstaben.append("D")
    antwort = str(input("Geben Sie eine Buchstabe ein ?"))
    #z = 0
    y = 0
    for x in buchstaben:
        for y in range(26):
            print(end=" ")
        print(x)
        #z = z + 1
        if x == antwort:
            exit()
buchstaben()
