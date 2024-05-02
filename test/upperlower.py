def testupper(phrase):
    majuscule = ''
    minuscule = ''
    for i in range(len(phrase)):
        if ord(phrase[i]) >= ord('A') and ord(phrase[i]) <= ord('Z'):
            majuscule += phrase[i]
        else:
            minuscule += phrase[i]
    print(majuscule,minuscule,sep='\n')

testupper("qzeqzeqzeqze")