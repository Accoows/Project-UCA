# from tkinter import *
# from math import *
# from random import *
#
#
# (Hauteur,Largeur) = (800,1400)
# root = Tk()
# root.title("Révolution")
# Dessin = Canvas(root,height=Hauteur,width=Largeur,bg='black')
# Dessin.pack()
#
# imgfile = '../Projet TK/Soleil.png'
# img = PhotoImage(file=imgfile)
# img_2 = img.subsample(1,1)
#
# image = Dessin.create_image(Largeur/2,Hauteur/2,image=img_2)
#
# root.mainloop() # À mettre à la fin de chaque programme Tk


#Fonction changement de vitesse des planètes
#def modif_vitesse(y):
#    vitesse_base = int(y)
#    état.vitesse_terre = (état.vitesse_terre * 2)
#    état.vitesse_lune = (état.vitesse_lune * 2)
#    état.vitesse_mercure = (état.vitesse_mercure * 2)
#    état.vitesse_venus = (état.vitesse_venus * 2)
#    état.vitesse_mars = (état.vitesse_mars + vitesse_base)
#    état.vitesse_jupiter = (état.vitesse_jupiter + vitesse_base)
#    état.vitesse_saturne = (état.vitesse_saturne + vitesse_base)
#    état.vitesse_neptune = (état.vitesse_neptune + vitesse_base)
#    état.affichage()
#
import tkinter as tk

(Hauteur, Largeur) = (800, 800)
root = tk.Tk()
root.title("Révolution")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='white')
Dessin.pack()

# def settings():
#     win = Toplevel()
#     win.title("Settings")
#     label = Label(win, text='Coucou')
#     label.pack()


bouton1 = tk.Button(root, text="Créer une nouvelle fenêtre", command=None)
bouton1.pack()
root.mainloop()

# root = Tk()
# def create():
#    win = Toplevel(root)
# root.geometry('200x100')
# btn = Button(root, text="Créer une nouvelle fenêtre", command = create)
# btn.pack()
# root.mainloop()
