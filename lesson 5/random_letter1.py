import random
L=['самовар','весна', 'лето']
rand=random.choice(L)
if rand=='самовар':
    print ( rand[:-1]+'?')
    l=str(input("Введите букву: "))
    if l=="р":
        print("Победа!\n Слово: самовар")
    else:
        print ("Увы! Попробуйте в другой раз.\n Слово: самовар")
elif rand=='лето':
    print ( rand[0:1]+'?'+rand[2:])
    l=str(input("Введите букву: "))
    if l=="е":
        print("Победа!\n Слово: лето")
    else:
        print ("Увы! Попробуйте в другой раз.\n Слово: лето")
elif rand=='весна':
    print ( rand[0:2]+'?'+rand[3:])
    l=str(input("Введите букву: "))
    if l=="с":
        print("Победа!\n Слово: весна")
    else:
        print ("Увы! Попробуйте в другой раз.\n Слово: весна")

