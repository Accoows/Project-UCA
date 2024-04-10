#Exo 1 TP 9

import tkinter as tk
from math import *


(Hauteur,Largeur) = (300,300)
root = tk.Tk()
root.title("Exprimons nos émotions")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='white')
Dessin.pack()

def disque(x,y,r,couleur):
    p = (x+r,y+r)
    q = (x-r,y-r)
    Dessin.create_oval(p,q,fill=couleur)

class État():
    
    def __init__(self):
        self.yeux=20
        self.heureux = True
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all')
        # Tête
        (xt,yt)=(Largeur/2,Hauteur/2)
        Rt=Hauteur*.9/2
        disque(xt,yt,Rt,'yellow')
        # Œil droit    
        (xd,yd)=(2*Largeur/3,Hauteur/3)
        disque(xd,yd,self.yeux,'black')
        # Œil gauche   
        (xg,yg)=(Largeur/3,Hauteur/3)
        disque(xg,yg,self.yeux,'black')
        # Bouche
        (xe,ye)=(Largeur/2,2*Hauteur/3)
        (Rex,Rey)= (40,30)
        Dessin.create_oval(xe-Rex,ye-Rey,xe+Rex,ye+Rey,fill='yellow',width=5)
        if self.heureux:
            h = -20
        else:
            h = 20
        (xr,yr)=(Largeur/2,2*Hauteur/3+h)
        (Rrx,Rry)=(70,20)
        Dessin.create_rectangle(xr-Rrx,yr-Rry,xr+Rrx,yr+Rry,fill='yellow',width=0)
        
état=État()
        
def est_heureux():
        état.heureux = True
        état.affichage()
        
def pas_heureux():
        état.heureux = False
        état.affichage()
        
def change_taille(x):
    état.yeux=int(x)
    état.affichage()
        
bouton1= tk.Button(root,text="Heureux",command=est_heureux, width=20)
bouton2= tk.Button(root,text="Pas Heureux",command=pas_heureux, width=20)
curseur = tk.Scale(root, orient="horizontal", length=Largeur,
                   label='Epaisseur',command=change_taille,
                   from_=1, to=50)

curseur.set(état.yeux)

bouton1.pack()
bouton2.pack()
curseur.pack()

root.mainloop()