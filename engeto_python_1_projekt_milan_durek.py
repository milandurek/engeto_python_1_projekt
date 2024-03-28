"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Milan Důrek 
email: m.durek@seznam.cz
discord: arkalik
"""

zadane_jmeno = str
zadane_heslo = str
zvoleny_text = int

ulozene_jmeno = ("bob", "ann", "mike","liz")
ulozene_heslo = ("123", "pass123", "password123","pass123")
ulozene_jmenoheslo = ("bob123", "annpass123", "mikepassword123", "lizpass123")

analyzovany_text = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

zadane_jmeno = input("Zadejte vaše přihlašovací jméno: ")
zadane_heslo = input("Zadejte vaše přihlašovací heslo: ")
zadane_jmenoheslo = zadane_jmeno + zadane_heslo

if (zadane_jmeno in ulozene_jmeno) and (zadane_heslo in ulozene_heslo) and (zadane_jmenoheslo in ulozene_jmenoheslo):
    print("Došlo k úspěšnému přihlášení uživatele" , zadane_jmeno,)
    
    zvoleny_text = input("Vyberte prosím číslo od 1 do 3 pro výběr textu: ")
    zvoleny_text = int(zvoleny_text) - 1

    rozpadnuty_text = analyzovany_text[zvoleny_text].split()
    pocet_istitle = int()
    pocet_isupper = int()
    pocet_islower = int()
    pocet_cisel = int()
    soucet_cisel = int()
    analyza_slov = dict()


    for prvek in rozpadnuty_text:
        if str.istitle(prvek):
            pocet_istitle = pocet_istitle + 1

    for prvek in rozpadnuty_text:
        if str.isupper(prvek) and str.isalpha(prvek):
            pocet_isupper = pocet_isupper + 1

    for prvek in rozpadnuty_text:
        if str.islower(prvek):
            pocet_islower = pocet_islower + 1      

    for prvek in rozpadnuty_text:
        if str.isnumeric(prvek):
            pocet_cisel = pocet_cisel + 1
            soucet_cisel = soucet_cisel + int(prvek)    

    print("Celkový počet slov je: ", len(rozpadnuty_text))
    print("Celkový počet slov začínajících velkým písmenem: ", pocet_istitle)
    print("Celkový počet slov velkými písmeny: ", pocet_isupper)
    print("Celkový počet slov malými písmeny: ", pocet_islower)
    print("Celkový počet čísel: ", pocet_cisel)
    print("Celkový součet všech čísel: ", soucet_cisel)

    for prvek in rozpadnuty_text:
        if analyza_slov.get(len(prvek),"Neexistuje") == "Neexistuje":
                analyza_slov[len(prvek)] = 1
        else:
            analyza_slov[len(prvek)] = analyza_slov.get(len(prvek)) + 1   
    for vypis in range(1,len(analyza_slov) + 1):
        print(vypis,"|", analyza_slov[vypis] * "*","|", analyza_slov[vypis])
else:
    print("Zadané přihlašovací údaje nejsou správné")
