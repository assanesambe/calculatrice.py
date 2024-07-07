
continuer = True

def calculator(num1,num2):

    z=(input("Choisissez l'opération à effectuer :(+, -, *, /)"))
    if z == "+":
        print(num1 + num2)
    elif z == "-":
         print(num1 - num2)
    elif z == "*":
        print(num1 * num2)
    elif z == "/" and num2 != 0:
         print(num1 / num2)
    else:
        print("Entrer le bon operateur")
    



while continuer == True  :
    x = int(input("Veuillez entrer le premier nombre: "))
    y = int(input("Veuillez entrer le deuxième nombre: "))
    calculator(x, y)
    n=input("Tapez y pour continuer ou q quitter" )
    if n == 'y':
        continuer = True
    
    else:
        continuer = False



    