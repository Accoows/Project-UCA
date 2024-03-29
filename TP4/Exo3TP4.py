#Exo 3 TP 4

import tkinter as tk
import math

#On créer une fenetre
root = tk.Tk()
root.title("Test")

# On créer un canvas (zone de dessin)
Hauteur = 400
Largeur = 400
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()


#Affichage par pixel
def affiche_pixel(x,y,couleur):
    Dessin.create_rectangle(x,y,x,y,fill=couleur,outline='')
    
##Affichage du carré
#def tracer_carré():
#    xmin = 100
#    ymin = 100
#    xmax = xmin+200
#    ymax = ymin+200
#    for x in range(xmin,xmax+1):
#        affiche_pixel(x,ymin,'black') 
#        affiche_pixel(x,ymax,'black')
#    for y in range(ymin,ymax+1):
#        affiche_pixel(xmin,y,'black')
#        affiche_pixel(xmax,y,'black')
        
#tracer_carré()

##################
        
def entier_le_plus_proche(q):
    p = int(q)
    if q < p + 0.5:
        return p
    else:
        return p+1
        
#Algorithme v1
def affiche_segment_1(p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    for x in range(x1,x2+1):
        y = entier_le_plus_proche(a*x+b)
        affiche_pixel(x,y,'black')
        
        
root.mainloop()
    