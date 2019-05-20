def labyrinthe_charger_depuis_fichier(nom_fichier):


    return {
        "chemins": valeur, 
        "murs": valeur, 
        "hauteur": valeur, 
        "largeur": valeur, 
        "depart": valeur, 
        "arrivee": valeur
    }


def main():
    chemins = []
    murs = []
    largeur = None
    hauteur = None

    with open("labyrinthe.txt", "r") as mon_fichier:
        mon_labyrinthe = mon_fichier.readlines()
        hauteur = len(mon_labyrinthe)
        largeur = len(mon_labyrinthe[0].strip())

        print("Lecture du fichier labyrinthe.txt ligne par ligne:\n")
        print(mon_labyrinthe)

        print("Determination de la position des chemins et murs: ")
        for i, ligne in enumerate(mon_labyrinthe):
            for j, caractere in enumerate(ligne.strip()):
                if caractere == '.':
                    chemins.append((i, j))
                    
                elif caractere == '#':
                    murs.append((i, j))
                   

            print("Les chemins ", chemins,)
            print("Les murs", murs)


        
main()