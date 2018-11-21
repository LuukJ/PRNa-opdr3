import numpy as np
import sys
balpos = []
bal_v = []
tab_width = 2.84
tab_height = 1.42
aantal_ballen = 1


INFOBLOKJE = \
"""
+-------------------------------------------------------------------+
|Auteurs:                                                           |
+- Naam: Levi van Es                                                |
|  Studentnummer: 2115409                                           |
|  Jaar van aankomst: 2018                                          |
|  Studierichting: Natuurkunde                                      |
|                                                                   |
+- Naam: Luuk de Jong                                               |
|  Studentnummer: 2260018                                           |
|  Jaar van aankomst: 2018                                          |
|  Studierichting: Natuurkunde                                      |
+-------------------------------------------------------------------+
|Opgave: Biljard                                                     |
+-------------------------------------------------------------------+
|Inleverdatum: 30-11-2018                                           |
+-------------------------------------------------------------------+
|Instructie voor gebruiker:                                         |
|    Er wordt gevraagd wat het aantal stappen voor de simulatie is   |
|    en er wordt gevraagd wat het pad van het bestand is voor de    |
|   bestand waar de positie en richtingsvectoren uit worden gelezen |
|                                                                   |
+-------------------------------------------------------------------+
"""

print(INFOBLOKJE)



"""Deze functie genereerd bruikbare data voor de rest van het programma uit de invoerdata. Het neemt de input van de 
 gebruiker. Deze data word omgezet in positie en richtingsvectoren. De richtingsvectoren worden bepaald door de 
 richtingsvector van x en y uit te rekenen uit de snelheid en hoek waarin de bal zich beweegd."""

def balinvoer():
    print("De dementies van de tafel zijn", tab_width,"meter breed en ", tab_height, "meter hoog.")
    balpos_x = float(input("Geef de x-coordinaat van de bal"))
    balpos_y = float(input("Geef de y-coordinaat van de bal"))
    bal_ms = float(input("Geef de snelheid van de bal in m/s"))
    bal_ang= np.deg2rad(int(input("Geef de hoek van de bal in graden")))
    bal_v_y = np.sin(bal_ang) * bal_ms
    bal_v_x = np.cos(bal_ang) * bal_ms
    balpos.append(([balpos_x, balpos_y]))
    bal_v.append(([bal_v_x, bal_v_y]))


def initalisatie():
    modus = "x"
    while modus not in ("012"):
        modus= (input("Selecteer een operatie:\n[0] Automatisch\n[1] Handmatig\n[2] Afsluiten> "))

    stapcheck = False
    while not stapcheck:
        try:
            stappen = int(input("Gewenste simulatiestappen:"))
            print(stappen)
            stapcheck = True
        except ValueError:
            print("Dit is geen geldige input vul een geldige gehele waarde in.")

    if modus == "0":

        filecheck = False
        while not filecheck:
            try:
                filename = str(input("Geef de naam van het gewenste bestand:"))
                print(filename)
                open(filename).close()
                filecheck = True
            except FileNotFoundError:
                print("Dit is geen geldige input vul een geldige bestandsnaam in.")
        ## roept de functie aan waardoor de data word omgezet in vectoren
        file_vec_converter(filename)

        return stappen


    elif modus == "1":
        while not stapcheck:
            try:
                stappen = int(input("Gewenste simulatiestappen (geef een getal tussen 100 en 1000):"))
                print(stappen)
                stapcheck = True
            except ValueError:
                print("Dit is geen geldige input vul een geldige gehele waarde in.")
        for i in range(aantal_ballen):
            print("Geef de data van de",i + 1 ,"e bal")
            balinvoer()
        return stappen

    elif modus == "2":
        sys.exit()




### deze functie handeld het automatische deel van de code waarij de positie en richtingsvectoren worden uitgelezen uit
##  een vooringestelde file.
def file_vec_converter(filename):

    ##deze functie leest het invoerbestand uit en geeft 4 lijsen terug met in elk een andere positie of richtingsvector
    balpos_x, balpos_y, bal_v_x, bal_v_y = np.loadtxt(fname=filename, delimiter=' ', usecols=(0,1,2,3), unpack=True)

    ## deze for loop zorgt ervoor dat er twee 2-dementionale array word gemaakt van x en y waardes. De uitvoer is een
    ##snelheidsvector lijst en een positie lijst
    for i in range(len(balpos_x)):
        balpos.append([balpos_x[i], balpos_y[i]])
        bal_v.append([bal_v_x[i], bal_v_y[i]])
    ## deze voorwaarde checkt of alle positie waardes op de tafel vallen
    if np.any(balpos_x >= tab_width) or np.any(balpos_y >= tab_height) or np.any(balpos_y <= 0) or np.any(balpos_x <= 0):
        print("Een van de waardes valt buiten de parameters van de tafel. Zorg ervoor dat alle waardes tussen x<",tab_width, " en y <", tab_height,"vallen")
        initalisatie()


## Dit stukje code is essentiel voor het starten van de code en het definieren van de stappen
stappen = initalisatie()

#### om later mee te werken heb ik deze variablen gedefinieerd zodat het makkelijk samen te voegen is met de rest van de code
print(balpos)
print(bal_v)
print(stappen)

