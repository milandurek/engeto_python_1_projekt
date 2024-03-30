"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Milan Důrek 
email: m.durek@seznam.cz
discord: arkalik
"""

zadane_jmeno = str()
zadane_heslo = str()
zvoleny_text = int()

ulozene_jmenoheslo = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

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

if ulozene_jmenoheslo.get(zadane_jmeno) == zadane_heslo:
    print("Došlo k úspěšnému přihlášení uživatele" , zadane_jmeno,)
    
    zvoleny_text = input("Vyberte prosím číslo od 1 do 3 pro výběr textu: ")
    zvoleny_text = int(zvoleny_text) - 1

    predpriprava_textu = analyzovany_text[zvoleny_text]
    predpriprava_textu = predpriprava_textu.replace(",", "")
    predpriprava_textu = predpriprava_textu.replace(".", "")

    rozpadnuty_text = predpriprava_textu.split()
    pocet_istitle = int()
    pocet_isupper = int()
    pocet_islower = int()
    pocet_cisel = int()
    soucet_cisel = int()
    analyza_slov = dict()


    for prvek in rozpadnuty_text:
        if str.istitle(prvek):
            pocet_istitle = pocet_istitle + 1
        if str.isupper(prvek) and str.isalpha(prvek):
            pocet_isupper = pocet_isupper + 1
        if str.islower(prvek):
            pocet_islower = pocet_islower + 1   
        if str.isnumeric(prvek):
            pocet_cisel = pocet_cisel + 1
            soucet_cisel = soucet_cisel + int(prvek)  
  
    print("Celkový počet slov je: ", len(rozpadnuty_text))
    print("Celkový počet slov začínajících velkým písmenem: ", pocet_istitle)
    print("Celkový počet slov velkými písmeny: ", pocet_isupper)
    print("Celkový počet slov malými písmeny: ", pocet_islower)
    print("Celkový počet čísel: ", pocet_cisel)
    print("Celkový součet všech čísel: ", soucet_cisel)

    print("LEN|  OCCURENCES  |NR.")

    for prvek in rozpadnuty_text:
        if analyza_slov.get(len(prvek),"Neexistuje") == "Neexistuje":
                analyza_slov[len(prvek)] = 1
        else:
            analyza_slov[len(prvek)] = analyza_slov.get(len(prvek)) + 1   
    for vypis in range(1,len(analyza_slov) + 1):
        print(vypis,"|", analyza_slov[vypis] * "*","|", analyza_slov[vypis])
else:
    print("Zadané přihlašovací údaje nejsou správné")

#Pokud používáš vscode, doporučuju použít určitě automatické formátování, takové detaily se lehce přehlédnou
        #Zkoušel jsem hledat na netu, ale žádný rozumný návod jsem nenašel. Nevíš, kde se prosím tě nastavuje? Díky
#Tady si nejsem jist co byl cíl. Pokud nějaký type hinting, tak správně je: promenna: typ = hodnota. 
#Zamysli se nad tím, co si takhle do proměnné takhle vlastně uložil, klidně prozkoumej s funkcí type.
        #Chtěl jsem si tam proměnné založit, ale udělal jsem chybu, že jsem zapomněl na závorky... Opraveno
#Tohle není úplně ideální způsob, jak to kontrolovat a je to poměrně neudržovatelné, když pridáš uživatele, musíš ho
#zároveň přidat do 3 proměnných, z nichž 1 je jen kombinace toho, co je ve dvou předchozích. Co použít jinou datovou strukturu?
        #Prošel jsem si zadání projektu a postupně procházel cvičení od první lekce. Když jsem našel nějaký způsob, jak se s projektem
        #posunout dále, tak jsem to do kódu zakomponoval. Chtěl jsem použít kontrolu zda existuje login a heslo, ale toto není správně
        #protože ti uživatel zadá heslo k jinému uživateli a ono by fungovalo... což není správně. Proto jsem vymyslel tohle řešení
        #, které podle mě splnilo zadání. Až v dalších lekcích jsem pak našel tu úlohu s dict a get na kontrolu, která je samozřejmě
        #lepší. Upravil jsem tedy dle této úlohy.
#Když opravíš to výše, zjednodušši se ti i tato podmínka:
        #Upraveno
#Možná by také bylo lepší použít nějakou datovou strukturu na tyhle proměnné, bylo by to trošku čitelnější. 
#Jinak nemusíš používat int() nebo dict(), stačí 0 a {}. :)    
        #Já se v tom hrozně ztrácím v těch formátech. Je to pro mě přehlednější... ale chápu..
#Dalo by se to dát do jednoho for cyklu? Takhle jich tam máš, skoro bych řekl zbytečně, 5.     
        #Dal jsem do jednoho cyklu..
#Tady ses dostal tak na půl cesty k určitému nápadu, co použít takový get, aby si mohl za každé situace jen přičíst jedničku? :) 
#Můžeš si pohrát s defaultní hodnotou, "Neexistuje" na to není ideální, ale k čemu bys ji mohl přičíst u prvního neexistujícího?   
        #Vůbec nechápu, co se po mě chce :D Za mě to funguje (výsledek odpovídá zadání) a to je hlavní...
#Ve výpisu ti chybí hlavička tabulky.
        #Přidáno    
#A nakonec ten hlavní problém, čísla nesedí. Zkus se ještě jednou podívat na výstup ze zadání projektu a porovnat, co přesně nesedí.
#Trošku navedu, podívej se do proměnné rozpadnuty_text na to, co obsahuje. Některá slova mají něco navíc.
        #Věděl jsem o těch tečkách a čárkách, ale nevědel jsem jak to vyřešit. Replace v listu nefunguje, asi by se dal nějak
        #projít ten list a vyměnit ty hodnoty. Jestli to jsou jenom čárky a tečky. Čísla nyní sedí..
        #Šel jsem tedy cestou list (bylo to zadání zadaného textu) - do stringu (odstranění čárek a teček) a zase zpět do listu.. 
        #Funguje to a to je za mě hlavní

#Celkově jsem z toho programování spíše demotivovaný. Asi to není úplně to co jsem si do toho představoval... Uvídíme dále, třeba mě
#to začne více bavit s tím, jak se budou řešit "praktičtější věci". Samozřejmě to nijak nesouvisí s vámi jako lektory... Díky za zpětnou
#vazbu. Milan
