# Exo 2 TP 4

import tkinter as tk

#On créer une fenetre
root = tk.Tk()
root.title("Jeu de go")

# On créer un canvas (zone de dessin)
Hauteur = 700
Largeur = 700
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()

#Disque
def disque(x, y, rayon, couleur):
    p1 = (x - rayon, y - rayon)
    p2 = (x + rayon, y + rayon)
    Dessin.create_oval(p1, p2, width=0, fill=couleur)

#Initilisation du carré beige
delta = Hauteur/22
Dessin.create_rectangle(delta,delta,Largeur-delta, Hauteur-delta,fill='#C8A165')

#Création des lignes et colonnes
for i in range(2,21):
    Dessin.create_line((delta*2,delta*i),(delta*20,delta*i))
    Dessin.create_line((delta*i,delta*2),(delta*i,delta*20))

#étoiles
def étoiles(x,y):
    disque((x+1)*delta,(y+1)*delta,delta/6,'black')
    
for i in range(4,17,6):
    for j in range(4,17,6):
        étoiles(i,j)
        
#Place des pierres V1
def place_pierre_1(x,y,couleur):
    disque((x+1)*delta,(19-y+2)*delta, delta/2, couleur)
    
place_pierre_1(17,16,'black')
place_pierre_1(4,16,'white')
place_pierre_1(16,3,'black')
place_pierre_1(4,4,'red')
place_pierre_1(6,17,'black')

#Place des pierres V2
couleur = 'black'
def place_pierre_2(x,y):
    global couleur
    disque((x+1)*delta,(19-y+2)*delta, delta/2, couleur)
    if couleur == 'black':
        couleur = 'white'
    else:
        couleur = 'black'

#place_pierre_2(17,16)
#place_pierre_2(4,16)
#place_pierre_2(16,3)
#place_pierre_2(4,4)
#place_pierre_2(6,17)

root.mainloop()