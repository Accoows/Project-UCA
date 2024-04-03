#Exo 5 TP 8

from pnm import *
from chat import chat_mignon

(n,m)=dimensions(chat_mignon)
python_mignon = matrice_vide(n,m)

for i in range(n):
    for j in range(m):
        (r,v,b) = chat_mignon[i][j]
        python_mignon[i][j] = (r//2, v//2, b//2)
        
voir_matrice(python_mignon)
