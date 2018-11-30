import numpy as np


def ASCII_plot(tafel):
    dimensies = (70, 18)
    pos0, pos1 = tafel.balls[0].pos, tafel.balls[1].pos
    pos0 = (pos0 * dimensies / tafel.dim).astype("uint8")
    pos1 = (pos1 * dimensies / tafel.dim).astype("uint8")
    array = np.zeros(dimensies, dtype="uint8") 
    array[tuple(pos0.transpose())] += 1
    array[tuple(pos1.transpose())] += 2
    plot = np.tile(" ", dimensies)
    plot[array == 1] = "o"
    plot[array == 2] = "x"
    plot[array == 3] = "+"
    out = "+" + dimensies[0]*"-" + "+\n"
    for line in plot.transpose()[::-1]:
        out += "|{}|\n".format("".join(line))
    out += "+" + dimensies[0]*"-" + "+"
    return out




        
