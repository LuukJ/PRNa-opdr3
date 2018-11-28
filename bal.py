import numpy as np


class Bal:
    def __init__(self, pos, v_init, N, dt, colour=(0,1,0,1)):
        self.dt = dt
        self.pos = np.zeros((N, 2))
        self.pos[0] = pos
        self.v = np.zeros((N, 2))
        self.v[0] = v_init
        self.m = 0.220  # kilogram
        self.mu = 0.015  # rolweerstand
        self.radius = 0.03075  # meter
        self.in_gat = False
        self.col = colour

    def snelheid(self, i):
        """Geef snelheid voor simulatie-stap i"""
        return self.v[i]

    def geef_snelheden(self):
        """Levert een 1-d array van genormaliseerde snelheden op, handig
        voor de plot met balsnelheden"""
        return np.linalg.norm(self.v, axis=1)

    def bereken_positie(self, i):
        """Bereken positie voor stap i, op basis van huidige snelheid"""
        return self.pos[i-1] + self.v[i-1]*self.dt

    def bereken_snelheid(self, i):
        """Bereken snelheid voor stap i, door de rolweerstand zoals
        gegeven in de opdracht toe te passen."""
        if not any(self.v[i-1]):
            return np.copy(self.v[i-1])
        Delta_v = -1*self.mu*9.81*self.dt*self.v[i-1]/np.linalg.norm(self.v[i-1])
        return self.v[i-1] + Delta_v

    def let_op_randen(self, i, tafel):
        """Zorgt dat dat bal tegen de randen stuitert"""
        richting = np.array([1,1])
        for j in (0,1):
            if ((self.v[i-1, j] < 0 and self.radius >= self.pos[i-1, j]) or 
                    (self.v[i-1, j] > 0 and self.pos[i-1, j] >= tafel.dim[j] - self.radius)):
                richting[j] *= -1
        return richting
