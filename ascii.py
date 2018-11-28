import numpy as np

positionvec_1 = [[2.84,1.42],[1.42,0.72]]
positionvec_2 = [[2.2,1.4],[0.4,0.1]]


def ascii_add (posarraybal):
    array = np.array(posarraybal)
    x_a=  (array[:,0] / 2.84) * 18
    y_a = (array[:, 1] / 1.42) * 70
    x_norm = np.round(x_a) - 1
    y_norm =np.round(y_a)
    m_stack = np.stack((x_norm, y_norm), axis=-1)
    return(m_stack)


def ascii_plot_init (bal1,bal2):
    ascii_plot = []
    print("+" +"-" * 70 + "+ ")
    for i in range(18):
        ascii_plot.append("|")
        for i in range(70):
            ascii_plot.append(" ")

        ascii_plot.append("| \n")

    for i in ascii_add(bal1):
        x = i.tolist()
        ascii_plot[(18 -int(x[0])) * 72 + int(x[1])] = "o"

    for i in ascii_add(bal2):
        x = i.tolist()
        ascii_plot[(18-int(x[0])) * 72 + int(x[1]) ] = "x"



    print("".join(ascii_plot))
    print("+" +"-" * 70 + "+ ")
ascii_plot_init(positionvec_1, positionvec_2)
