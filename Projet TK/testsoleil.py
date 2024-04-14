
from tkinter import *
from math import *
from random import *


(Hauteur,Largeur) = (800,1400)
root = Tk()
root.title("Révolution")
Dessin = Canvas(root,height=Hauteur,width=Largeur,bg='black')
Dessin.pack()

imgfile = '../Projet TK/Soleil.png'
img = PhotoImage(file=imgfile)
img_2 = img.subsample(1,1)

image = Dessin.create_image(Largeur/2,Hauteur/2,image=img_2)

root.mainloop() # À mettre à la fin de chaque programme Tk