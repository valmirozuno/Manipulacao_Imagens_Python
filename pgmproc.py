#Definition des classes :

class FileCorruptError(Exception) :	
	def __init__(self,message) :
		self.messageError = message
	def printError(self) :
		print self.messageError

class Dimension:
	#Une dimension, c'est une hauteur et une largeur
	def __init__(self, htr, lgr):
		self.hauteur = htr
		self.largeur = lgr

class Image :
	#Une image est composee :
	# - d'un tableau a deux dimensions d'entiers correspondants au niveau de gris d'un pixel
	# - d'une dimension, c'est a dire d'une hauteur et largeur
	def __init__ (self,img,dim) :
		self.img = img
		self.dim = dim


#Partie consacree au traitement de l'image

def negatifPGMraw(image) :
	#Donnée : image, l’image originale
	#Résultat : une copie de l’image en négatif
	#Complexité : O(n*n), plus précisement largeur*hauteur
	#Recopie de l'image actuelle
	tab = [[0 for x in range (image.dim.largeur)] for x in range (image.dim.hauteur)]
	image2 = Image(tab,Dimension(image.dim.hauteur,image.dim.largeur))
	#Inversion des couleurs de l'image
	#Invariant : image2.img[0..i][0..j] est inversé
	for i in range(0,image.dim.hauteur) :
		for j in range(0,image.dim.largeur) :
			image2.img[i][j] = 255 - image.img[i][j]
	#Renvoi de l'image
	return image2

def pivot90PGMraw(image):
	#Donnée : image, l’image originale
	#Résultat : une copie de l’image pivoté de 90 degrés dans le sens des aiguilles d’une montre

	#Complexité : O(n*n), plus précisement largeur*hauteur
	#Recopie de l'image actuelle. La largeur correspond desormais a la hauteur et vice versa
	tab = [[0 for x in range (image.dim.hauteur)] for x in range (image.dim.largeur)]
	image2 = Image(tab,Dimension(image.dim.largeur,image.dim.hauteur))
	#Rotation de 90 degre dans le sens des aiguilles d'une montre de chaque pixel

	#Invariant : image2.img[0..i][0..j] est tourne de 90 degre dans le sens des aiguilles d'une montre
	for i in range (image2.dim.hauteur) :
		for j in range (image2.dim.largeur) :
			image2.img[i][j] = image.img[image.dim.hauteur-j-1][i]
	#Renvoi de l'image
	return image2

def pivotMoins90PGMraw(image):
	#Donnée : image, l’image originale
	#Résultat : une copie de l’image pivotée de 90 degrés dans le sens inverse des aiguilles d’une montre
	#Complexité : O(n*n), plus précisement largeur*hauteur
	#Recopie de l'image actuelle. La largeur correspond desormais a la hauteur et vice versa
	tab = [[0 for x in range (image.dim.hauteur)] for x in range (image.dim.largeur)]
	image2 = Image(tab,Dimension(image.dim.largeur,image.dim.hauteur))
	#Rotation de 90 degre dans le sens inverse des aiguilles d'une montre de chaque pixel

	#Invariant : image2.img[0..i][0..j] est tourne de 90 degre dans le sens inverse des aiguilles d'une montre
	for i in range (image2.dim.hauteur) :
		for j in range (image2.dim.largeur) :
			image2.img[i][j] = image.img[j][image.dim.largeur-i-1]
	#Renvoi de l'image
	return image2

def miroirHorizontalPGMraw(image):
	#Donnée : image, l’image originale
	#Résultat : une copie de l’image retournée horizontalement
	#Complexité : O(n*n), plus précisement largeur*hauteur
	#Recopie de l'image actuelle
	tab = [[0 for x in range (image.dim.largeur)] for x in range (image.dim.hauteur)]
	image2 = Image(tab,Dimension(image.dim.hauteur,image.dim.largeur))
	#Inversion horizontale de chaque pixel
	#Invariant : image2.img[0..i][0..j] est inversé horizontalement
	for i in range (image.dim.hauteur):
		for j in range (image.dim.largeur):
			image2.img[i][j] = image.img[i][image.dim.largeur-j-1]
	#Renvoi de l'image
	return image2

def miroirVerticalPGMraw(image):
	#Donnée : image, l’image originale
	#Résultat : une copie de l’image retournée verticalement
	#L'option d'utiliser deux fois pivot90PGMraw est possible, mais aurait un temps d'execution deux fois plus long. Ici, on est simplement en complexite n^2
	#Recopie de l'image actuelle
	tab = [[0 for x in range (image.dim.largeur)] for x in range (image.dim.hauteur)]
	image2 = Image(tab,Dimension(image.dim.hauteur,image.dim.largeur))
	#Inversion Verticale de chaque pixel
	#Invariant : image2.img[0..i][0..j] est inversé verticalement
	for i in range (image.dim.hauteur):
		for j in range (image.dim.largeur):
			image2.img[i][j] = image.img[image.dim.hauteur-i-1][j]
	#Renvoi de l'image
	return image2

def niveauDeGrisPGMraw(image, grisMin, grisMax):
	#Données : image, l’image originale, grisMin : le niveau de gris minimal de l’image à remettre à zéro, grisMax : le niveau de gris maximal à remettre à 255
	#Résultat : une copie de l’image avec le nouveau niveau de gris spécifié
	#Complexite d'ordre n^2
	#On recopie la matrice sans les valeurs
	tab = [[0 for x in range (image.dim.largeur)] for x in range (image.dim.hauteur)]
	image2 = Image(tab,Dimension(image.dim.hauteur,image.dim.largeur))

	if(grisMin>grisMax):
		#Si erreur, on renvoie une copie de l'image actuelle
		print "La valeur minimale du niveau de gris doit etre inferieure a la valeure maximale. L'image ne sera pas modifiee" #Remplacer par une erreur
		#Invariant : image2.img[0..i][0..j] contient les memes valeurs que image.img[0..i][0..j]
		for i in range (image.dim.hauteur) :
			for j in range (image.dim.largeur) :
				image2.img[i][j] = image.img[i][j]
		return image2
	
	moy = (grisMin+grisMax)/2
	#Partie traitement de l'image
	#Distance entre le blanc et le nouveau gris max
	distMax = (float)(255-grisMax)
	#Distance entre le noir et le nouveau gris min
	distMin = (float)(0+grisMin)
	#Invariant : image2.img[0..i][0..j] est contraste
	for i in range (image.dim.hauteur) :
		for j in range (image.dim.largeur) :
			#Si la valeur est superieure a la moyenne alors :
			#On calcule un coefficient compris entre 0 et 1, en fonction de la distance de la valeur actuelle, entre la valeur moyenne et le gris maximum. Si valeur=moyenne -> coef=0. Si valeur=grismax -> coef=1
			#On multiplie ce coefficient avec la distance max impose par l'utilisateur, qui donne la difference a rajouter a la valeur actuelle du pixel
			if image.img[i][j]>=moy :
				coefficient = ( (float)(image.img[i][j] - moy) / (float)(grisMax - moy) )
				difference =  (int)(coefficient * distMax)
			#Sinon :
			#On calcule un coefficient compris entre 0 et 1, en fonction de la distance de la valeur actuelle, entre la valeur moyenne et le gris minimum. Si valeur=moyenne -> coef=0. Si valeur=grismin -> coef=1
			#On multiplie ce coefficient avec la distance min impose par l'utilisateur, qui donne la difference a rajouter a la valeur actuelle du pixel
			else :
				coefficient = ( (float)(moy-image.img[i][j]) / (float)(moy-grisMin) )
				difference = (int)(-coefficient * distMin)
			#On ajoute la difference
			image2.img[i][j] = image.img[i][j] + difference
			#On termine par verifier si la valeur depasse des bornes, si oui : on le corrige
			if(image2.img[i][j] < 0):
				image2.img[i][j] = 0
			if(image2.img[i][j] > 255):
				image2.img[i][j] = 255
	return image2
 
def contrasteAutoPGMraw(image):
	#Donnée : image, l’image originale
	#Résultat : une copie de l’image avec un niveau de gris optimisé
	#Complexité : O(n*n), plus précisement largeur*hauteur
	maxi = 0
	mini = 255
	for i in range (image.dim.hauteur) :
		for j in range (image.dim.largeur) :
			if(image.img[i][j]>maxi):
				maxi = image.img[i][j]
			if(image.img[i][j]<mini):
				mini = image.img[i][j]
	return niveauDeGrisPGMraw(image,mini,maxi)

#Fonction pour connaitre qui pixel d'une image donnee  aura une correspondance avec une pixel d'une autre image avec une taille different
#Complexite O(1)
#w1 est l'hauteur ou la largeur de l'image original, w2 est l'hauteur ou la largeur de la nouvelle image et aux une position pour choisir le pixel correct
def map(aux, w1, w2):
	#Données : aux : la position (x ou y) de base d’un pixel, w1 : une longueur (largeur ou hauteur) originale, w2 : une longeur (largeur ou hauteur) de destination
	#Résultat : res de type float, la position (x ou y) finale d’un pixel

	res = float((aux * w1)/ float(w2))
	return res

#Fonction pour prendre un pixel, avec quelques optimizations pour travailler avec la fonction d'echelle
#Complexite O(1)
#i est ligne et j la colonne
def get_pixel(image, i, j):
	#Donnée : image, l’image, i : la position x du pixel, j : la position y du pixel
	#Résultat : le pixel correspondant au (x,y) spécifié
	if (i < 0):
		i = int(0)
	if (i >= image.dim.hauteur):
		i = int(image.dim.hauteur - 1)
	if (j < 0):
		j = int(0)
	if (j >= image.dim.largeur):
		j = int(image.dim.largeur - 1)

	return int(image.img[i][j])


#Fonction pour changer l'echelle d'une image donnee, en utilisant l'algorithme d'interpolation bilineaire
#Complexite O(p), ou p est egal au nombre total de pixels de l'image donnee
#percentage est un float
#Exemple d'appel : scalePGMraw(image, 1.7) -> Cet appel cre une nouvelle image avec 170% de la taille de l'image original
def scalePGMraw(image, percentage):
	#Donnée : image, l’image originale, percentage : le pourcentage de redimensionnement
	#Résultat : une copie de l’image redimensionnée
	# cree une nouvelle matrice et une nouvelle dimension pour la nouvelle image
	tab = [[0 for x in range((int(image.dim.largeur*percentage)))] for x in range((int(image.dim.hauteur*percentage)))]
	dim = Dimension((int(image.dim.hauteur*percentage)), (int(image.dim.largeur*percentage)))
	# cree la nouvelle image
	image2 = Image(tab,dim)
	# [p1,...,p4] sont les pixels que on regarde pour creer le nouveau pixel, p5, pour la nouvelle image
	p1 = 0; p2 = 0; p3 = 0; p4 = 0; p5 = 0;
	# ii et jj sont variables pour prendre des pixels de la image donnee et les mettre sur la nouvelle image
	ii = 0; jj = 0

	# Invariant: a la n-eme iteration, toutes les lignes < i de l'image2  auront les nouveux pixels
	for i in range(0, image2.dim.hauteur):
		# Invariant: a la n-eme iteration dans la ligne courent, toutes les positions < j de l'image2  auront les nouveux pixels
		for j in range(0, image2.dim.largeur):
			#prendre des pixels des lignes et des colonnes pour cree la nouvelle image
			ii = int(map(i, image.dim.hauteur, image2.dim.hauteur))
			jj = int(map(j, image.dim.largeur, image2.dim.largeur))

			#prendre 4 pixels de la image donnee pour faire l'interpolation
			p1 = get_pixel(image, ii, jj)
			p2 = get_pixel(image, ii + 1, jj)
			p3 = get_pixel(image, ii, jj + 1)
			p4 = get_pixel(image, ii + 1, jj + 1)

			#l'interpolation. le nouveau pixel aura la moyenne des autres pixels
			p5 = (p1 + p2 + p3 + p4) / 4
			#ajouter le nouveau pixel a la nouvelle image
			image2.img[i][j] = p5


	return image2
	
	#Fonctions de traitement des fichiers

def estPGMrawValide(path):
	#Donnée : path, le chemin d’accès vers le fichier
	#Résultat : estValide, un booléen qui indique si le fichier est au format PGM
	#Complexité : constante
	"""Teste si le fichier est valide - lève l'exception IOerror si problème de lecture du fichier"""
	fichier = open(path, "r")

	#on recupere la premier ligne du fichier
	ligneSuivante = recupererLigne(fichier, 1, True)
	if ligneSuivante != "P5\n":
		fichier.close()
		return False
	#on recupere la deuxieme ligne du fichier. Les lignes precedentes sont valides
	ligneSuivante = recupererLigne(fichier, 1, True)
	aux = recupererDimension(ligneSuivante)
	#Non valide si la dimension recuperee vaut [-1,-1]
	if (aux.largeur == -1):
		fichier.close()

		return False
	#on recupere la troisieme ligne du fichier. Les lignes precedentes sont valides
	ligneSuivante = recupererLigne(fichier, 1, True)
	if (ligneSuivante != "255\n"):
		fichier.close()
		return False
	#A ce stade, le fichier correspond bien a un fichier PGMraw
	#on compte le nombre de caracteres
	cpt = 0

	ligneCouleurs = fichier.read()
	if (len(ligneCouleurs) != (aux.hauteur * aux.largeur)):
		fichier.close()
		return False
	fichier.close()
	return True

def lirePGMraw (chemin) :
	#Donnée : chemin, le chemin d’accès au fichier
	#Résultat : image, le type abstrait contenant les données du fichier PGM
	#Complexité : O(nbp) avec nbp le nombre de pixels de l'image. nbp pour la fonction estPGMrawValide, nbp pour le reste de la fonction
	"""Essaye de lire un fichier PGM - lève l'exception IOerror si problème de lecture du fichier, lève FormatPGMError si le fichier n'est pas au format PGM"""
	if(not estPGMrawValide(chemin)):
		raise FileCorruptError("Le fichier existe mais est corrompu (Raison : fichier non valide)")

	fichier = open(chemin,"r")

	ligne = 0
	#On recupere les dimensions de l'image et on cree la matrice
	ligneSuivante = recupererLigne(fichier,2,True)
	dimension = recupererDimension(ligneSuivante)
	img = [[0 for x in range(dimension.largeur)] for x in range(dimension.hauteur)]
	ligneSuivante = recupererLigne(fichier,1,False)
	#On insere chaque couleur dans la matrice
	for i in range (0,dimension.largeur*dimension.hauteur):
		img[i / dimension.largeur][i % dimension.largeur] = recupererCouleur(fichier.read(1))
	fichier.close()
	#On retourne l'image
	return Image(img,dimension)

def ecrirePGMraw(image,chemin) :
	#Données : image : l’image à ecrire, chemin : le chemin pour écrire l’image
	#Résultat : Vide
	#Complexité : O(n*n), plus précisement largeur*hauteur
	#On ecrit les proprietes d'un fichier PGMraw
	fichier = open(chemin,"w")
	fichier.write("P5\n")
	fichier.write(str(image.dim.largeur)+" "+str(image.dim.hauteur) + "\n")
	fichier.write("255\n")
	#On ecrit chaque couleur dans le fichier
	#Invariant : fichier content toutes les couleurs de image.img[0..i][0..j]
	for i in range (0,image.dim.hauteur) :
		for j in range (0,image.dim.largeur) :
			ecrireCouleur(fichier,image.img[i][j])
	fichier.close()

def recupererDimension (ligne):
	#Donnée : ligne, la ligne des dimensions de l’image
	#Résultat : dimension, les dimensions de l’image
	compteurCaractere = 0
	#Complexité : O(n) avec n le nombre de caractere de la ligne
	#ligne s'ecrit de la forme [largeur]{espace}[hauteur]
	while((compteurCaractere < len(ligne)) and ligne[compteurCaractere] != ' '):
		compteurCaractere += 1
	if (compteurCaractere == len(ligne)):
		raise FileCorruptError("Le fichier existe mais est corrompu (Raison : dimensions inexistantes)")
	largeur = (int)(ligne[0 : compteurCaractere])
	hauteur = (int)(ligne[compteurCaractere : len(ligne)])
	if(largeur <= 0 or hauteur <= 0) :
		raise FileCorruptError("Le fichier existe mais est corrompu (Raison : dimensions incorrectes)")
	return Dimension(hauteur, largeur)

def estCommentaire(ligne):
	#Donnée : ligne, la ligne à vérifier
	#Résultat : un booléen qui vaut vrai si la ligne est un commentaire, faux sinon
	return ligne[0] == '#'

def recupererLigne(fichier, nblignes, sauterCommentaires) :
	#Données : fichier, le fichier sur lequel on doit récupérer la ligne, nblignes : le nombre de ligne (moins 1) à passer pour récupérer la bonne ligne, sauterCommentaires : s’il vaut vrai, on ne comptera pas la ligne des commentaires comme une vraie ligne.
	#Résultat : la ligne à récupérer depuis le fichier
	#Complexité : O(n)
	ligne = 0
	finFichier = False
	ligneSuivante = ""
	while (not(finFichier) and ligne<nblignes) :
		ligneSuivante = fichier.readline()
		if(len(ligneSuivante) == 0) :
			finFichier = True
		#not (sauter commentraire et estCommentaire)
 		elif (not((sauterCommentaires) and estCommentaire(ligneSuivante))) :
			ligne = ligne + 1
	return ligneSuivante

def recupererCouleur(couleurFichier) :
	#Donnée : couleursFichier, une couleur codée en ASCII
	#Résultat : la couleur convertie en valeur entière
	return ord(couleurFichier)

def ecrireCouleur(fichier,couleur) :
	#Donnée : fichier, le fichier dans lequel il faut écrire la couleur, couleur : la valeure entière de la couleur
	#Résultat : Vide, mais la couleur est convertie en code ASCII et écrite dans le fichier
	if(couleur<0 or couleur>255) :
		fichier.write(chr(0))
	else :
		fichier.write(chr(couleur))
import sys

entete = "\n"+ sys.argv[0] +" propose des fonctionnalités permettant le traitement d'images au format PGM.\nLes fonctionnalités disponibles et leur manière d'utilisation sont résumées ci-dessous:\n"
utilisation = "utilisation : python "+ sys.argv[0] +" [Option 1] [Argument(s) 1] [Option 2] ... [Chemin source] [Chemin destination]\nExemple : python python.py -ndg 20 200 -mh canada.pgm canadaModifie.pgm"
description="-h, -help : Affiche l'aide\n-n : Inverse les couleurs de l'image\n-p : Effectue une rotation de 90 degrés dans le sens des aiguilles d'une montre\n-pi : Effectue une rotation de 90 degrés dans le sens inverse des aiguilles d'une montre\n-sc [Pourcentage] : La taille de l'image est modifiée en fonction du pourcentage spécifié\n-autoc : Applique un contraste automatique sur l'image\n-ndg [Gris minimum] [Gris maximum] : modifie les niveaux de gris de l'image en fonction des gris min/max spécifiés\n-mv : L'image est retournée verticalement\n-mh : L'image est retournée horizontalement\n\nChemin source et chemin destination : correspond au chemin relatif à partir duquel vous voulez que l'image soit chargée puis sauvegardée (Indiquez uniquement le nom de l'image si celle ci se trouve dans le meme répertoire que le script)\nDe plus, le chemin de destination est optionnel : vous pouvez indiquer uniquement l'image source si vous voulez qu'elle soit modifiée directement"

def afficherAide() :
	print entete
	print utilisation
	print description
if(len(sys.argv)==1):
	afficherAide()
elif(sys.argv[1] == "-help" or sys.argv[1] == "-h"):
	afficherAide()
else :
	i = 1
	argmax = len(sys.argv) - 1
	imageSource = sys.argv[argmax - 1]
	imageDest = sys.argv[argmax]

	#On va regarder si l'utilisateur a rentré : - un fichier source et destination, - uniquement un fichier source (dans ce cas là, la destination sera la source), - aucun fichier
	try :
		if(not estPGMrawValide(imageSource)) :
			if(estPGMrawValide(imageDest)) :
				imageSource = imageDest				
	except (IOError) :
		if(imageSource[-4:]==".pgm"):
			print"Le fichier " + imageSource + " n'existe pas"
			sys.exit(1)
		try :
			estPGMrawValide(imageDest)
			imageSource = imageDest
			argmax = len(sys.argv)
		except (IOError) :
			print"Le fichier " + imageDest + " n'existe pas"
			sys.exit(1)
	except (FileCorruptError) as e :
		e.printError()
		sys.exit(1)
	except (ValueError) :
		print "Erreur de conversion des dimensions de l'image"
		sys.exit(1)
	#A ce stade, on a l'image source et le chemin de destination
	print "L'image \""+imageSource+"\" va etre chargée. Sa copie modiée sera enregistrée au nom de \""+imageDest+"\""
	print "Verification du fichier " + imageSource + "..."
	try :
		image1 = lirePGMraw(imageSource)
	except (FileCorruptError) as e :
		e.printError()
		sys.exit(1)
	print "Lecture du fichier " + imageSource + " reussie"
	while i < argmax - 1 : 
		if(sys.argv[i] == "-n"):
			print "Les couleurs de l'image vont être inversée"
			image1 = negatifPGMraw(image1)
		elif(sys.argv[i] == "-p"):
			print "L'image va pivoter de 90 degrés dans le sens des aiguilles d'une montre"
			image1 = pivot90PGMraw(image1)
		elif(sys.argv[i] == "-pi"):
			print "L'image va pivoter de 90 degrés dans le sens inverse des aiguilles d'une montre"
			image1 = pivotMoins90PGMraw(image1)
		elif(sys.argv[i] == "-sc"):
			print "La taille de l'image va être modifiée"
			try :
				pourcentage = (float)(sys.argv[i+1])
				if(pourcentage <= 0):
					print "Le pourcentage doit etre positif"
					sys.exit(1)
				print "Pourcentage : "+ str(pourcentage)
				i = i + 1
			except (ValueError) :
				print "Les valeurs entrées sont incorrectes. Syntaxe de la fonction : -sc [pourcentage] ..."
				sys.exit(1)
			image1 = scalePGMraw(image1,(pourcentage/100.0))
		elif(sys.argv[i] == "-autoc"):
			print "Activation des contrastes automatiques"
			image1 = contrasteAutoPGMraw(image1)
		elif(sys.argv[i] == "-ndg"):
			print "Le niveau de gris sera changé avec les paramètres suivants : "
			try :
				grisMin = (int)(sys.argv[i+1])
				i = i + 1
				grisMax = (int)(sys.argv[i+1])
				i = i + 1
			except (ValueError) :
				print "Les valeurs entrées sont incorrectes. Syntaxe de la fonction : -ndg [min] [max] ..."
				sys.exit(1)
			print "Gris minimal : "+str(grisMin)+", gris maximal : "+ str(grisMax)
			image1 = niveauDeGrisPGMraw(image1,grisMin,grisMax)
		elif(sys.argv[i] == "-mv"):
			print "Miroir vertical de l'image"
			image1 = miroirVerticalPGMraw(image1)
		elif(sys.argv[i] == "-mh"):
			print "Miroir horizontal de l'image"
			image1 = miroirHorizontalPGMraw(image1)
		else :
			print "L'argument \"" + sys.argv[i] + "\" est invalide. Tapez \"python python.py -h\" pour plus de détail"
		i = i + 1
	ecrirePGMraw(image1,imageDest)
	print "Le fichier " + imageDest + " a ete enregistre"