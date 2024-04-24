import tkinter as tk
from math import *
from random import *

################# Idee à faire #####################
# Installation d'un curseur qui multiplie le temps 
# Modification de la taille des planetes et distance avec le soleil
# Ajouter au supprimer l'apparition d'une planete
# Ajouter du texte si possible sur les planètes 
# Ajouter une zone de légende pour les planètes
# Curseur pour faire un zoom si possible en augmentant la zone de rotation et la taille des planètes
#Affichage système solaire en 2006 avec Pluton et sans pluton (2014)
###################################################

(Hauteur, Largeur) = (700, 1400)
root = tk.Tk()
root.title("Système solaire")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='black')
Dessin.pack()

class État(): 
    
    def __init__(self):
        (L, H) = (Largeur, Hauteur)
        self.étoiles = [(randint(0, L), randint(0, H)) for e in range(600)]
        self.temps = 0
        self.centre_x = Largeur//2
        self.centre_y = Hauteur//2
        self.rayon_base = 0

        self.modifvitesse_testeur = 4
        
        ############################
        #Soleil
        self.rayon_soleil = 30;
        #Mercure
        self.rayon_mercure = (self.rayon_soleil*0.22); 
        self.rayon_x_mercure = 100; 
        self.rayon_y_mercure = 30; 
        self.vitesse_mercure = (1/88)*self.modifvitesse_testeur;
        #Venus
        self.rayon_venus = (self.rayon_soleil*0.28); 
        self.rayon_x_venus = 150; 
        self.rayon_y_venus = 60; 
        self.vitesse_venus = (1/225)*self.modifvitesse_testeur;
        #Terre
        self.rayon_terre = (self.rayon_soleil*0.3); 
        self.rayon_x_terre = 200; 
        self.rayon_y_terre = 90; 
        self.vitesse_terre = (1/365)*self.modifvitesse_testeur;
        #Lune
        self.rayon_lune = (self.rayon_soleil*0.1); 
        self.rayon_x_lune = 30; 
        self.rayon_y_lune = 10; 
        self.vitesse_lune = (1/27.3)*self.modifvitesse_testeur;
        #Mars
        self.rayon_mars = None; 
        self.rayon_x_mars = None; 
        self.rayon_y_mars = None; 
        self.vitesse_mars = None;
        #Jupiter
        self.rayon_jupiter = (self.rayon_soleil*0.6); 
        self.rayon_x_jupiter = None; 
        self.rayon_y_jupiter = None; 
        self.vitesse_jupiter = None;
        #Saturne
        self.rayon_saturne = None; 
        self.rayon_x_saturne = None; 
        self.rayon_y_saturne = None; 
        self.vitesse_saturne = None;
        #Uranus
        self.rayon_uranus = None; 
        self.rayon_x_uranus = None; 
        self.rayon_y_uranus = None; 
        self.vitesse_uranus = None;
        #Neptune
        self.rayon_neptune = None; 
        self.rayon_x_neptune = None; 
        self.rayon_y_neptune = None; 
        self.vitesse_neptune = None;
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

        # Position de Mercure
        (x1, y1) = rotation(x0, y0, self.rayon_x_mercure, self.rayon_y_mercure, self.vitesse_mercure, self.temps)
        # Position de Venus
        (x2, y2) = rotation(x0, y0, self.rayon_x_venus, self.rayon_y_venus, self.vitesse_venus, self.temps)
        # Positions de la Terre
        (x3, y3) = rotation(x0, y0, self.rayon_x_terre, self.rayon_y_terre, self.vitesse_terre, self.temps)
        # Position de la Lune
        (x4, y4) = rotation(x3, y3, self.rayon_x_lune, self.rayon_y_lune, self.vitesse_lune, self.temps)
        ## Position de Mars
        #(x5, y5) = rotation(x0, y0, self.rayon_x_mars, self.rayon_y_mars, self.vitesse_mars, self.temps)
        ## Position de Jupiter
        #(x6, y6) = rotation(x0, y0, self.rayon_x_jupiter, self.rayon_y_jupiter, self.vitesse_jupiter, self.temps)
        ## Position de Saturne
        #(x7, y7) = rotation(x0, y0, self.rayon_x_saturne, self.rayon_y_saturne, self.vitesse_saturne, self.temps)
        ## Position d'Uranus
        #(x8, y8) = rotation(x0, y0, self.rayon_x_uranus, self.rayon_y_uranus, self.vitesse_uranus, self.temps)
        ## Position de Neptune
        #(x9, y9) = rotation(x0, y0, self.rayon_x_neptune, self.rayon_y_neptune, self.vitesse_neptune, self.temps)

        
        # Profondeur Mercure -> Soleil
        if y0 >= y1:
            disque(x1, y1, self.rayon_mercure, '#797C68')
            disque(x0, y0, self.rayon_soleil, '#ECD600')
        else:
            disque(x0, y0, self.rayon_soleil, '#ECD600')
            disque(x1, y1, self.rayon_mercure, '#797C68')
        disque(x2, y2, self.rayon_venus, 'orange')
        #
        if y3 >= y4:
            disque(x4, y4, self.rayon_lune, '#A4A4A4')
        disque(x3, y3, self.rayon_terre, '#0042FF')
        if y3 < y4:
            disque(x4, y4, self.rayon_lune, '#A4A4A4')
 

        #Couleur
        #disque(x0, y0, self.rayon_soleil, '#ECD600')
        #disque(x2, y2, self.rayon_lune, '#A4A4A4')
        #disque(x1, y1, self.rayon_terre, '#0042FF')
        #disque(x3, y3, self.rayon_mercure, '#797C68')
    
            
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
    état.rayon_mercure = (état.rayon_base*0.22)
    état.rayon_venus = (état.rayon_base*0.28)
    état.rayon_terre = (état.rayon_base*0.3)
    état.rayon_lune = (état.rayon_base*0.1)
    état.affichage()


#Fonction de pause (stop)
def pause(event):
    état.pause = not état.pause

#Curseur d'agrandissement   
curseur_taille = tk.Scale(root, orient="horizontal", length=Largeur,
                        label='Taille',command=modif_taille_planete,
                        from_=30, to=100)

curseur_taille.pack(side="left")


état = État()
tictac()
root.bind('<space>', pause)
root.mainloop()