import tkinter as tk
from math import *
from random import *

(Hauteur, Largeur) = (800, 800)
root = tk.Tk()
root.title("Révolution")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='black')
Dessin.pack()

class État():
    
    def __init__(self):
        (L, H) = (Largeur, Hauteur)
        self.étoiles = [(randint(0, L), randint(0, H)) for e in range(200)]
        self.temps = 0
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all')
        for (x, y) in self.étoiles:
            Dessin.create_rectangle((x-1, y-1), (x+1, y+1), fill='white')
        
        (x0, y0) = (Largeur//2, Hauteur//2)
        # La Terre, tournant sur une ellipse
        (x1, y1) = rotation(x0, y0, 300, 50, 1/100, self.temps)
        # La Lune, tournant également sur une petite ellipse
        (x2, y2) = rotation(x1, y1, 80, 60, 12/100, self.temps)
        disque(x1, y1, 40, 'blue')
        disque(x2, y2, 10, 'gray')
        # Le Soleil
        disque(x0, y0, 80, 'yellow')
        
def tictac():
    état.temps += 1
    état.affichage()
    Dessin.after(10, tictac)
    
def rotation(x, y, rx, ry, w, t):
    return (x + rx * cos(-t * w), y + ry * sin(-t * w))

def disque(x, y, r, couleur):
    p = (x + r, y + r)
    q = (x - r, y - r)
    Dessin.create_oval(p, q, fill=couleur)

état = État()
tictac()
root.mainloop()