#Exo 3 TP 3

def ascii():
#   n = ''
    for i in range(32,127):
#       n += str(i) + ' ' + str(chr(i))
        if i < 100:
            print(' ',end='')
        print(i, chr(i), sep=' ',end=' ')
        if i%8 == 0: #\n
            print('')
    print()
