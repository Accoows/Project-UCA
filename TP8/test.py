def ajoute_vertical(M1,M2):
(n1,m1) = dimensions(M1)
(n2,m2) = dimensions(M2)
n = n1+n2
m = max(m1,m2)
# On crée une matrice de la bonne taille
M=matrice_false(n,m)
# On complète le haut de la matrice M avec M1
for i in range(n1):
for j in range(m1): # m1<m donc M[i][j] bien définie
M[i][j] = M1[i][j]
# On complète le bas de la matrice M avec M1
for i in range(n2): # i+n1 <= n2+n1 <= n donc M[i+n1] bien définie
for j in range(m2): # m2<m donc M[i][j] bien définie
M[i+n1][j] = M2[i][j]
return M