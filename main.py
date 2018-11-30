import numpy as np
import matplotlib.pyplot as plt
from tafel import Tafel
from plot_tafel import plot_tafel
from plot_snelheid import plot_snelheid
from ascii_plot import ASCII_plot


def hoofdmenu():
    while 1:  # herhalen tot afsluiten is gekozen
        modus = keuze("\nSelecteer een operatie",
                "Automatisch", "Handmatig", "Afsluiten")
        # Automatisch
        if modus == 1:
            automatisch()
        elif modus == 2:
            handmatig()
        else:
            return


def handmatig():
    while 1:
        try:
            N = int(input("Aantal simulatiestappen: "))
            break
        except ValueError:
            print("Voer natuurlijk getal in.")
    tafel = Tafel((2.84, 1.42), N, 0.05)
    print("\nDe tafel is {} bij {} meter.".format(tafel.dim[0], tafel.dim[1]))
    print("\nBal 1")
    pos, v_init = vraag_bal(tafel)
    tafel.register_ball(pos=pos, v_init=v_init, colour=(0, 0.5, 0, 1))  # Groen
    print("\nBal 2")
    pos, v_init = vraag_bal(tafel)
    tafel.register_ball(pos=pos, v_init=v_init, colour=(0, 0, 0, 1))    # Zwart
    tafel.simulate()
    modus = "x"
    while 1:
        modus = keuze("\nSelecteer een visualisatie",
                "Tafeloverzicht", "Snelheid-tijddiagram",
                "ASCII-tafeloverzicht", "Terug naar hoofdmenu")
        if modus == 1:
            fig, ax = plot_tafel(tafel)
            plt.show()
        elif modus == 2:
            fig, ax = plot_snelheid(tafel)
            plt.show()
        elif modus == 3:
            print(ASCII_plot(tafel))
        else:
            return


def automatisch():
    while 1:
        try:
            N = int(input("Aantal simulatiestappen: "))
            break
        except ValueError:
            print("Voer natuurlijk getal in.")
    tafel = Tafel((2.84,1.42), N, 0.05)
    while 1:
        try:
            filename = input("Invoerbestand: ")
            data = np.loadtxt(filename)
            pos = data[:,:2]
            v = data[:,2:]
            assert np.all(0.03075 < pos < tafel.dim-0.03075)
            break
        except FileNotFoundError:
            print("Bestand bestaat niet")







def vraag_bal(tafel):
    """
    Vraagt de gebruiker x, y, snelheid en hoek van een bal te geven
    en controleert of deze geldig zijn
    """
    radius = 0.03075
    print("Geef de volgende gegevens over de bal:")
    x = 0
    while 1:
        try:
            x = float(input("x in meter: "))
            assert radius < x < tafel.dim[0]-radius
            break
        except ValueError:
            print("Geen geldig getal.")
        except AssertionError:
            print("Geen geldige positie.")
    y = 0
    while 1:
        try:
            y = float(input("y in meter: "))
            assert radius < y < tafel.dim[1]-radius
            break
        except ValueError:
            print("Geen geldig getal.")
        except AssertionError:
            print("Geen geldige positie.")
    while 1:
        try:
            v = float(input("snelheid in m/s: "))
            break
        except ValueError:
            print("Geen geldig getal.")
    #  Vraag hoek alleen als v != 0
    if v:
        while 1:
            try:
                hoek = np.deg2rad(float(input("Hoek in graden "
                    "(tegen de klok in, 0 is rechts): ")))
                break
            except ValueError:
                print("Geen geldige hoek")
        v_x = np.cos(hoek)*v
        v_y = np.sin(hoek)*v
    else:
        v_x = v_y = 0
    return (x, y), (v_x, v_y)


def keuze(header, *keuzes):
    print(header)
    for n, keuze in enumerate(keuzes):
        print("[{}] {}".format(n+1, keuze))
    while 1:
        try:
            keuze = int(input("> "))
            assert 0 < keuze <= len(keuzes)
            break
        except:
            print("Geen geldige keuze.")
    return keuze



#TODO:
"""
automatisch (uitlezen bestand)
infoblok toevoegen.
"""

if __name__ == "__main__":
    hoofdmenu()
