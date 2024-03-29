#Exo 3 TP1

def reduction(n):
    if n >= 10 and n < 50:
        reduc_10 = n * (10/100)
        n = n - reduc_10
        return n
    elif n >= 50:
        reduc_20 = n * (20/100)
        n = n - reduc_20
        return n
    else:
        return n

assert reduction(89) == 71.2
assert reduction(2983) == 2386.4
assert reduction(5) == 5
assert reduction(18) == 16.2
assert reduction(43) == 38.7