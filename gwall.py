#!/usr/bin/python
import json, os, requests, urllib, sys, time, codecs , datetime, random ,subprocess
import imageGwall
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

###################===TO DO===#######################
#fait           Raw input nombre d'image
#fait           if input nbr image >= 10 
#fait           Do a barrel roll
#fait           page + 10
#fait           request to json utf8
#fait~          Image io error
#fait           parse fichier contenant 660x666
#fait           fonction pour limiter les requetes
#fait           Raw input nbr d'images par page
#fait           Prise en charge des images sans extensions
#fait~          Recherche image en HD 
#fait		Changer le noms si identique
#fait		Changer les noms si recurrant
#fait           fichier contenant 0x non accessible
#fait           Nbr de fichier par page ne mache pas
#fait		Log print to file
#fait		afficher limage dans la console
#fait		Habillage
#fait		Variables api et cx
#               Choix Api ou Image.Google.com
#               Integrer Image.Google.com
#               Make this fucking script optimized and readable
##################===/TO DO===#######################

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("../tmp/gwall.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

#Put your Api key and cx value here

Apikey = ""
Cx = ""

##





#title figlet 
from pyfiglet import Figlet

gwall = Figlet(font='univers')
version = Figlet(font='doh')
bye = Figlet(font='doh')

print gwall.renderText('Gwall')
print version.renderText('V2.3')



#==Align center
Taille = int(subprocess.check_output(['stty', 'size']).split()[1])
Mid = Taille
#==
Temps = datetime.datetime.now()
page = 1
counter = 0

if len(sys.argv) > 1:

	searcharg = sys.argv
	searchTerm = " ".join(searcharg).replace('gwall.py','')
	nbr = 10
	pageInput = 10
else:
	searchTerm = raw_input("Images a rechercher : ")
	nbr = raw_input(" Nombre d image par page (10 max) :")

	if not nbr.isdigit():
	        print "Nombre entre 1 et 10 uniquement"
	        print ""
	        print Temps
	        print ""
	        print bye.renderText('Bye!')
	        sys.exit()

	if int(nbr) > 10:
	        nbr = 10
 

	pageInput = raw_input("Nombre totale de pages : ")

	if not pageInput.isdigit():
	        print "Nombre entre 00 et 101 uniquement"
	        print ""
	        print Temps
	        print ""
	        print bye.renderText('Bye!')
	        sys.exit()


query = searchTerm

path = '/home/on4r4p/Images/ImagesFromGwall'


 
BASE_PATH2 = os.path.join(path, query)
BASE_PATH =  BASE_PATH2.replace(' ','-') 
creadossier = "Creation du dossier images : ",BASE_PATH
creadossier = str(creadossier)
print ""
print creadossier
print ""
if not os.path.exists(BASE_PATH):
	os.makedirs(BASE_PATH)


pageInput = int(pageInput)
counter = int(counter)

#Debut boucle nombre pages demandees
while counter <= pageInput:

	BASE_URL = 'https://www.googleapis.com/customsearch/v1?key=' + str(Apikey) + '&cx=' + str(Cx) + '&q=' + query + '&num=' + str(nbr) + '&searchType=image&imgSize=xxlarge&start=' + str(page)
#	print "Gwallpy adresse :"
#	print BASE_URL
	try:
		f = requests.get(BASE_URL)
	except:
		print "Enigmatic Error"
		continue

	if os.path.exists("../tmp/gwall2.json"):
		fichier = open("../tmp/gwall2.json","w")
		fichier.close()
		os.remove("../tmp/gwall2.json")
		if os.path.exists("../tmp/gwall2.json"):
			print "HE s STILL ALIVE !!!"
			print "Erreur le fichier ne veut pas creuver.."
	                print ""
	                print Temps
	                print ""
			print bye.renderText('Bye!')
			sys.exit()


	json_out = codecs.open("../tmp/gwall2.json","w" , "utf-8")
	json_out.write(f.text)
	json_out.close()
	fichier = open("../tmp/gwall2.json")
	r  = json.load(fichier)
	

	total_no_of_images = nbr
	counter_total_img = 0
	counter_total_img = int(counter_total_img)
	total_no_of_images = int(total_no_of_images)




	print ""
	print "Execution en cours...".center(Mid)
	print ""
	
#boucle interne
	while counter_total_img < total_no_of_images:
		try:
			parsurl = r['items'][counter_total_img]['link']
		except KeyError as ki:

			print ""
			print "Fin des resultats"
			print r
			print "Mefaits accomplies."
			print "-Fin du programme-"
	                print ""
			print bye.renderText('Bye!')
	                print str(Temps).center(Mid)
	                print ""
			sys.exit()


		code200 = 0
		codeRedirect = 0
		codeExt = 0
		hex = 0		



		print ""
		print "##############################################################"
		print "Page : ",page
		print "Image numero:",counter_total_img + 1


		titre = r['items'] [counter_total_img] ['snippet']

                furl = parsurl

		try:
			print  "Titre :",titre
		except UnicodeEncodeError as fuck:
			print "!!!!!!!!!!!!!!!!!!!!Unicode!!!!!!!!!!!!!!!!!!!!".center(Mid) 
		print "Lien : ",furl
		print "##############################################################"
		print ""

		print "Le fichier sera enregistre sous ce nom:".center(Mid)
	
		furlext = parsurl
		furlext = furlext.split('/')[-1].replace('/', '').replace('\\', '').split('.')
	        filename, ext = furlext[0], str(furlext[-1])
	        ext = ext.split('?', 1)[0].lower()



		listExt = ['jpg', 'jpeg','png','gif', 'bmp','tiff',]
		if "0x" in filename:
			print "Filtrage de 000x000".center(Mid)
			hex = 1
                if "1x" in filename:
                        print "Filtrage de 001x000".center(Mid)
                        hex = 1
                if "2x" in filename:
                        print "Filtrage de 002x000".center(Mid)
                        hex = 1
                if "3x" in filename:
                        print "Filtrage de 003x000".center(Mid)
                        hex = 1
                if "4x" in filename:
                        print "Filtrage de 004x000".center(Mid)
                        hex = 1
                if "5x" in filename:
                        print "Filtrage de 005x000".center(Mid)
                        hex = 1
                if "6x" in filename:
                        print "Filtrage de 006x000".center(Mid)
                        hex = 1
                if "7x" in filename:
                        print "Filtrage de 007x000".center(Mid)
                        hex = 1
                if "8x" in filename:
                        print "Filtrage de 008x000".center(Mid)
                        hex = 1
                if "9x" in filename:
                        print "Filtrage de 009x000".center(Mid)
                        hex = 1

		
		if not ext in listExt:
			print "Impossible de trouver une extension.".center(Mid)
			codeExt = 1





		if codeExt == 0:
			try:
				if hex == 1:
					nomfichier = filename.replace('x','').replace('/','').replace(':','').replace('?','').replace('-','').replace('_','').replace('=','') 
				if hex == 0:
					nomfichier = filename.replace('/','').replace(':','').replace('?','').replace('-','').replace('_','').replace('=','') 
					
				file = nomfichier + "." + ext
				fileprint = str(file)
				print fileprint.center(Mid)
				try:
					image_get = requests.get(parsurl, allow_redirects=False,timeout=1.0)
				except:
					print "Mysterious Error"
					
			
				if image_get.status_code == 200:
					print "Element accessible: Oui".center(Mid)
				else:
					print "Element accessible: Non".center(Mid)
					code200 = 1
				
			
				if code200 == 0:
					try:
						image_get = requests.get(parsurl, allow_redirects=False,timeout=1.0)
						image_r = image_get
						print "Ecriture du fichier".center(Mid)

					except requests.exceptions.TooManyRedirects, tmrdirect:
						print "Too many redirects".center(Mid)
						codeRedirect = 1

					if codeRedirect == 0:

						try:
							doublons = ['maxresdefault.jpg', 'original.jpg']

							if file in doublons:
								print ""
                                                                print "Nom de fichier generique".center(Mid)
                                                                print "Changement de nom".center(Mid)
								print ""
								time.sleep(1)
								nbralea = random.randint(23,99999)
                                                                nomfichier = nomfichier + "double" + str(nbralea)
                                                                file = nomfichier + "." + ext




							testidentique = os.path.join(BASE_PATH, '%s') % (file)

							if os.path.exists(testidentique):

								print ""
								print "!!!!!!!!!!!!!!!!!!!!!!!!!".center(Mid)
								print "!!!!!Fichier Identique!!!".center(Mid)
                                                                print "!!!!!!!!!!!!!!!!!!!!!!!!!".center(Mid)
                                                                print ""
								
								nbralea = random.randint(23,99999)
								nomfichier = nomfichier + "copie" + str(nbralea)
								file = nomfichier + "." + ext

							if not os.path.exists(testidentique):
								print "Aucun fichier du meme nom deja present.".center(Mid)
								print ""

							ecriture = open(os.path.join(BASE_PATH, '%s') % (file), 'wb')
							Image.open(StringIO(image_r.content)).save(ecriture)
							loadimage = BASE_PATH + "/" + file

#img2term
							from fabulous import utils
							print imageGwall.Image(loadimage)
							time.sleep(0.5)
##
							print "Emplacement du fichier :".center(Mid)
							basefile = BASE_PATH + "/" + file
							basefile = str(basefile)
							print basefile.center(Mid)
							print "Fichier suivant...".center(Mid)

 						except IOError, ioe:
							print "Impossible de sauvegarder le fichier".center(Mid)
							print "tant pis".center(Mid)
			
			except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError) as tup:
                                	print tup

		counter_total_img += 1

		print "==============================================================".center(Mid)
		print ""
		print ""

#Fin boucle interne

	print "Page numero : ",counter
	counter +=1
	page +=10

	if page >=101:

		print "Limites Api atteintes . (101 pages max)"
		print "Sortie du programme "
		print "Mefaits accomplies."
		print "-Fin du programme-"
		print ""
		print bye.renderText('Bye!')
		print str(Temps).center(Mid)
		print ""
		sys.exit()
#fin:		
print "Mefaits accomplies."
print "-Fin du programme-"
print ""
print bye.renderText('Bye!').center(Mid)
print str(Temps).center(Mid)
print ""
#Fin boucle nombre d'images demandees
sys.exit()









