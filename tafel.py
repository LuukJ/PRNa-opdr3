import numpy as np
from bal import *


class Tafel:
    def __init__(self, dim, N, dt):
        self.dim = dim  # grootte in (x, y)
        self.N = N
        self.dt = dt
        # Gaten in een tuple maakt aanpassing of uitbreiding makkelijker
        self.holes = (  # gaten in de vorm (x, y, x-grootte, y-grootte)
                (0,0,0.065,0.065),  # linksonder
                (0, dim[1]-0.065, 0.065, 0.065),  # linksboven
                ((dim[0]-0.065)/2, dim[1]-0.065, 0.065, 0.065),  # middenboven
                ((dim[0]-0.065)/2, 0, 0.065, 0.065),  # middenonder
                (dim[0]-0.065, 0, 0.065, 0.065),  # rechtsonder
                (dim[0]-0.065, dim[1]-0.065, 0.065, 0.065)  # rechtsboven
            )
        self.clear()

    def clear(self):
        self.balls = []
        self.collisions = []


    def register_ball(self, pos, v_init, colour=(0,1,0,1)):
        """Voeg bal toe aan tafel"""
        self.balls.append(Bal(pos, v_init, self.N, self.dt, colour))

    
    def bal_in_gat(self, bal, i):
        """Retourneert True als de bal in een gat valt"""
        for gat in self.holes:
            x, y, b, h = gat
            pos = bal.pos[i]
            # Snelheid laag genoeg en bal geheel boven gat
            if (np.linalg.norm(bal.snelheid(i)) <=0.125 and
                    pos[0] + bal.radius <= x+b and
                    x <= pos[0] - bal.radius and
                    pos[1] + bal.radius <= y+h and
                    y <= pos[1] - bal.radius):
                return True
        return False




    def detect_collision(self, ball, i):
        """
        detecteer botsingen tussen ballen en pas de snelheden dezer ballen aan.
        retourneert ook een list met botspunten teneinde het tekenen
        van kruisjes op botspunten.
        Kan bij heel lage snelheden misgaan
        """
        collisions = []
        for other in self.balls:
            if other == ball:
                continue
            p1, p2 = ball.pos[i], other.pos[i]
            v1, v2 = ball.v[i], other.v[i]
            if  np.linalg.norm(p1 - p2) < (ball.radius + other.radius):
                collisions.append(np.mean((p1,p2), axis=0))
                n = (p1 - p2)/np.linalg.norm(p1-p2)  # Unit normaalvector
                t = np.array([n[1]*-1, n[0]])  # Unit v langs raaklijn
                # Splits in normaal- en raaklijncomponenten
                v_n1 = np.dot(n, v1)
                v_n2 = np.dot(n, v2)
                v_t1 = np.dot(t, v1)
                v_t2 = np.dot(t, v2)
                new_v1 = np.dot(v_n2, n) + np.dot(v_t1, t) 
                new_v2 = np.dot(v_n1, n) + np.dot(v_t2, t)
                ball.v[i] = new_v1
                other.v[i] = new_v2
        return collisions


    def simulate(self):
        for i in range(1, self.N):
            for ball in self.balls:
                if ball.in_gat:
                    continue
                v = ball.bereken_snelheid(i)
                v *= ball.let_op_randen(i, self)
                pos = ball.bereken_positie(i)
                ball.v[i] = v
                ball.pos[i] = pos
                self.collisions += self.detect_collision(ball, i)
                if self.bal_in_gat(ball, i):
                    ball.in_gat = True



