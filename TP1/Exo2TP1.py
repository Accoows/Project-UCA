r = 0
m = int(input("Entrer un nombre entre 0 et 999 :"))

c = m%10
r = r*10 + c
m = m//10
print(c)

c = m%10
r = r*10 + c
m = m//10
print(c)

c = m%10
r = r*10 + c
m = m//10

print(c)
print(r)