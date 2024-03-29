#Exo 4 TP 3

def justification_à_gauche(s,n):
    k = 0           #compteur
    m = ''          
    for i in range(len(s)):
        if k > n : #retour à la ligne
            print()
            k = len(m)
        if s[i] == ' ': #espace
            print(m, end=' ')
            m = ''
        else:
            m = m + s[i]
        k = k + 1
    print(m)
    
    



justification_à_gauche("Mais au lieu de la simplicité, c’est le faste que je mettais au plus haut rang, si, après que j’avais forcé Françoise, qui n’en pouvait plus et disait que les jambes « lui rentraient », à faire les cent pas pendant une heure, je voyais enfin, débouchant de l’allée qui vient de la Porte Dauphine – image pour moi d’un prestige royal, d’une arrivée souveraine telle qu’aucune reine véritable n’a pu m’en donner l’impression dans la suite, parce que j’avais de leur pouvoir une notion moins vague et plus expérimentale – emportée par le vol de deux chevaux ardents, minces et contournés comme on en voit dans les dessins de Constantin Guys, portant établi sur son siège un énorme cocher fourré comme un cosaque, à côté d’un petit groom rappelant le « tigre » de « feu Baudenord », je voyais – ou plutôt je sentais imprimer sa forme dans mon coeur par une nette et épuisante blessure – une incomparable victoria, à dessein un peu haute et laissant passer à travers son luxe « dernier cri » des allusions aux formes anciennes, au fond de laquelle reposait avec abandon Mme Swann, ses cheveux maintenant blonds avec une seule mèche grise ceints d’un mince bandeau de fleurs, le plus souvent des violettes, d’où descendaient de longs voiles, à la main une ombrelle mauve, aux lèvres un sourire ambigu où je ne voyais que la bienveillance d’une Majesté et où il y avait surtout la provocation de la cocotte, et qu’elle inclinait avec douceur sur les personnes qui la saluaient.", 50)