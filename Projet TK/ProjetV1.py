import tkinter as tk
from math import *
from random import *

(Hauteur, Largeur) = (700, 1400)
root = tk.Tk()
root.title("Système solaire (sans png)")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='black')
Dessin.pack()

class État():
    
    def __init__(self):
        (L, H) = (Largeur, Hauteur)
        self.étoiles = [(randint(50, L), randint(50, H)) for e in range(300)]
        self.temps = 0
        self.centre_x = Largeur//2
        self.centre_y = Hauteur//2
        self.rayon_terre = 20 ; self.rayon_lune = 5 ; self.rayon_soleil = 40
        self.rayonx_terre = 300 ; self.rayony_terre = 40
        self.rayonx_lune = 80 ; self.rayony_lune = 12
        self.vitesse_terre = 1/100 ; self.vitesse_lune = 6/100
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all')
        
        #Affichage étoiles
        for (x, y) in self.étoiles:
            Dessin.create_rectangle((x-1, y-1), (x+1, y+1), fill='white')
        
        (x0, y0) = (self.centre_x, self.centre_y)
        # Positions de la Terre et de la Lune
        (x1, y1) = rotation(x0, y0, self.rayonx_terre, self.rayony_terre, self.vitesse_terre, self.temps)
        (x2, y2) = rotation(x1, y1, self.rayonx_lune, self.rayony_lune, self.vitesse_lune, self.temps)
        # Position de Mercure
        (x3, y3) = rotation(x0, y0, self.rayonx_terre, self.rayony_terre, self.vitesse_terre, self.temps)
        
        # Dessin dans l'ordre correct pour la profondeur
        if y1 >= y0:  # Terre en bas de l'ellipse du Soleil
            disque(x0, y0, self.rayon_soleil, 'yellow')  # Soleil par-dessus tout
            if y2 >= y1:  # Lune en bas de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, 'gray')  # Lune ensuite
            disque(x1, y1, self.rayon_terre, 'blue')  # Terre d'abord                
            if y2 < y1:  # Lune en haut de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, 'gray')  # Lune derrière la Terre
        else:  # Terre en haut de l'ellipse du Soleil
            if y2 >= y1:  # Lune en bas de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, 'gray')  # Lune devant la Terre
            disque(x1, y1, self.rayon_terre, 'blue') # Terre par-dessus le Soleil
            disque(x0, y0, self.rayon_soleil, 'yellow')  # Soleil par-dessus la Terre
            if y2 < y1:  # Lune en haut de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, 'gray')  # Lune derrière la Terre
            
def tictac():
    état.temps += 1
    état.affichage()
    Dessin.after(20, tictac)
    
def rotation(x, y, rayon_x, rayon_y, w, t):
    return (x + rayon_x * cos(-t * w), y + rayon_y * sin(-t * w))

def disque(x, y, r, couleur):
    p = (x + r, y + r)
    q = (x - r, y - r)
    Dessin.create_oval(p, q, fill=couleur)
    
def modif_taille_planete(x):
    état.rayon_soleil = int(x)
    état.rayon_terre = (int(x)/2)
    état.rayon_lune = (int(x)/6)
    état.affichage()

#Curseur d'aggrandissement   
curseur_systeme = tk.Scale(root, orient="horizontal", length=Largeur,
                        label='Taille',command=modif_taille_planete,
                        from_=20, to=100)

curseur_systeme.pack(side="left")



état = État()
tictac()
root.mainloop()