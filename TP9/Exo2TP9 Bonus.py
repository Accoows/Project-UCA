#Exo 2 TP9.py Bonus

import tkinter as tk
from math import *
import random


(Hauteur,Largeur) = (500,500)
root = tk.Tk()
root.title("Ballon")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='white')
Dessin.pack()

def ballon(x,y,r):
    p=(x-r,y-r) ; p1=(x-2.5*r,y-r) ; p2=(x+2.5*r,y-r)
    q=(x+r,y+r) ; q1=(x-.5*r, y+r) ; q2=x+.5*r, y+r
    Dessin.create_oval(p,q,fill='orange',outline='black',width=5)
    Dessin.create_line((x,y-r),(x,y+r),width=5)
    Dessin.create_arc(p1,q1, extent=80, start=-40, width=5,style='arc')
    Dessin.create_arc(p2,q2, extent=80, start=140, width=5,style='arc')

class État():
    
    def __init__(self):
        self.x = Largeur//2
        self.y = Hauteur//2
        self.vx = random.randint(1.0,3.0)
        self.vy = random.randint(1.0,3.0)
        self.rayon = 30
        self.pause = False
        self.mouseclick = False
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all')
        ballon(self.x,self.y,self.rayon)
    
état=État()
        
######

    
def pause(event):
    état.pause = not état.pause

def borner(x,a,b):
    return max(min(x,b),a)

def mousedeplace(event):
    if état.mouseclick:
        état.x = borner(event.x, état.rayon,Largeur-état.rayon)
        état.y = borner(event.y, état.rayon,Hauteur-état.rayon)

def changeclick(event):
    état.mouseclick = False
    
def deplacer(event):
    dx = état.x-event.x
    dy = état.y-event.y 
    if dx**2 + dy**2 < état.rayon**2:
        état.mouseclick = True
        état.x = event.x
        état.y = event.y
    
def tictac():
    if not état.pause and not état.mouseclick:
        if état.x + état.rayon >= Largeur or état.x - état.rayon <= 0:
            état.vx = -état.vx
        if état.y + état.rayon >= Hauteur or état.y - état.rayon <= 0:
            état.vy = -état.vy
        état.x = état.x + état.vx
        état.y = état.y + état.vy
    état.affichage()
    Dessin.after(10,tictac)
    
root.bind('<space>', pause)
root.bind('<ButtonRelease>', changeclick)
root.bind('<Motion>', mousedeplace)
root.bind('<Button>', deplacer)
tictac()
    
root.mainloop()