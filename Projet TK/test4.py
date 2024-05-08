import tkinter as tk
from math import *
from random import *

################# Idee à faire #####################
# Installation d'un curseur qui multiplie le temps 
# Modification de la taille des planetes et distance avec le soleil OK
# Ajouter au supprimer l'apparition d'une planete OK
# Ajouter du texte si possible sur les planètes 
# Ajouter une zone de légende pour les planètes
# Curseur pour faire un zoom si possible en augmentant la zone de rotation et la taille des planètes OK
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
        self.centre_x = Largeur // 2
        self.centre_y = Hauteur // 2
        self.rayon_base = 0

        self.modif_vitesse = 1

        ############################
        #Soleil
        self.rayon_soleil = 20
        #Mercure
        self.rayon_mercure = (self.rayon_soleil * 0.22)
        self.rayon_x_mercure = (self.rayon_soleil * 3)
        self.rayon_y_mercure = (self.rayon_soleil * 1.05)
        self.vitesse_mercure = (1 / 88) * self.modif_vitesse
        #Venus
        self.rayon_venus = (self.rayon_soleil * 0.28)
        self.rayon_x_venus = (self.rayon_soleil * 6)
        self.rayon_y_venus = (self.rayon_soleil * 1.40)
        self.vitesse_venus = (1 / 225) * self.modif_vitesse
        #Terre
        self.rayon_terre = (self.rayon_soleil * 0.3)
        self.rayon_x_terre = (self.rayon_soleil * 8)
        self.rayon_y_terre = (self.rayon_soleil * 2)
        self.vitesse_terre = (1 / 365) * self.modif_vitesse
        #Lune
        self.rayon_lune = (self.rayon_soleil * 0.1)
        self.rayon_x_lune = (self.rayon_soleil * 1.1)
        self.rayon_y_lune = (self.rayon_soleil * 0.3)
        self.vitesse_lune = (1 / 27.3) * self.modif_vitesse
        #Mars
        self.rayon_mars = (self.rayon_soleil * 0.20)
        self.rayon_x_mars = (self.rayon_soleil * 10)
        self.rayon_y_mars = (self.rayon_soleil * 3)
        self.vitesse_mars = (1 / 687) * self.modif_vitesse
        #Jupiter
        self.rayon_jupiter = (self.rayon_soleil * 0.6)
        self.rayon_x_jupiter = (self.rayon_soleil * 12)
        self.rayon_y_jupiter = (self.rayon_soleil * 4)
        self.vitesse_jupiter = (1 / 4335) * self.modif_vitesse * 10
        #Saturne
        self.rayon_saturne = (self.rayon_soleil * 0.5)
        self.rayon_x_saturne = (self.rayon_soleil * 14)
        self.rayon_y_saturne = (self.rayon_soleil * 5)
        self.vitesse_saturne = (1 / 10757) * self.modif_vitesse * 10
        #Uranus
        self.rayon_uranus = (self.rayon_soleil * 0.45)
        self.rayon_x_uranus = (self.rayon_soleil * 16)
        self.rayon_y_uranus = (self.rayon_soleil * 6)
        self.vitesse_uranus = (1 / 30687) * self.modif_vitesse * 10
        #Neptune
        self.rayon_neptune = (self.rayon_soleil * 0.45)
        self.rayon_x_neptune = (self.rayon_soleil * 18)
        self.rayon_y_neptune = (self.rayon_soleil * 7)
        self.vitesse_neptune = (1 / 60224) * self.modif_vitesse * 10
        ############################

        self.pause = False
        self.aff_mercure = True
        self.aff_venus = True
        self.aff_terre = True
        self.aff_mars = True
        self.aff_jupiter = True
        self.aff_saturne = True
        self.aff_uranus = True
        self.aff_neptune = True

        self.affichage()

    def affichage(self):
        Dessin.delete('all')

        #Affichage étoiles
        for (x, y) in self.étoiles:
            Dessin.create_rectangle((x - 1, y - 1), (x + 1, y + 1), fill='white')

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
        # Position de Mars
        (x5, y5) = rotation(x0, y0, self.rayon_x_mars, self.rayon_y_mars, self.vitesse_mars, self.temps)
        # Position de Jupiter
        (x6, y6) = rotation(x0, y0, self.rayon_x_jupiter, self.rayon_y_jupiter, self.vitesse_jupiter, self.temps)
        # Position de Saturne
        (x7, y7) = rotation(x0, y0, self.rayon_x_saturne, self.rayon_y_saturne, self.vitesse_saturne, self.temps)
        # Position d'Uranus
        (x8, y8) = rotation(x0, y0, self.rayon_x_uranus, self.rayon_y_uranus, self.vitesse_uranus, self.temps)
        # Position de Neptune
        (x9, y9) = rotation(x0, y0, self.rayon_x_neptune, self.rayon_y_neptune, self.vitesse_neptune, self.temps)

        # Profondeur Mercure -> Soleil
        if y0 >= y1:
            if self.aff_mercure:
                disque(x1, y1, self.rayon_mercure, '#797C68')
            disque(x0, y0, self.rayon_soleil, '#ECD600')
        else:
            disque(x0, y0, self.rayon_soleil, '#ECD600')
            if self.aff_mercure:
                disque(x1, y1, self.rayon_mercure, '#797C68')
        if self.aff_venus:
            disque(x2, y2, self.rayon_venus, '#FF4D00')
        #
        if self.aff_terre:
            if y3 >= y4:
                disque(x4, y4, self.rayon_lune, '#A4A4A4')
            disque(x3, y3, self.rayon_terre, '#0042FF')
            if y3 < y4:
                disque(x4, y4, self.rayon_lune, '#A4A4A4')
        if self.aff_mars:
            disque(x5, y5, self.rayon_mars, '#C80101')
        if self.aff_jupiter:
            disque(x6, y6, self.rayon_jupiter, '#dc6e37')
        if self.aff_saturne:
            disque(x7, y7, self.rayon_saturne, couleur='#ffdead')
        if self.aff_uranus:
            disque(x8, y8, self.rayon_uranus, couleur='#c0d6e4')
        if self.aff_neptune:
            disque(x9, y9, self.rayon_neptune, couleur='#0049bb')


#############################################################################

#Timer
def tictac():
    if état.pause:
        état.temps += 1
    état.affichage()
    Dessin.after(10, tictac)


#Déplacement ellipse
def rotation(x, y, rayon_x, rayon_y, w, t):
    return x + rayon_x * cos(-t * w), y + rayon_y * sin(-t * w)


#Graphique planètes
def disque(x, y, r, couleur):
    p = (x + r, y + r)
    q = (x - r, y - r)
    Dessin.create_oval(p, q, fill=couleur)


#Fonction changement de taille des planètes
def modif_taille_planete(x):
    état.rayon_base = int(x)
    état.rayon_soleil = état.rayon_base

    état.rayon_mercure = (état.rayon_base * 0.22)
    état.rayon_x_mercure = (état.rayon_base * 3)
    état.rayon_y_mercure = (état.rayon_base * 1.05)

    état.rayon_venus = (état.rayon_base * 0.28)
    état.rayon_x_venus = (état.rayon_base * 6)
    état.rayon_y_venus = (état.rayon_base * 1.40)

    état.rayon_terre = (état.rayon_base * 0.3)
    état.rayon_x_terre = (état.rayon_base * 8)
    état.rayon_y_terre = (état.rayon_base * 2)

    état.rayon_lune = (état.rayon_base * 0.1)
    état.rayon_x_lune = (état.rayon_base * 1.1)
    état.rayon_y_lune = (état.rayon_base * 0.3)

    état.rayon_mars = (état.rayon_base * 0.20)
    état.rayon_x_mars = (état.rayon_base * 10)
    état.rayon_y_mars = (état.rayon_base * 3)

    état.rayon_jupiter = (état.rayon_base * 0.6)
    état.rayon_x_jupiter = (état.rayon_base * 12)
    état.rayon_y_jupiter = (état.rayon_base * 4)

    état.rayon_saturne = (état.rayon_base * 0.5)
    état.rayon_x_saturne = (état.rayon_base * 14)
    état.rayon_y_saturne = (état.rayon_base * 5)

    état.rayon_uranus = (état.rayon_base * 0.45)
    état.rayon_x_uranus = (état.rayon_base * 16)
    état.rayon_y_uranus = (état.rayon_base * 6)

    état.rayon_neptune = (état.rayon_base * 0.45)
    état.rayon_x_neptune = (état.rayon_base * 18)
    état.rayon_y_neptune = (état.rayon_base * 7)

    état.affichage()


#Fonction de pause (stop)
var_on_off = False
def pause(event):
    état.pause = not état.pause
def btn_pause():
    état.pause = not état.pause

def vitesse_planete(x):
    état.modif_vitesse = int(x)
    état.vitesse_mercure = (1 / 88) * état.modif_vitesse
    état.vitesse_venus = (1 / 225) * état.modif_vitesse
    état.vitesse_terre = (1 / 365) * état.modif_vitesse
    état.vitesse_lune = (1 / 27.3) * état.modif_vitesse
    état.vitesse_mars = (1 / 687) * état.modif_vitesse
    état.vitesse_jupiter = (1 / 4335) * état.modif_vitesse
    état.vitesse_saturne = (1 / 10757) * état.modif_vitesse
    état.vitesse_uranus = (1 / 30687) * état.modif_vitesse
    état.vitesse_neptune = (1 / 60224) * état.modif_vitesse
    état.affichage()


#   Event Clavier 'D,F,G,H,J,K,L,M'
def aff_mercure(event): état.aff_mercure = not état.aff_mercure
def aff_venus(event): état.aff_venus = not état.aff_venus
def aff_terre(event): état.aff_terre = not état.aff_terre
def aff_mars(event): état.aff_mars = not état.aff_mars
def aff_jupiter(event): état.aff_jupiter = not état.aff_jupiter
def aff_saturne(event): état.aff_saturne = not état.aff_saturne
def aff_uranus(event): état.aff_uranus = not état.aff_uranus
def aff_neptune(event): état.aff_neptune = not état.aff_neptune

#   Event Boutons Settings
def btn_aff_mercure(): état.aff_mercure = not état.aff_mercure
def btn_aff_venus(): état.aff_venus = not état.aff_venus
def btn_aff_terre(): état.aff_terre = not état.aff_terre
def btn_aff_mars(): état.aff_mars = not état.aff_mars
def btn_aff_jupiter(): état.aff_jupiter = not état.aff_jupiter
def btn_aff_saturne(): état.aff_saturne = not état.aff_saturne
def btn_aff_uranus(): état.aff_uranus = not état.aff_uranus
def btn_aff_neptune(): état.aff_neptune = not état.aff_neptune


#Curseur d'agrandissement
# curseur_taille = tk.Scale(root, orient="horizontal", length=Largeur,
#                           label='Taille', command=modif_taille_planete,
#                           from_=20, to=60)
#
# curseur_taille.pack(side="left")


#   Toplevel / Nouvelle fenêtre 'Settings'
def settings():
    win = tk.Toplevel()
    win.title("Settings")
    win.geometry("600x400")

    #   Curseur de taille
    curseur_taille = tk.Scale(win, orient="vertical", length=Hauteur,
                              label='Taille', command=modif_taille_planete,
                              from_=20, to=35)

    curseur_taille.pack(side="left")

    #   Texte boutons planètes
    text_label = tk.Label(win, text='Touches de paramétrage', font=("Courier", 11))
    text_label.place(x=370, y=30)
    text_mercure = tk.Label(win, text='<d>  ON/OFF Mercure', font=("Courier", 11))
    text_mercure.place(x=380, y=80)
    text_venus = tk.Label(win, text='<f>  ON/OFF Venus', font=("Courier", 11))
    text_venus.place(x=380, y=100)
    text_terre = tk.Label(win, text='<g>  ON/OFF Terre', font=("Courier", 11))
    text_terre.place(x=380, y=120)
    text_mars = tk.Label(win, text='<h>  ON/OFF Mars', font=("Courier", 11))
    text_mars.place(x=380, y=140)
    text_jupiter = tk.Label(win, text='<j>  ON/OFF Jupiter', font=("Courier", 11))
    text_jupiter.place(x=380, y=160)
    text_saturne = tk.Label(win, text='<k>  ON/OFF Saturne', font=("Courier", 11))
    text_saturne.place(x=380, y=180)
    text_uranus = tk.Label(win, text='<l>  ON/OFF Uranus', font=("Courier", 11))
    text_uranus.place(x=380, y=200)
    text_neptune = tk.Label(win, text='<m>  ON/OFF Neptune', font=("Courier", 11))
    text_neptune.place(x=380, y=220)
    text_pause = tk.Label(win, text='<space>  ON/OFF Système', font=("Courier", 10))
    text_pause.place(x=380, y=260)
    text_neptune = tk.Label(win, text="(En dehors de 'Settings')", font=("Courier", 10))
    text_neptune.place(x=380, y=280)

    #   Boutons d'affichage pour les planètes
    Btn_aff_mercure = tk.Button(win, text='Mercure', height=2, width=10, bg='#797C68', command=btn_aff_mercure)
    Btn_aff_mercure.place(x=80, y=140)
    Btn_aff_venus = tk.Button(win, text='Venus', height=2, width=10, bg='#FF4D00', command=btn_aff_venus)
    Btn_aff_venus.place(x=170, y=140)
    Btn_aff_terre = tk.Button(win, text='Terre', height=2, width=10, bg='#0042FF', command=btn_aff_terre)
    Btn_aff_terre.place(x=260, y=140)
    Btn_aff_mars = tk.Button(win, text='Mars', height=2, width=10, bg='#C80101', command=btn_aff_mars)
    Btn_aff_mars.place(x=80, y=190)
    Btn_aff_jupiter = tk.Button(win, text='Jupiter', height=2, width=10, bg='#dc6e37', command=btn_aff_jupiter)
    Btn_aff_jupiter.place(x=170, y=190)
    Btn_aff_saturne = tk.Button(win, text='Saturne', height=2, width=10, bg='#ffdead', command=btn_aff_saturne)
    Btn_aff_saturne.place(x=260, y=190)
    Btn_aff_uranus = tk.Button(win, text='Uranus', height=2, width=10, bg='#c0d6e4', command=btn_aff_uranus)
    Btn_aff_uranus.place(x=120, y=250)
    Btn_aff_neptune = tk.Button(win, text='Neptune', height=2, width=10, bg='#0049bb', command=btn_aff_neptune)
    Btn_aff_neptune.place(x=210, y=250)


    #   Curseur de modification de la vitesse des planètes
    curseur_vitesse = tk.Scale(win, orient="horizontal", length=300,
                               label='Vitesse', command=vitesse_planete,
                                from_=1, to=100)
    curseur_vitesse.place(x=50, y=320)

    #   Bouton ON/OFF
    #  Bug connu : Si la fenêtre est ouverte puis refermée,
    #  le bouton revient sur ON alors que le système est en marche.
    def change_var():
        global var_on_off
        if var_on_off:
            btn_pause()
            Btn_on_off.config(text='ON', bg='green')
            var_on_off = False
        else:
            btn_pause()
            Btn_on_off.config(text='OFF', bg='red')
            var_on_off = True

    Btn_on_off = tk.Button(win, text='ON', height=2, width=15, bg='green', command=change_var)
    Btn_on_off.place(x=150, y=40)


#   Boutons de paramétrages
Btn_settings = tk.Button(root, text='Settings', width=10, command=settings, bg='orange')
Btn_settings.pack()

#   Lancement/Arrêt du programme
état = État()
tictac()
root.bind('<space>', pause)
root.bind('d', aff_mercure)
root.bind('f', aff_venus)
root.bind('g', aff_terre)
root.bind('h', aff_mars)
root.bind('j', aff_jupiter)
root.bind('k', aff_saturne)
root.bind('l', aff_uranus)
root.bind('m', aff_neptune)
root.mainloop()
