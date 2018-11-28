#!/usr/bin/env python3

import matplotlib.pyplot as plt


def plot_tafel(tafel):
    """
    Neemt een object van type Table waarvan de simulatie
    reeds is uitgevoerd en retourneert plot van tafel"""
    fig = plt.figure()
    #fig.tightlayout()
    ax = fig.add_subplot(111, aspect="equal")
    ax.axis('off')
    ax.hlines(0,0,2.84,colors="r")
    ax.hlines(1.42,0,2.84,colors="r")
    ax.vlines(0,0,1.42,colors="r")
    ax.vlines(2.84,0,1.42,colors="r")
    ax.set_xlim(0,tafel.dim[0])
    ax.set_ylim(0,tafel.dim[1])
    for gat in tafel.holes:
        ax.add_artist(plt.Rectangle(gat[:2], gat[2], gat[3],
            facecolor="gray"))
    for ball in tafel.balls:
        for pos in ball.pos:
            ax.add_artist(plt.Circle(xy=pos, radius=tafel.balls[0].radius, color=ball.col))
    for c in tafel.collisions:
        x,y = c
        ax.plot([x-0.03, x+0.03], [y-0.03, y+0.03], 'r-')
        ax.plot([x-0.03, x+0.03], [y+0.03, y-0.03], 'r-')
    v = ["0", "0"]
    for i in (0,1):
        if any(tafel.balls[i].v[0]):
            v[i] = "({:0.3f}, {:0.3f})".format(
                    tafel.balls[i].v[0,0],
                    tafel.balls[i].v[0,1]
                    )
    ax.set_title("Bal 1 startpositie ({:0.3f}, {:0.3f}), snelheid {} m/s\n" \
            "Bal 2 startpositie ({:0.3f}, {:0.3f}), snelheid {} m/s".format(
                     tafel.balls[0].pos[0,0],
                     tafel.balls[0].pos[0,1],
                     v[0],
                     tafel.balls[1].pos[0,0],
                     tafel.balls[1].pos[0,1],
                     v[1]))
    return fig, ax

