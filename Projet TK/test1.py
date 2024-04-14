
import tkinter as tk
from math import *
from random import *


(Hauteur,Largeur) = (800,800)
root = tk.Tk()
root.title("Révolution")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='black')
Dessin.pack()

class État():
    
    def __init__(self): # Deux attributs : le temps et une liste d'étoiles
        (L,H) = (Largeur,Hauteur)
        self.étoiles = [(randint(0,L),randint(0,H)) for e in range(200)]
        self.temps=0
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all') # On efface tout
        for (x,y) in self.étoiles: # Les étoiles
            Dessin.create_rectangle((x-1,y-1),(x+1,y+1),fill='white')
            
        (x0,y0) = (Largeur//2,Hauteur//2) # Le Soleil
        (x1,y1) = rotation(x0,y0,300,1/100,self.temps) # La Terre
        (x2,y2) = rotation(x1,y1, 80,12/100,self.temps) # La Lune
        disque(x0,y0,80,'yellow')
        disque(x1,y1,40,'blue')
        disque(x2,y2,10,'gray')
        
def tictac(): # Toutes les 20 ms, on change l'état et on l’affiche
    état.temps = état.temps+1
    état.affichage()
    Dessin.after(20,tictac)
    
def rotation(x,y,r,w,t):
# position d'un point à l'instant t, tournant sur
# un cercle de centre (x,y) et de rayon r avec une
# vitesse angulaire w
    return (x + r*cos(-t*w) , y + r*sin(-t*w))

def disque(x,y,r,couleur):
    p = (x+r,y+r)
    q = (x-r,y-r)
    Dessin.create_oval(p,q,fill=couleur)
    
état=État()
tictac() # On lance l'horloge
root.mainloop() # À mettre à la fin de chaque programme Tk