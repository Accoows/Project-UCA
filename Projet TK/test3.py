import tkinter as tk
from math import *
from random import *

################# Idee à faire #####################
# Installation d'un curseur qui multiplie le temps 
# Choix d'un systeme solaire verticale ou horizontale
# Modification de la taille des planetes
# Ajouter au supprimer l'apparition d'une planete
# Ajouter du texte si possible sur les plantes 
# Ajouter une zone de légende pour les planètes
# Curseur pour faire un zoom si possible en augmentant la zone de rotation et la taille des planètes
###################################################

(Hauteur, Largeur) = (700, 1400)
root = tk.Tk()
root.title("Système solaire (sans png)")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='black')
Dessin.pack()

class État():
    
    def __init__(self):
        (L, H) = (Largeur, Hauteur)
        self.étoiles = [(randint(0, L), randint(0, H)) for e in range(1000)]
        self.temps = 0
        self.centre_x = Largeur//2
        self.centre_y = Hauteur//2
        self.rayon_base = 0

        self.modifvitesse_testeur = 8
        
        ############################
        #Soleil
        self.rayon_soleil = 60;
        #Terre
        self.rayon_terre = 20; self.rayon_x_terre = 200; self.rayon_y_terre = 40; self.vitesse_terre = (1/365)*self.modifvitesse_testeur;
        #Lune
        self.rayon_lune = 5; self.rayon_x_lune = 50; self.rayon_y_lune = 15; self.vitesse_lune = (1/27.3)*self.modifvitesse_testeur;
        #Mercure
        self.rayon_mercure = 10; self.rayon_x_mercure = 100; self.rayon_y_mercure = 40; self.vitesse_mercure = (1/88)*self.modifvitesse_testeur;
        #Venus
        self.rayon_venus = 15; self.rayon_x_venus = 150; self.rayon_y_venus = 40; self.vitesse_venus = (1/225)*self.modifvitesse_testeur;
        #Mars
        self.rayon_mars = None; self.rayon_x_mars = None; self.rayon_y_mars = None; self.vitesse_mars = None;
        #Jupiter
        self.rayon_jupiter = None; self.rayon_x_jupiter = None; self.rayon_y_jupiter = None; self.vitesse_jupiter = None;
        #Saturne
        self.rayon_saturne = None; self.rayon_x_saturne = None; self.rayon_y_saturne = None; self.vitesse_jupiter = None;
        #Uranus
        self.rayon_uranus = None; self.rayon_x_uranus = None; self.rayon_y_uranus = None; self.vitesse_saturne = None;
        #Neptune
        self.rayon_neptune = None; self.rayon_x_neptune = None ; self.rayon_y_neptune = None; self.vitesse_neptune = None;
        ############################

        self.pause = False
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all')
        
        #Affichage étoiles
        for (x, y) in self.étoiles:
            Dessin.create_rectangle((x-1, y-1), (x+1, y+1), fill='white')
        
        #Position Soleil
        (x0, y0) = (self.centre_x, self.centre_y)
        
        # Positions de la Terre et de la Lune
        (x1, y1) = rotation(x0, y0, self.rayon_x_terre, self.rayon_y_terre, self.vitesse_terre, self.temps)
        (x2, y2) = rotation(x1, y1, self.rayon_x_lune, self.rayon_y_lune, self.vitesse_lune, self.temps)
        # Position de Mercure
        (x3, y3) = rotation(x0, y0, self.rayon_x_mercure, self.rayon_y_mercure, self.vitesse_mercure, self.temps)
        # Position de Venus
        (x4, y4) = rotation(x0, y0, self.rayon_x_venus, self.rayon_y_venus, self.vitesse_venus, self.temps)

        
        # Profondeur Bas
        if y1 >= y0:                                         # Terre en bas de l'ellipse du Soleil
            disque(x0, y0, self.rayon_soleil, '#ECD600')      # Soleil par-dessus tout
            if y1 >= y2:                                     # Lune en bas de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, 'red')      # Lune ensuite
            disque(x1, y1, self.rayon_terre, '#0042FF')         # Terre d'abord                
            if y1 < y2:                                      # Lune en haut de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune derrière la Terre 
        #Profondeur Haut
        else:                                                # Terre en haut de l'ellipse du Soleil
            if y1 >= y2:                                     # Lune en bas de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune devant la Terre
            disque(x1, y1, self.rayon_terre, '#0042FF')         # Terre par-dessus le Soleil
            disque(x0, y0, self.rayon_soleil, '#ECD600')      # Soleil par-dessus la Terre
            if y1 < y2:                                      # Lune en haut de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune derrière la Terre
            disque(x0, y0, self.rayon_soleil, '#ECD600')

#
        ## Profondeur Venus -> Soleil
        #if y0 >= y4:
        #    disque(x4, y4, self.rayon_venus, '#C08115')
        #    disque(x0, y0, self.rayon_soleil, '#ECD600')
        #else:
        #    disque(x0, y0, self.rayon_soleil, '#ECD600')
        #    disque(x4, y4, self.rayon_venus, '#C08115')
    
            
#Timer
def tictac():
    if not état.pause:
        état.temps += 1
    état.affichage()
    Dessin.after(20, tictac)
    
#Déplacement ellipse
def rotation(x, y, rayon_x, rayon_y, w, t):
    return (x + rayon_x * cos(-t * w), y + rayon_y * sin(-t * w))

#Graphique planètes
def disque(x, y, r, couleur):
    p = (x + r, y + r)
    q = (x - r, y - r)
    Dessin.create_oval(p, q, fill=couleur)

#Fonction changement de taille des planètes
def modif_taille_planete(x):
    état.rayon_base = int(x)
    état.rayon_soleil = état.rayon_base
    état.rayon_terre = état.rayon_base // 4
    état.rayon_lune = état.rayon_base // 6
    état.rayon_mercure = état.rayon_base // 4
    état.rayon_venus = état.rayon_base // 4
    état.affichage()


#Fonction de pause (stop)
def pause(event):
    état.pause = not état.pause

#Curseur d'agrandissement   
curseur_taille = tk.Scale(root, orient="horizontal", length=Largeur,
                        label='Taille',command=modif_taille_planete,
                        from_=40, to=100)

curseur_taille.pack(side="left")



état = État()
tictac()
root.bind('<space>', pause)
root.mainloop()