import tkinter as tk
from math import *
from random import *

(Hauteur, Largeur) = (800, 1000)
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
        # Positions de la Terre et de la Lune
        (x1, y1) = rotation(x0, y0, 300, 50, 1/100, self.temps)
        (x2, y2) = rotation(x1, y1, 80, 12, 12/100, self.temps)        
        # Dessin dans l'ordre correct pour la profondeur
        if y0 >= y1:  # Terre en bas de l'ellipse
            disque(x1, y1, 20, 'blue')
            disque(x2, y2, 5, 'gray')
            disque(x0, y0, 40, 'yellow')
        else:  # Terre en haut de l'ellipse
            disque(x0, y0, 40, 'yellow')
            disque(x1, y1, 20, 'blue')
            disque(x2, y2, 5, 'gray')
        
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