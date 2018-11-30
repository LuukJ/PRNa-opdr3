import numpy as np

positionvec_1 = ([0.9,0.9],[0.3,1.2])
positionvec_2 = [[0.9,0.9],[0.3,1.2]]

""""Deze functie normaliseerd de positiearray van de ballen doormiddel van numpyfuncties en zet deze in de goede 
sequentie terug in een genormaliseerde array en returnd deze array. De functie word elke keer aangeroepen wanneer een
lijst van een bal genormaliseerd moet woren"""
def ascii_add_norm (posarraybal):
    array = np.array(posarraybal)
    x_a=  (array[:,0] / 2.48) * 70
    y_a = (array[:, 1] / 1.42) * 18
    x_norm = np.round(x_a) - 1
    y_norm =np.round(y_a)
    m_stack = np.stack((x_norm, y_norm), axis=-1)
    returnedlist = m_stack.tolist()
    return(returnedlist)

"""Dit is de hoofdfunctie van de asciiplot. Deze genereerd een 1 dementionale array waarin met een rekensom alle 
 posities van de ballen op hun goede plek gesubstitueerd kunnen worden. """
def ascii_plot_init (bal1,bal2):
    ascii_plot = []
    print("+" +"-" * 70 + "+ ")
    for i in range(18):
        ascii_plot.append("|")
        for i in range(70):
            ascii_plot.append(" ")

        ascii_plot.append("| \n")


    """plaatst de positiecoordinaten van de 1e bal in het asciiplot doormiddel van een rekenom die het nummer van de n-de 
    rij en n-de kolom bepaald van dit coordinaat en omzet naar een positie in een array"""
    for i in ascii_add_norm(bal1):
        ascii_plot[(18 -int(i[1])) * 72 + int(i[0]) -1] = "o"

    """plaatst de positiecoordinaten van de 1e bal in het asciiplot doormiddel van een rekenom die het nummer van de n-de 
        rij en n-de kolom bepaald van dit coordinaat en omzet naar een positie in een array. Hiervoor check het eerst
        of er in de vervangende positie al een karakter staat en als dat zo is deze veranderd in een plusje"""
    for i in ascii_add_norm(bal2):

        if ascii_plot[(18-int(i[1])) * 72 + int(i[0])  -1] == "o":
            ascii_plot[(18-int(i[1])) * 72 + int(i[0])  -1] = "+"
        else:
            ascii_plot[(18-int(i[1])) * 72 + int(i[0])  -1] = "x"

    print("".join(ascii_plot))
    print("\033[F"+"+" +"-" * 70 + "+ ")


ascii_plot_init(positionvec_1, positionvec_2)
