#Version casse tête

import tkinter as tk

# On crée une fenêtre
root = tk.Tk()
root.title("Arc-en-ciel")

# On crée un canvas (zone de dessin)
Hauteur = 500
Largeur = 500
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg="#7799FF")
Dessin.pack()

#########

#Fonction création de disque
def cercle(x,y,rayon,épaisseur,couleur):
    p1 = (x-rayon,y-rayon)
    p2 = (x+rayon,y+rayon)
    (w,c) = (épaisseur,couleur)
    Dessin.create_oval(p1,p2,width=w,outline=c)
    
cercle(250,250,190,15,'#822FC3') #violet
cercle(250,250,175,15,'#400072') #violet foncé
cercle(250,250,160,15,'#000AB4') #bleu
cercle(250,250,145,15,'#00931F') #vert
cercle(250,250,130,15,'#D7EC00') #jaune
cercle(250,250,115,15,'#ECA900') #orange
cercle(250,250,100,15,'#EC2600') #rouge

#Création du carré vert
b1 = (0,250)
b2 = (500,500)
b='blue'
Dessin.create_rectangle(b1,b2,width=0,fill="#0B6400")
