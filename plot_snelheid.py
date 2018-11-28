#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def plot_snelheid(tafel):
    """
    Neemt een object van type Table waarvan de simulatie
    reeds is uitgevoerd en retourneert plot van snelheid"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    t = np.cumsum([tafel.dt for _ in range(tafel.N)])
    ax.plot(t, tafel.balls[0].geef_snelheden(), "g-")
    ax.plot(t, tafel.balls[1].geef_snelheden(), "k--")
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
    ax.set_xlabel("Tijd (s)")
    ax.set_ylabel("Snelheid (m/s)")
    return fig, ax

