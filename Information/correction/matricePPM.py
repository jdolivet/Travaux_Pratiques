# Fonction permettant de transformer une image au format ppm en matrice

def ppm_vers_matrice(fichier_texte):
    # On récupère le fichier
    source = open(fichier_texte,"r")
    fichier = source.readlines()
    source.close()
    
    # On prélève les informations nécessaires
    dimensions = fichier[2].split()
    largeur = int(dimensions[0])
    print("Largeur de l'image :", largeur)
    hauteur = int(dimensions[1])
    print("Hauteur de l'image :", hauteur)
    nuances = int(fichier[3])
    print("Nuances de couleurs :", nuances)

    # On construit la matrice
    ligne = 4
    matrice = [[0 for j in range(largeur)] for i in range(hauteur)]
    for j in range(hauteur):
        for i in range(largeur):
            pixel = [0,0,0]
            for k in range(3):
                pixel[k] = int(fichier[ligne])
                ligne += 1
            matrice[j][i] = pixel
    return matrice
