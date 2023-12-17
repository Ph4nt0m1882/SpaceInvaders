#Space invaders


#Import des modules nécessaire: tkinter pour l'interface graphique
#                               random pour la gestion des tir ennemi et pour la gestion de l'ennemi bonus
from tkinter import *
from random import *

class POINT:
    def __init__(self,abscisse,ordonnee):
        self.x=abscisse
        self.y=ordonnee


def texte(canv,P,abc,font,coul,coul2):
    canv.create_text(P.x,P.y,text=abc,font=font,fill=coul,activefill=coul2)

def image(canv,P,chemin):
    canv.create_image(P.x,P.y,image=chemin)

def pixel(canv,P,e,coul):
    canv.create_rectangle(P.x,P.y,P.x+e,P.y+e,outline=coul,fill=coul)

def c_Px(canv,P,coul):
    pixel(canv=canv,P=P,e=4,coul=coul)
#Dans space invaders, les lignes ennemi sont composé de 11 mob, le plus grand fait 12 pixel, ils ont un écart de 3 pixel,
#   la résolution de l'ecran fait 210 pixel je choisi donc une résolution de 4 x 4 pixel





## ## ## ##
## Sprit ##
## ## ## ##

#Cette fonction permet de dessiner le vaisseau à sa position initiale, de définire la position de son canon et de sa zone de collision

def dessine_vaisseau():
    global vaisseau,pos_vaisseau,pos_canon1,pos_canon2,col_vaisseau1,col_vaisseau2
    vaisseau=[]
    pos_vaisseau=POINT(25,750)
    vaisseau.append(game.create_rectangle(pos_vaisseau.x-22,pos_vaisseau.y+6,pos_vaisseau.x+22,pos_vaisseau.y+14,fill='green',outline="green"))
    vaisseau.append(game.create_rectangle(pos_vaisseau.x-18,pos_vaisseau.y+2,pos_vaisseau.x+18,pos_vaisseau.y+6,fill='green',outline="green"))
    vaisseau.append(game.create_rectangle(pos_vaisseau.x-6,pos_vaisseau.y-6,pos_vaisseau.x+6,pos_vaisseau.y+2,fill='green',outline="green"))
    vaisseau.append(game.create_rectangle(pos_vaisseau.x-2,pos_vaisseau.y-10,pos_vaisseau.x+2,pos_vaisseau.y-6,fill='green',outline="green"))
    pos_canon1=POINT(pos_vaisseau.x-2,pos_vaisseau.y-10)
    pos_canon2=POINT(pos_vaisseau.x+2,pos_vaisseau.y-6)
    col_vaisseau1=POINT(pos_vaisseau.x-22,pos_vaisseau.y-10)
    col_vaisseau2=POINT(pos_vaisseau.x+22,pos_vaisseau.y+14)

#Mob
#Il y a 4 mob dans space invaders, la différence est que chacun d'entre eux vaut 10, 20, 30 ou une valeur aléatoir de point les 3 premiers
#   sont disposer sur les 5 lignes, le dernier apparait de manières aléatoires en haut de l'écran, je définit chaque ligne du front ennemis

def dessine_mob_10():       # première ligne face au joueur
    global liste_ennemis,liste_coordennemis,xe,ye,nb_ennemis
    liste_coordennemis[0].append([xe,ye])
    Ennemis=[]
    Ennemis.append(game.create_rectangle(xe+16,ye,xe+32,ye+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+4,ye+8,xe+44,ye+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe,ye+12,xe+48,ye+8,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe,ye+12,xe+12,ye+16,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+20,ye+12,xe+28,ye+16,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+36,ye+12,xe+48,ye+16,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe,ye+16,xe+48,ye+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+8,ye+20,xe+20,ye+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+28,ye+20,xe+40,ye+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+4,ye+24,xe+12,ye+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+20,ye+24,xe+28,ye+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+36,ye+24,xe+44,ye+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+8,ye+28,xe+16,ye+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe+32,ye+28,xe+40,ye+32,fill="gray",outline="gray",width=0))
    liste_ennemis[0].append(Ennemis)
    xe=xe+60

def dessine_mob_10_2():     # seconde ligne face au joueur
    global liste_ennemis,liste_coordennemis,xe2,ye2,nb_ennemis
    liste_coordennemis[1].append([xe2,ye2])
    Ennemis=[]
    Ennemis.append(game.create_rectangle(xe2+16,ye2,xe2+32,ye2+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+4,ye2+8,xe2+44,ye2+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2,ye2+12,xe2+48,ye2+8,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2,ye2+12,xe2+12,ye2+16,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+20,ye2+12,xe2+28,ye2+16,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+36,ye2+12,xe2+48,ye2+16,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2,ye2+16,xe2+48,ye2+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+8,ye2+20,xe2+20,ye2+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+28,ye2+20,xe2+40,ye2+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+4,ye2+24,xe2+12,ye2+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+20,ye2+24,xe2+28,ye2+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+36,ye2+24,xe2+44,ye2+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+8,ye2+28,xe2+16,ye2+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe2+32,ye2+28,xe2+40,ye2+32,fill="gray",outline="gray",width=0))
    liste_ennemis[1].append(Ennemis)
    xe2=xe2+60

def dessine_mob_20_1():     # troisième ligne face au joueur
    global liste_ennemis,liste_coordennemis,xe3,ye3,nb_ennemis
    liste_coordennemis[2].append([xe3,ye3])
    Ennemis=[]
    Ennemis.append(game.create_rectangle(xe3+36,ye3,xe3+40,ye3+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+12,ye3,xe3+16,ye3+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+36,ye3+8,xe3+32,ye3+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+16,ye3+8,xe3+20,ye3+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+12,ye3+8,xe3+40,ye3+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+8,ye3+16,xe3+16,ye3+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+32,ye3+16,xe3+20,ye3+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+36,ye3+16,xe3+44,ye3+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+8,ye3+16,xe3+48,ye3+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+8,ye3+16,xe3+48,ye3+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+8,ye3+16,xe3+4,ye3+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+44,ye3+16,xe3+48,ye3+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+12,ye3+20,xe3+40,ye3+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+16,ye3+28,xe3+12,ye3+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+36,ye3+28,xe3+40,ye3+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+24,ye3+28,xe3+16,ye3+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe3+36,ye3+28,xe3+28,ye3+32,fill="gray",outline="gray",width=0))
    liste_ennemis[2].append(Ennemis)
    xe3=xe3+60

def dessine_mob_20_2():     # quatrième ligne face au joueur
    global liste_ennemis,liste_coordennemis,xe4,ye4,nb_ennemis
    liste_coordennemis[3].append([xe4,ye4])
    Ennemis=[]
    Ennemis.append(game.create_rectangle(xe4+36,ye4,xe4+40,ye4+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+12,ye4,xe4+16,ye4+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+36,ye4+8,xe4+32,ye4+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+16,ye4+8,xe4+20,ye4+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+12,ye4+8,xe4+40,ye4+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+8,ye4+16,xe4+16,ye4+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+32,ye4+16,xe4+20,ye4+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+36,ye4+16,xe4+44,ye4+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+8,ye4+16,xe4+48,ye4+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+8,ye4+16,xe4+48,ye4+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+8,ye4+16,xe4+4,ye4+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+44,ye4+16,xe4+48,ye4+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+12,ye4+20,xe4+40,ye4+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+16,ye4+28,xe4+12,ye4+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+36,ye4+28,xe4+40,ye4+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+24,ye4+28,xe4+16,ye4+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe4+36,ye4+28,xe4+28,ye4+32,fill="gray",outline="gray",width=0))
    liste_ennemis[3].append(Ennemis)
    xe4=xe4+60

def dessine_mob_30_1():     # dernière ligne face au joueur
    global liste_ennemis,liste_coordennemis,xe5,ye5,nb_ennemis
    liste_coordennemis[4].append([xe5,ye5])
    Ennemis=[]
    Ennemis.append(game.create_rectangle(xe5+24,ye5,xe5+32,ye5+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+36,ye5+8,xe5+20,ye5+4,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+40,ye5+8,xe5+16,ye5+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+20,ye5+16,xe5+12,ye5+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+24,ye5+16,xe5+32,ye5+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+44,ye5+16,xe5+36,ye5+12,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+44,ye5+16,xe5+12,ye5+20,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+24,ye5+20,xe5+20,ye5+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+36,ye5+20,xe5+32,ye5+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+24,ye5+24,xe5+32,ye5+28,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+16,ye5+28,xe5+20,ye5+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+36,ye5+28,xe5+40,ye5+24,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+24,ye5+28,xe5+20,ye5+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+36,ye5+28,xe5+32,ye5+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+16,ye5+28,xe5+12,ye5+32,fill="gray",outline="gray",width=0))
    Ennemis.append(game.create_rectangle(xe5+44,ye5+28,xe5+40,ye5+32,fill="gray",outline="gray",width=0))
    liste_ennemis[4].append(Ennemis)
    xe5=xe5+60


#La suite du code est dédié à la création/animation du mob bonus

def launch_Bonus():     # le mob bonus apparait de manière aléatoires sur 1 min 30,
                        #     j'ai choisit de réduire le une chance par milliseconde par une chance par centièmes de secondes pour soulager le programem
    RNG=randint(0,900)
    if RNG==777:
        dessine_mob_Bonus()
    else:
        game.after(100,launch_Bonus)

def dessine_mob_Bonus():     # le dessin du mob bonus est gardé indépendant de la liste des autres mob pour des raison évidentes du fait qu'il soit désynchro
    global mob_bonus,pos_mob_bonus,col_mob_bonus1,col_mob_bonus2,luck,dir_bonus
    if luck!= 1:
        luck=1
        mob_bonus=[]
        d_g=randint(1,2)
        if d_g==2:
            dir_bonus=-4
            pos_mob_bonus=POINT(-72,50)
        else:
            dir_bonus=4
            pos_mob_bonus=POINT(740,50)
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+20,pos_mob_bonus.y,pos_mob_bonus.x+52,pos_mob_bonus.y+4,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+12,pos_mob_bonus.y+4,pos_mob_bonus.x+60,pos_mob_bonus.y+8,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+8,pos_mob_bonus.y+8,pos_mob_bonus.x+64,pos_mob_bonus.y+12,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+5,pos_mob_bonus.y+12,pos_mob_bonus.x+13,pos_mob_bonus.y+16,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+18,pos_mob_bonus.y+12,pos_mob_bonus.x+26,pos_mob_bonus.y+16,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+31,pos_mob_bonus.y+12,pos_mob_bonus.x+40,pos_mob_bonus.y+16,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+45,pos_mob_bonus.y+12,pos_mob_bonus.x+54,pos_mob_bonus.y+16,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+59,pos_mob_bonus.y+12,pos_mob_bonus.x+68,pos_mob_bonus.y+16,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x,pos_mob_bonus.y+16,pos_mob_bonus.x+72,pos_mob_bonus.y+20,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+9,pos_mob_bonus.y+24,pos_mob_bonus.x+22,pos_mob_bonus.y+20,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+63,pos_mob_bonus.y+24,pos_mob_bonus.x+50,pos_mob_bonus.y+20,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+31,pos_mob_bonus.y+24,pos_mob_bonus.x+40,pos_mob_bonus.y+20,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+13,pos_mob_bonus.y+24,pos_mob_bonus.x+18,pos_mob_bonus.y+28,fill="red",outline="red",width=0))
        mob_bonus.append(game.create_rectangle(pos_mob_bonus.x+59,pos_mob_bonus.y+24,pos_mob_bonus.x+54,pos_mob_bonus.y+28,fill="red",outline="red",width=0))
        col_mob_bonus1=POINT(pos_mob_bonus.x,50)
        col_mob_bonus2=POINT(pos_mob_bonus.x+72,78)
        Animations_mob_Bonus()


def Animations_mob_Bonus():     # évidemment le mob bonus fait un mouvement horizontal d'un bout à l'autre de l'écran
    global pos_mob_bonus,mob_bonus,col_mob_bonus1,col_mob_bonus2,luck,dir_bonus
    if luck==1:
        pos_mob_bonus.x=pos_mob_bonus.x-dir_bonus
        if pos_mob_bonus.x<=-72 or pos_mob_bonus.x>=840:
            luck=0
            erase_bonus()
            col_mob_bonus1=POINT(0,0)
            col_mob_bonus2=POINT(0,0)
            launch_Bonus()
        else:
            game.coords(mob_bonus[0],pos_mob_bonus.x+20,pos_mob_bonus.y,pos_mob_bonus.x+52,pos_mob_bonus.y+4)
            game.coords(mob_bonus[1],pos_mob_bonus.x+12,pos_mob_bonus.y+4,pos_mob_bonus.x+60,pos_mob_bonus.y+8)
            game.coords(mob_bonus[2],pos_mob_bonus.x+8,pos_mob_bonus.y+8,pos_mob_bonus.x+64,pos_mob_bonus.y+12)
            game.coords(mob_bonus[3],pos_mob_bonus.x+5,pos_mob_bonus.y+12,pos_mob_bonus.x+13,pos_mob_bonus.y+16)
            game.coords(mob_bonus[4],pos_mob_bonus.x+18,pos_mob_bonus.y+12,pos_mob_bonus.x+26,pos_mob_bonus.y+16)
            game.coords(mob_bonus[5],pos_mob_bonus.x+31,pos_mob_bonus.y+12,pos_mob_bonus.x+40,pos_mob_bonus.y+16)
            game.coords(mob_bonus[6],pos_mob_bonus.x+45,pos_mob_bonus.y+12,pos_mob_bonus.x+54,pos_mob_bonus.y+16)
            game.coords(mob_bonus[7],pos_mob_bonus.x+59,pos_mob_bonus.y+12,pos_mob_bonus.x+68,pos_mob_bonus.y+16)
            game.coords(mob_bonus[8],pos_mob_bonus.x,pos_mob_bonus.y+16,pos_mob_bonus.x+72,pos_mob_bonus.y+20)
            game.coords(mob_bonus[9],pos_mob_bonus.x+9,pos_mob_bonus.y+24,pos_mob_bonus.x+22,pos_mob_bonus.y+20)
            game.coords(mob_bonus[10],pos_mob_bonus.x+63,pos_mob_bonus.y+24,pos_mob_bonus.x+50,pos_mob_bonus.y+20)
            game.coords(mob_bonus[11],pos_mob_bonus.x+31,pos_mob_bonus.y+24,pos_mob_bonus.x+40,pos_mob_bonus.y+20)
            game.coords(mob_bonus[12],pos_mob_bonus.x+13,pos_mob_bonus.y+24,pos_mob_bonus.x+18,pos_mob_bonus.y+28)
            game.coords(mob_bonus[13],pos_mob_bonus.x+59,pos_mob_bonus.y+24,pos_mob_bonus.x+54,pos_mob_bonus.y+28)
            col_mob_bonus1=POINT(pos_mob_bonus.x,50)
            col_mob_bonus2=POINT(pos_mob_bonus.x+72,78)
            home.after(15,Animations_mob_Bonus)

def erase_bonus():     # Ceci permet au mob Bonus de disparaitre si le joueur à été incapable de le détruire
    game.delete(mob_bonus[0])
    game.delete(mob_bonus[1])
    game.delete(mob_bonus[2])
    game.delete(mob_bonus[3])
    game.delete(mob_bonus[4])
    game.delete(mob_bonus[5])
    game.delete(mob_bonus[6])
    game.delete(mob_bonus[7])
    game.delete(mob_bonus[8])
    game.delete(mob_bonus[9])
    game.delete(mob_bonus[10])
    game.delete(mob_bonus[11])
    game.delete(mob_bonus[12])
    game.delete(mob_bonus[13])

#je vais maintenant définir les mouvement du vaisseau

# les deux fonctions précédente vont définir si le joueur veut que le vaisseau aille à droite ou à gauche
def right(e):
    if lancement==1:
        global pos_vaisseau
        if pos_vaisseau.x<840-25:
            move(8)

def left(e):
    if lancement==1:
        global pos_vaisseau
        if 25<pos_vaisseau.x:
            move(-8)

def move(v_vaisseau):     # La fonction qui suit fait bouger le vaisseau vers la droite/gauche selon les désir du joueur
    global pos_vaisseau,pos_canon1,pos_canon2,col_vaisseau1,col_vaisseau2
    pos_vaisseau.x=pos_vaisseau.x+v_vaisseau
    game.coords(vaisseau[0],pos_vaisseau.x-22,pos_vaisseau.y+6,pos_vaisseau.x+22,pos_vaisseau.y+14)
    game.coords(vaisseau[1],pos_vaisseau.x-18,pos_vaisseau.y+2,pos_vaisseau.x+18,pos_vaisseau.y+6)
    game.coords(vaisseau[2],pos_vaisseau.x-6,pos_vaisseau.y-6,pos_vaisseau.x+6,pos_vaisseau.y+2)
    game.coords(vaisseau[3],pos_vaisseau.x-2,pos_vaisseau.y-10,pos_vaisseau.x+2,pos_vaisseau.y-6)
    pos_canon1=POINT(pos_vaisseau.x-2,pos_vaisseau.y-10)
    pos_canon2=POINT(pos_vaisseau.x+2,pos_vaisseau.y-6)
    col_vaisseau1=POINT(pos_vaisseau.x-22,pos_vaisseau.y-10)
    col_vaisseau2=POINT(pos_vaisseau.x+22,pos_vaisseau.y+14)

# Les fonctions suivantes définissent le système de tir du joueur
def chargement_laser(e):     # cette fonction empêche le joueur de tirer 2 laser, ou encore d'accélerer le laser déja présent
    if feu!=1:
        tir_joueur()

def tir_joueur():     # Ceci définit l'apparition du laser à la position du vaisseau
    if lancement==1:
        global pos_canon1,xtir,ytir,projectile,feu
        if feu!=1 :
            feu=1
            xtir=pos_canon1.x
            ytir=pos_canon1.y
            projectile=[(game.create_rectangle(xtir,ytir,xtir+4,ytir-32,fill='yellow'))]

        AnimationLaser()

def AnimationLaser():     # ceci gère l'animation et les collision du laser avec les ennemis
    global xtir,ytir,projectile,feu,nb_ennemis,Score,col_mob_bonus1,col_mob_bonus2
    if feu==1:
        ytir=ytir-10
        abri()
        if ytir<=20:
            feu=0
            game.delete(projectile)
        elif col_mob_bonus1.x<xtir<col_mob_bonus2.x and ytir<=col_mob_bonus2.y:
            game.delete(projectile)
            erase_bonus()
            point_win=(randint(1,6))*50
            MaJ_Score(point_win)

        i=0
        t=0

        while i<len(liste_coordennemis):      # il est évidemment inutile de chercher à gérer les collision si il n'y à pas d'ennemis à détruire

            if len(liste_coordennemis)>=1:
                if len(liste_coordennemis[i])>=1:
                    while t<len(liste_coordennemis[i]):
                        if xtir+5>=liste_coordennemis[i][t][0] and xtir-5<=liste_coordennemis[i][t][0]+60 :
                            if ytir<=liste_coordennemis[i][t][1]+60 and ytir>=liste_coordennemis[i][t][1]-60 :
                                xtir,ytir=0,0
                                if i==0 or i==1:
                                    MaJ_Score(10)
                                    nb_ennemis=nb_ennemis-1
                                elif i==2 or i==3:
                                    MaJ_Score(20)
                                    nb_ennemis=nb_ennemis-1
                                elif i==4:
                                    MaJ_Score(30)
                                    nb_ennemis=nb_ennemis-1
                                feu=0
                                game.delete(projectile[0])
                                if i==0:
                                    Nb_Ennemis[0]=Nb_Ennemis[0]-1
                                    game.delete(liste_ennemis[i][t][0])
                                    game.delete(liste_ennemis[i][t][1])
                                    game.delete(liste_ennemis[i][t][2])
                                    game.delete(liste_ennemis[i][t][3])
                                    game.delete(liste_ennemis[i][t][4])
                                    game.delete(liste_ennemis[i][t][5])
                                    game.delete(liste_ennemis[i][t][6])
                                    game.delete(liste_ennemis[i][t][7])
                                    game.delete(liste_ennemis[i][t][8])
                                    game.delete(liste_ennemis[i][t][9])
                                    game.delete(liste_ennemis[i][t][10])
                                    game.delete(liste_ennemis[i][t][11])
                                    game.delete(liste_ennemis[i][t][12])
                                    game.delete(liste_ennemis[i][t][13])
                                    del liste_ennemis[i][t]
                                    del liste_coordennemis[i][t]
                                elif i==1:
                                    Nb_Ennemis[1]=Nb_Ennemis[1]-1
                                    game.delete(liste_ennemis[i][t][0])
                                    game.delete(liste_ennemis[i][t][1])
                                    game.delete(liste_ennemis[i][t][2])
                                    game.delete(liste_ennemis[i][t][3])
                                    game.delete(liste_ennemis[i][t][4])
                                    game.delete(liste_ennemis[i][t][5])
                                    game.delete(liste_ennemis[i][t][6])
                                    game.delete(liste_ennemis[i][t][7])
                                    game.delete(liste_ennemis[i][t][8])
                                    game.delete(liste_ennemis[i][t][9])
                                    game.delete(liste_ennemis[i][t][10])
                                    game.delete(liste_ennemis[i][t][11])
                                    game.delete(liste_ennemis[i][t][12])
                                    game.delete(liste_ennemis[i][t][13])
                                    del liste_ennemis[i][t]
                                    del liste_coordennemis[i][t]
                                elif i==2:
                                    Nb_Ennemis[2]=Nb_Ennemis[2]-1
                                    game.delete(liste_ennemis[i][t][0])
                                    game.delete(liste_ennemis[i][t][1])
                                    game.delete(liste_ennemis[i][t][2])
                                    game.delete(liste_ennemis[i][t][3])
                                    game.delete(liste_ennemis[i][t][4])
                                    game.delete(liste_ennemis[i][t][5])
                                    game.delete(liste_ennemis[i][t][6])
                                    game.delete(liste_ennemis[i][t][7])
                                    game.delete(liste_ennemis[i][t][8])
                                    game.delete(liste_ennemis[i][t][9])
                                    game.delete(liste_ennemis[i][t][10])
                                    game.delete(liste_ennemis[i][t][11])
                                    game.delete(liste_ennemis[i][t][12])
                                    game.delete(liste_ennemis[i][t][13])
                                    game.delete(liste_ennemis[i][t][14])
                                    game.delete(liste_ennemis[i][t][15])
                                    game.delete(liste_ennemis[i][t][16])
                                    del liste_ennemis[i][t]
                                    del liste_coordennemis[i][t]
                                elif i==3:
                                    Nb_Ennemis[3]=Nb_Ennemis[3]-1
                                    game.delete(liste_ennemis[i][t][0])
                                    game.delete(liste_ennemis[i][t][1])
                                    game.delete(liste_ennemis[i][t][2])
                                    game.delete(liste_ennemis[i][t][3])
                                    game.delete(liste_ennemis[i][t][4])
                                    game.delete(liste_ennemis[i][t][5])
                                    game.delete(liste_ennemis[i][t][6])
                                    game.delete(liste_ennemis[i][t][7])
                                    game.delete(liste_ennemis[i][t][8])
                                    game.delete(liste_ennemis[i][t][9])
                                    game.delete(liste_ennemis[i][t][10])
                                    game.delete(liste_ennemis[i][t][11])
                                    game.delete(liste_ennemis[i][t][12])
                                    game.delete(liste_ennemis[i][t][13])
                                    game.delete(liste_ennemis[i][t][14])
                                    game.delete(liste_ennemis[i][t][15])
                                    game.delete(liste_ennemis[i][t][16])
                                    del liste_ennemis[i][t]
                                    del liste_coordennemis[i][t]
                                elif i==4:
                                    Nb_Ennemis[4]=Nb_Ennemis[4]-1
                                    game.delete(liste_ennemis[i][t][0])
                                    game.delete(liste_ennemis[i][t][1])
                                    game.delete(liste_ennemis[i][t][2])
                                    game.delete(liste_ennemis[i][t][3])
                                    game.delete(liste_ennemis[i][t][4])
                                    game.delete(liste_ennemis[i][t][5])
                                    game.delete(liste_ennemis[i][t][6])
                                    game.delete(liste_ennemis[i][t][7])
                                    game.delete(liste_ennemis[i][t][8])
                                    game.delete(liste_ennemis[i][t][9])
                                    game.delete(liste_ennemis[i][t][10])
                                    game.delete(liste_ennemis[i][t][11])
                                    game.delete(liste_ennemis[i][t][12])
                                    game.delete(liste_ennemis[i][t][13])
                                    game.delete(liste_ennemis[i][t][14])
                                    game.delete(liste_ennemis[i][t][15])
                                    del liste_ennemis[i][t]
                                    del liste_coordennemis[i][t]

                        t+=1
                t=0
                i+=1

        else:
            game.coords(projectile[0],xtir,ytir,xtir+4,ytir-32)
            home.after(50,AnimationLaser)



def ennemis():     # Ceci permet d'effectuer l'animation de l'ennemi
    global v_ennemies,nb_ennemis,liste_coordennemis,DebutJeu,feu
    global liste_ennemis,PasAvancement,Nb_Ennemis

    if len(Nb_Ennemis)>=1 and lancement!=0:

        if Nb_Ennemis!=0:     # ceci empêche l'animation des ennemis si il n'y en à pas
            i=0
            t=0
            PasAvancement+=1

            tir_ennemi()

            # comme dans le jeu de base si les ennemis atteignent le bas de l'écran  YOU DIE!!!

            while i<len(liste_coordennemis):
                while t<len(liste_coordennemis[i]):
                    if liste_coordennemis[i][t][1]>=790:
                        game.delete(ALL)
                        game.create_text(320,240,font=('Fixedsys',18),text="Game Over !!",fill='red')
                        feu=0
                        game.delete(vaisseau[0])
                        game.delete(vaisseau[1])
                        game.delete(vaisseau[2])
                        game.delete(vaisseau[3])
                        DebutJeu=0
                        new_HighScore(Score)
                        pos_vaisseau=POINT(0,0)
                    t+=1
                t=0
                i+=1

            i=0

            # La suite du code permet de définir l'inversion de direction des mob lorsqu'ils atteignent la fin de l'écran

            dy=0


            if v_ennemies>0:

                v_ennemies2=v_ennemies
                if len(liste_coordennemis[0])!=0:
                    if liste_coordennemis[0][len(liste_coordennemis[0])-1][0]>=794:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[1])!=0:
                    if liste_coordennemis[1][len(liste_coordennemis[1])-1][0]>=794:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[2])!=0:
                    if liste_coordennemis[2][len(liste_coordennemis[2])-1][0]>=794:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[3])!=0:
                    if liste_coordennemis[3][len(liste_coordennemis[3])-1][0]>=794:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[4])!=0:
                    if liste_coordennemis[4][len(liste_coordennemis[4])-1][0]>=794:
                        v_ennemies=-v_ennemies2
                        dy=10
            elif v_ennemies<0:
                v_ennemies2=v_ennemies
                if len(liste_coordennemis[0])!=0:
                    if liste_coordennemis[0][0][0]<=0:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[1])!=0:
                    if liste_coordennemis[1][0][0]<=0:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[2])!=0:
                    if liste_coordennemis[2][0][0]<=0:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[3])!=0:
                    if liste_coordennemis[3][0][0]<=0:
                        v_ennemies=-v_ennemies2
                        dy=10
                if len(liste_coordennemis[4])!=0:
                    if liste_coordennemis[4][0][0]<=0:
                        v_ennemies=-v_ennemies2
                        dy=10


            i=0
            t=0

            # Il reste plus qu'a faire avancer les ennemis

            while i<len(liste_coordennemis):
                while t<len(liste_coordennemis[i]):
                    liste_coordennemis[i][t][0]=liste_coordennemis[i][t][0]+v_ennemies
                    liste_coordennemis[i][t][1]=liste_coordennemis[i][t][1]+dy
                    t+=1
                i+=1
                t=0
            i=0
            while i<Nb_Ennemis[0]:
                game.coords(liste_ennemis[0][i][0],liste_coordennemis[0][i][0]+16,liste_coordennemis[0][i][1],liste_coordennemis[0][i][0]+32,liste_coordennemis[0][i][1]+4)
                game.coords(liste_ennemis[0][i][1],liste_coordennemis[0][i][0]+4,liste_coordennemis[0][i][1]+8,liste_coordennemis[0][i][0]+44,liste_coordennemis[0][i][1]+4)
                game.coords(liste_ennemis[0][i][2],liste_coordennemis[0][i][0],liste_coordennemis[0][i][1]+12,liste_coordennemis[0][i][0]+48,liste_coordennemis[0][i][1]+8)
                game.coords(liste_ennemis[0][i][3],liste_coordennemis[0][i][0],liste_coordennemis[0][i][1]+12,liste_coordennemis[0][i][0]+12,liste_coordennemis[0][i][1]+16)
                game.coords(liste_ennemis[0][i][4],liste_coordennemis[0][i][0]+20,liste_coordennemis[0][i][1]+12,liste_coordennemis[0][i][0]+28,liste_coordennemis[0][i][1]+16)
                game.coords(liste_ennemis[0][i][5],liste_coordennemis[0][i][0]+36,liste_coordennemis[0][i][1]+12,liste_coordennemis[0][i][0]+48,liste_coordennemis[0][i][1]+16)
                game.coords(liste_ennemis[0][i][6],liste_coordennemis[0][i][0],liste_coordennemis[0][i][1]+16,liste_coordennemis[0][i][0]+48,liste_coordennemis[0][i][1]+20)
                game.coords(liste_ennemis[0][i][7],liste_coordennemis[0][i][0]+8,liste_coordennemis[0][i][1]+20,liste_coordennemis[0][i][0]+20,liste_coordennemis[0][i][1]+24)
                game.coords(liste_ennemis[0][i][8],liste_coordennemis[0][i][0]+28,liste_coordennemis[0][i][1]+20,liste_coordennemis[0][i][0]+40,liste_coordennemis[0][i][1]+24)
                game.coords(liste_ennemis[0][i][9],liste_coordennemis[0][i][0]+4,liste_coordennemis[0][i][1]+24,liste_coordennemis[0][i][0]+12,liste_coordennemis[0][i][1]+28)
                game.coords(liste_ennemis[0][i][10],liste_coordennemis[0][i][0]+20,liste_coordennemis[0][i][1]+24,liste_coordennemis[0][i][0]+28,liste_coordennemis[0][i][1]+28)
                game.coords(liste_ennemis[0][i][11],liste_coordennemis[0][i][0]+36,liste_coordennemis[0][i][1]+24,liste_coordennemis[0][i][0]+44,liste_coordennemis[0][i][1]+28)
                game.coords(liste_ennemis[0][i][12],liste_coordennemis[0][i][0]+8,liste_coordennemis[0][i][1]+28,liste_coordennemis[0][i][0]+16,liste_coordennemis[0][i][1]+32)
                game.coords(liste_ennemis[0][i][13],liste_coordennemis[0][i][0]+32,liste_coordennemis[0][i][1]+28,liste_coordennemis[0][i][0]+40,liste_coordennemis[0][i][1]+32)
                i+=1
            i=0
            while i<Nb_Ennemis[1]:
                game.coords(liste_ennemis[1][i][0],liste_coordennemis[1][i][0]+16,liste_coordennemis[1][i][1],liste_coordennemis[1][i][0]+32,liste_coordennemis[1][i][1]+4)
                game.coords(liste_ennemis[1][i][1],liste_coordennemis[1][i][0]+4,liste_coordennemis[1][i][1]+8,liste_coordennemis[1][i][0]+44,liste_coordennemis[1][i][1]+4)
                game.coords(liste_ennemis[1][i][2],liste_coordennemis[1][i][0],liste_coordennemis[1][i][1]+12,liste_coordennemis[1][i][0]+48,liste_coordennemis[1][i][1]+8)
                game.coords(liste_ennemis[1][i][3],liste_coordennemis[1][i][0],liste_coordennemis[1][i][1]+12,liste_coordennemis[1][i][0]+12,liste_coordennemis[1][i][1]+16)
                game.coords(liste_ennemis[1][i][4],liste_coordennemis[1][i][0]+20,liste_coordennemis[1][i][1]+12,liste_coordennemis[1][i][0]+28,liste_coordennemis[1][i][1]+16)
                game.coords(liste_ennemis[1][i][5],liste_coordennemis[1][i][0]+36,liste_coordennemis[1][i][1]+12,liste_coordennemis[1][i][0]+48,liste_coordennemis[1][i][1]+16)
                game.coords(liste_ennemis[1][i][6],liste_coordennemis[1][i][0],liste_coordennemis[1][i][1]+16,liste_coordennemis[1][i][0]+48,liste_coordennemis[1][i][1]+20)
                game.coords(liste_ennemis[1][i][7],liste_coordennemis[1][i][0]+8,liste_coordennemis[1][i][1]+20,liste_coordennemis[1][i][0]+20,liste_coordennemis[1][i][1]+24)
                game.coords(liste_ennemis[1][i][8],liste_coordennemis[1][i][0]+28,liste_coordennemis[1][i][1]+20,liste_coordennemis[1][i][0]+40,liste_coordennemis[1][i][1]+24)
                game.coords(liste_ennemis[1][i][9],liste_coordennemis[1][i][0]+4,liste_coordennemis[1][i][1]+24,liste_coordennemis[1][i][0]+12,liste_coordennemis[1][i][1]+28)
                game.coords(liste_ennemis[1][i][10],liste_coordennemis[1][i][0]+20,liste_coordennemis[1][i][1]+24,liste_coordennemis[1][i][0]+28,liste_coordennemis[1][i][1]+28)
                game.coords(liste_ennemis[1][i][11],liste_coordennemis[1][i][0]+36,liste_coordennemis[1][i][1]+24,liste_coordennemis[1][i][0]+44,liste_coordennemis[1][i][1]+28)
                game.coords(liste_ennemis[1][i][12],liste_coordennemis[1][i][0]+8,liste_coordennemis[1][i][1]+28,liste_coordennemis[1][i][0]+16,liste_coordennemis[1][i][1]+32)
                game.coords(liste_ennemis[1][i][13],liste_coordennemis[1][i][0]+32,liste_coordennemis[1][i][1]+28,liste_coordennemis[1][i][0]+40,liste_coordennemis[1][i][1]+32)
                i+=1
            i=0
            while i<Nb_Ennemis[2]:
                game.coords(liste_ennemis[2][i][0],liste_coordennemis[2][i][0]+36,liste_coordennemis[2][i][1],liste_coordennemis[2][i][0]+40,liste_coordennemis[2][i][1]+4)
                game.coords(liste_ennemis[2][i][1],liste_coordennemis[2][i][0]+12,liste_coordennemis[2][i][1],liste_coordennemis[2][i][0]+16,liste_coordennemis[2][i][1]+4)
                game.coords(liste_ennemis[2][i][2],liste_coordennemis[2][i][0]+36,liste_coordennemis[2][i][1]+8,liste_coordennemis[2][i][0]+32,liste_coordennemis[2][i][1]+4)
                game.coords(liste_ennemis[2][i][3],liste_coordennemis[2][i][0]+16,liste_coordennemis[2][i][1]+8,liste_coordennemis[2][i][0]+20,liste_coordennemis[2][i][1]+4)
                game.coords(liste_ennemis[2][i][4],liste_coordennemis[2][i][0]+12,liste_coordennemis[2][i][1]+8,liste_coordennemis[2][i][0]+40,liste_coordennemis[2][i][1]+12)
                game.coords(liste_ennemis[2][i][5],liste_coordennemis[2][i][0]+8,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+16,liste_coordennemis[2][i][1]+12)
                game.coords(liste_ennemis[2][i][6],liste_coordennemis[2][i][0]+32,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+20,liste_coordennemis[2][i][1]+12)
                game.coords(liste_ennemis[2][i][7],liste_coordennemis[2][i][0]+36,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+44,liste_coordennemis[2][i][1]+12)
                game.coords(liste_ennemis[2][i][8],liste_coordennemis[2][i][0]+8,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+48,liste_coordennemis[2][i][1]+20)
                game.coords(liste_ennemis[2][i][9],liste_coordennemis[2][i][0]+8,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+48,liste_coordennemis[2][i][1]+20)
                game.coords(liste_ennemis[2][i][10],liste_coordennemis[2][i][0]+8,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+4,liste_coordennemis[2][i][1]+28)
                game.coords(liste_ennemis[2][i][11],liste_coordennemis[2][i][0]+44,liste_coordennemis[2][i][1]+16,liste_coordennemis[2][i][0]+48,liste_coordennemis[2][i][1]+28)
                game.coords(liste_ennemis[2][i][12],liste_coordennemis[2][i][0]+12,liste_coordennemis[2][i][1]+20,liste_coordennemis[2][i][0]+40,liste_coordennemis[2][i][1]+24)
                game.coords(liste_ennemis[2][i][13],liste_coordennemis[2][i][0]+16,liste_coordennemis[2][i][1]+28,liste_coordennemis[2][i][0]+12,liste_coordennemis[2][i][1]+24)
                game.coords(liste_ennemis[2][i][14],liste_coordennemis[2][i][0]+36,liste_coordennemis[2][i][1]+28,liste_coordennemis[2][i][0]+40,liste_coordennemis[2][i][1]+24)
                game.coords(liste_ennemis[2][i][15],liste_coordennemis[2][i][0]+24,liste_coordennemis[2][i][1]+28,liste_coordennemis[2][i][0]+16,liste_coordennemis[2][i][1]+32)
                game.coords(liste_ennemis[2][i][16],liste_coordennemis[2][i][0]+36,liste_coordennemis[2][i][1]+28,liste_coordennemis[2][i][0]+28,liste_coordennemis[2][i][1]+32)
                i+=1
            i=0
            while i<Nb_Ennemis[3]:
                game.coords(liste_ennemis[3][i][0],liste_coordennemis[3][i][0]+36,liste_coordennemis[3][i][1],liste_coordennemis[3][i][0]+40,liste_coordennemis[3][i][1]+4)
                game.coords(liste_ennemis[3][i][1],liste_coordennemis[3][i][0]+12,liste_coordennemis[3][i][1],liste_coordennemis[3][i][0]+16,liste_coordennemis[3][i][1]+4)
                game.coords(liste_ennemis[3][i][2],liste_coordennemis[3][i][0]+36,liste_coordennemis[3][i][1]+8,liste_coordennemis[3][i][0]+32,liste_coordennemis[3][i][1]+4)
                game.coords(liste_ennemis[3][i][3],liste_coordennemis[3][i][0]+16,liste_coordennemis[3][i][1]+8,liste_coordennemis[3][i][0]+20,liste_coordennemis[3][i][1]+4)
                game.coords(liste_ennemis[3][i][4],liste_coordennemis[3][i][0]+12,liste_coordennemis[3][i][1]+8,liste_coordennemis[3][i][0]+40,liste_coordennemis[3][i][1]+12)
                game.coords(liste_ennemis[3][i][5],liste_coordennemis[3][i][0]+8,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+16,liste_coordennemis[3][i][1]+12)
                game.coords(liste_ennemis[3][i][6],liste_coordennemis[3][i][0]+32,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+20,liste_coordennemis[3][i][1]+12)
                game.coords(liste_ennemis[3][i][7],liste_coordennemis[3][i][0]+36,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+44,liste_coordennemis[3][i][1]+12)
                game.coords(liste_ennemis[3][i][8],liste_coordennemis[3][i][0]+8,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+48,liste_coordennemis[3][i][1]+20)
                game.coords(liste_ennemis[3][i][9],liste_coordennemis[3][i][0]+8,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+48,liste_coordennemis[3][i][1]+20)
                game.coords(liste_ennemis[3][i][10],liste_coordennemis[3][i][0]+8,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+4,liste_coordennemis[3][i][1]+28)
                game.coords(liste_ennemis[3][i][11],liste_coordennemis[3][i][0]+44,liste_coordennemis[3][i][1]+16,liste_coordennemis[3][i][0]+48,liste_coordennemis[3][i][1]+28)
                game.coords(liste_ennemis[3][i][12],liste_coordennemis[3][i][0]+12,liste_coordennemis[3][i][1]+20,liste_coordennemis[3][i][0]+40,liste_coordennemis[3][i][1]+24)
                game.coords(liste_ennemis[3][i][13],liste_coordennemis[3][i][0]+16,liste_coordennemis[3][i][1]+28,liste_coordennemis[3][i][0]+12,liste_coordennemis[3][i][1]+24)
                game.coords(liste_ennemis[3][i][14],liste_coordennemis[3][i][0]+36,liste_coordennemis[3][i][1]+28,liste_coordennemis[3][i][0]+40,liste_coordennemis[3][i][1]+24)
                game.coords(liste_ennemis[3][i][15],liste_coordennemis[3][i][0]+24,liste_coordennemis[3][i][1]+28,liste_coordennemis[3][i][0]+16,liste_coordennemis[3][i][1]+32)
                game.coords(liste_ennemis[3][i][16],liste_coordennemis[3][i][0]+36,liste_coordennemis[3][i][1]+28,liste_coordennemis[3][i][0]+28,liste_coordennemis[3][i][1]+32)
                i+=1
            i=0
            while i<Nb_Ennemis[4]:
                game.coords(liste_ennemis[4][i][0],liste_coordennemis[4][i][0]+24,liste_coordennemis[4][i][1],liste_coordennemis[4][i][0]+32,liste_coordennemis[4][i][1]+4)
                game.coords(liste_ennemis[4][i][1],liste_coordennemis[4][i][0]+36,liste_coordennemis[4][i][1]+8,liste_coordennemis[4][i][0]+20,liste_coordennemis[4][i][1]+4)
                game.coords(liste_ennemis[4][i][2],liste_coordennemis[4][i][0]+40,liste_coordennemis[4][i][1]+8,liste_coordennemis[4][i][0]+16,liste_coordennemis[4][i][1]+12)
                game.coords(liste_ennemis[4][i][3],liste_coordennemis[4][i][0]+20,liste_coordennemis[4][i][1]+16,liste_coordennemis[4][i][0]+12,liste_coordennemis[4][i][1]+12)
                game.coords(liste_ennemis[4][i][4],liste_coordennemis[4][i][0]+24,liste_coordennemis[4][i][1]+16,liste_coordennemis[4][i][0]+32,liste_coordennemis[4][i][1]+12)
                game.coords(liste_ennemis[4][i][5],liste_coordennemis[4][i][0]+44,liste_coordennemis[4][i][1]+16,liste_coordennemis[4][i][0]+36,liste_coordennemis[4][i][1]+12)
                game.coords(liste_ennemis[4][i][6],liste_coordennemis[4][i][0]+44,liste_coordennemis[4][i][1]+16,liste_coordennemis[4][i][0]+12,liste_coordennemis[4][i][1]+20)
                game.coords(liste_ennemis[4][i][7],liste_coordennemis[4][i][0]+24,liste_coordennemis[4][i][1]+20,liste_coordennemis[4][i][0]+20,liste_coordennemis[4][i][1]+24)
                game.coords(liste_ennemis[4][i][8],liste_coordennemis[4][i][0]+36,liste_coordennemis[4][i][1]+20,liste_coordennemis[4][i][0]+32,liste_coordennemis[4][i][1]+24)
                game.coords(liste_ennemis[4][i][9],liste_coordennemis[4][i][0]+24,liste_coordennemis[4][i][1]+24,liste_coordennemis[4][i][0]+32,liste_coordennemis[4][i][1]+28)
                game.coords(liste_ennemis[4][i][10],liste_coordennemis[4][i][0]+16,liste_coordennemis[4][i][1]+28,liste_coordennemis[4][i][0]+20,liste_coordennemis[4][i][1]+24)
                game.coords(liste_ennemis[4][i][11],liste_coordennemis[4][i][0]+36,liste_coordennemis[4][i][1]+28,liste_coordennemis[4][i][0]+40,liste_coordennemis[4][i][1]+24)
                game.coords(liste_ennemis[4][i][12],liste_coordennemis[4][i][0]+24,liste_coordennemis[4][i][1]+28,liste_coordennemis[4][i][0]+20,liste_coordennemis[4][i][1]+32)
                game.coords(liste_ennemis[4][i][13],liste_coordennemis[4][i][0]+36,liste_coordennemis[4][i][1]+28,liste_coordennemis[4][i][0]+32,liste_coordennemis[4][i][1]+32)
                game.coords(liste_ennemis[4][i][14],liste_coordennemis[4][i][0]+16,liste_coordennemis[4][i][1]+28,liste_coordennemis[4][i][0]+12,liste_coordennemis[4][i][1]+32)
                game.coords(liste_ennemis[4][i][15],liste_coordennemis[4][i][0]+44,liste_coordennemis[4][i][1]+28,liste_coordennemis[4][i][0]+40,liste_coordennemis[4][i][1]+32)
                i+=1
            home.after(25,ennemis)
    else:
        home.after(25,ennemis)

def tir_ennemi():     # je définit l'animation de tir des mob
    global feu_ennemi,Xlaser,Ylaser,laserEnnemi,liste_coordennemis,EnnemiChoisi,ChoixTireur,Nb_Ennemis,lancement
    if lancement!=0:
        if feu_ennemi!=1 :
            feu_ennemi=1
            laserEnnemi=[]
            Choix=randint(0,4)

            if len(laserEnnemi)!=1:
                if Choix==0:
                    if Nb_Ennemis[0]!=0:

                            CanonChoisi=randrange(0,3,1)

                            ChoixTireur=[]
                            ChoixTireur.append([liste_coordennemis[0][randrange(0,Nb_Ennemis[0],1)][0],liste_coordennemis[0][randrange(0,Nb_Ennemis[0],1)][1]])
                            Xobus=ChoixTireur[0][0]+9
                            Yobus=ChoixTireur[0][1]+40

                            if CanonChoisi==1:
                                laserEnnemi.append(game.create_rectangle(Xobus,Yobus,Xobus+2,Yobus+40,fill='orange'))
                            else:
                                Xobus=Xobus+40
                                laserEnnemi.append(game.create_rectangle(Xobus,Yobus,Xobus+2,Yobus+40,fill='orange'))

                elif Choix==1:
                    if Nb_Ennemis[1]!=0:

                        ChoixTireur=[]
                        ChoixTireur.append([liste_coordennemis[1][randrange(0,Nb_Ennemis[1],1)][0],liste_coordennemis[1][randrange(0,Nb_Ennemis[1],1)][1]])
                        Xlaser=ChoixTireur[0][0]+29
                        Ylaser=ChoixTireur[0][1]+60

                        laserEnnemi.append(game.create_rectangle(Xlaser,Ylaser,Xlaser+2,Ylaser+40,fill='orange'))

                elif Choix==2:
                    if Nb_Ennemis[2]!=0:

                        ChoixTireur=[]
                        ChoixTireur.append([liste_coordennemis[2][randrange(0,Nb_Ennemis[2],1)][0],liste_coordennemis[2][randrange(0,Nb_Ennemis[2],1)][1]])
                        Xlaser=ChoixTireur[0][0]+29
                        Ylaser=ChoixTireur[0][1]+60


                        laserEnnemi.append(game.create_rectangle(Xlaser,Ylaser,Xlaser+2,Ylaser+40,fill='orange'))

                elif Choix==3:
                    if Nb_Ennemis[3]!=0:

                        ChoixTireur=[]
                        ChoixTireur.append([liste_coordennemis[3][randrange(0,Nb_Ennemis[3],1)][0],liste_coordennemis[3][randrange(0,Nb_Ennemis[3],1)][1]])
                        Xlaser=ChoixTireur[0][0]+29
                        Ylaser=ChoixTireur[0][1]+60


                        laserEnnemi.append(game.create_rectangle(Xlaser,Ylaser,Xlaser+2,Ylaser+40,fill='orange'))

                elif Choix==4:
                    if Nb_Ennemis[4]!=0:

                        ChoixTireur=[]
                        ChoixTireur.append([liste_coordennemis[4][randrange(0,Nb_Ennemis[4],1)][0],liste_coordennemis[4][randrange(0,Nb_Ennemis[4],1)][1]])
                        Xlaser=ChoixTireur[0][0]+29
                        Ylaser=ChoixTireur[0][1]+60


                        laserEnnemi.append(game.create_rectangle(Xlaser,Ylaser,Xlaser+2,Ylaser+40,fill='orange'))

                AnimationlaserEnnemi()

def AnimationlaserEnnemi():
    global xe,ye,dylaserEnnemi,Ylaser,Xlaser,laserEnnemi,feu_ennemi,col_vaisseau1,col_vaisseau2
    global projectile,DebutJeu,Score,vie
    if feu_ennemi==1:
        Ylaser=Ylaser+dylaserEnnemi
        abri()

        if Ylaser>=775:
            if len(laserEnnemi)==1:
                    game.delete(laserEnnemi[0])
            feu_ennemi=0

        # ce code permet de tuer le joueur si par inadvertance il se prend un laser

        elif col_vaisseau1.x<=Xlaser<=col_vaisseau2.x and Ylaser>=col_vaisseau1.y:
            game.delete(vaisseau[0])
            game.delete(vaisseau[1])
            game.delete(vaisseau[2])
            game.delete(vaisseau[3])
            if len(projectile)!=0:
                game.delete(projectile[0])
            if len(laserEnnemi)!=0:
                game.delete(laserEnnemi[0])
            xlaser,ylaser=0,0
            feu_ennemi=0

            # il faut ensuite diminuer la vie du joueur

            vie=vie-1
            calculateur_vie()

            # Si le nombre de vie est non nul vaisseau = Jésus 2 The return

            if vie>0:
                home.after(500,dessine_vaisseau)

        if len(laserEnnemi)==1:
            game.coords(laserEnnemi[0],Xlaser,Ylaser,Xlaser+2,Ylaser+40)
        game.after(100,AnimationlaserEnnemi)

def Creation_Abris():     # il y a bien sur des bouclier à définir
    global ListeAbris,CoordonneesBriques

    ListeAbris=[]
    CoordonneesBriques=[]

    i=0

    x=50
    y=600

    while i<4:
        limX=x+120
        limY=y+60
        departx=x
        while y<limY:
            while x<limX:
                ListeAbris.append(game.create_rectangle(x,y,x+20,y+20,fill='green',width=0))
                CoordonneesBriques.append([x,y])
                x+=20
            x=departx
            y+=20
        i+=1
        x+=206
        y-=60

def abri():
    global CoordonneesBriques,ListeAbris,xtir,ytir,feu,Xlaser,Ylaser,feu_ennemi,laserEnnemi,projectile
    i=0
    t=0
    while i<len(CoordonneesBriques):
        x=CoordonneesBriques[i][t]
        y=CoordonneesBriques[i][t+1]

        # Si le joueur tire sur l'une des briques
        # composant les abris celle-ci est d�truite

        if xtir>=x and xtir<=x+20 and ytir<=y+20 :
            xtir,ytir=0,0
            game.delete(ListeAbris[i])
            game.delete(projectile[0])
            feu=0
            del CoordonneesBriques[i]
            del ListeAbris[i]
        t=0
        i+=1
    i=0
    t=0
    if feu_ennemi==1:
        while i<len(CoordonneesBriques):
            x=CoordonneesBriques[i][t]
            y=CoordonneesBriques[i][t+1]

            # Si l'ennemi tire sur l'une des briques
            # composant les abris celle-ci est
            # �galement d�truite

            if Xlaser>=x>=Xlaser-20 and Ylaser>=y-10:
                xlaser,ylaser=0,0
                game.delete(ListeAbris[i])
                if len(laserEnnemi)==1:
                    game.delete(laserEnnemi[0])
                laserEnnemi=[]
                feu_ennemi=0
                del CoordonneesBriques[i]
                del ListeAbris[i]
            t=0
            i+=1





## ##  ## ##
### game ###
## ##  ## ##

def menu():
    global home,feu,game,Stat,START
    home=Tk()
    home.geometry("1200x840")
    home.title("game Space invaders")
    home.iconphoto(True, PhotoImage(file="..\\Space Invaders Python\\start.png"))
    game=Canvas(home,bg="black",width=840,height=840)
    game.grid()
    Stat=Canvas(home,bg="black",width=360,height=840)
    Stat.grid(column=841,row=0)
    home.after(1000,titre)
    START=PhotoImage(file="..\\Space Invaders Python\\start.png")


    game.bind_all("<Right>",right)
    game.bind_all("<d>",right)
    game.bind_all("<Left>",left)
    game.bind_all("<q>",left)
    game.bind_all("<space>",chargement_laser)
    game.bind_all("<Escape>",retour_menu)
    home.mainloop()

def retour_menu(e):
    global lancement
    lancement=0
    game.delete(ALL)
    Stat.delete(ALL)
    titre()

def titre():
    P=POINT(420,350)
    texte(game,P,"Space invaders",("fixedsys",50,"underline","bold"),"#710000","#710000") #fixedsys est la premier police par defaut du bloc note
    home.after(1000,créateur)

def créateur():
    P=POINT(420,450)
    texte(game,P,"Créer par Phantom",("fixedsys",20),"white","white")
    home.after(1000,reste)

def reste():
    with open("..\\Space Invaders Python\\HighScore.txt","r",encoding="utf-8") as Hg:
        Score=Hg.readline()
        Score="The HighScore is equale to "+Score
        P=POINT(175,700)
        texte(game,P,Score,("fixedsys",15,"underline"),"white","white")
    home.after(1000,start_button)

def start_button():
        P=POINT(420,575)
        image(game,P,START)
        home.bind_all('<Button-1>',new_score)

def new_score(e):
    global Score,vie
    Score=0
    score()
    vie=3
    calculateur_vie()
    P=POINT(e.x,e.y)
    Starter(P)

def Starter(P):
    global lancement,feu,nb_ennemis,luck,Score,col_mob_bonus1,col_mob_bonus2,PasAvancement,v_ennemies,vie,feu_ennemi,dylaserEnnemi,ChoixTireur,Xlaser,Ylaser,xtir,ytir,liste_ennemis,liste_coordennemis,Nb_Ennemis,RangEnnemiChoisi,EnnemiChoisi,xe,ye,xe2,ye2,xe3,ye3,xe4,ye4,xe5,ye5,laserEnnemi,ListeAbris,CoordonneesBriques
    if 250<P.x<550 and 515<P.y<635:
        lancement=1
        game.delete(ALL)
        for i in range(0,209):
            for j in range(0,209):
                a=randint(0,250)
                if a==13:
                    P=POINT(i*4,j*4)
                    c_Px(game,P,"white")
        dessine_vaisseau()
        indiq_command()
        xtir=pos_canon2.x
        ytir=pos_canon2.y-4
        laserEnnemi=[]
        ListeAbris=[]
        CoordonneesBriques=[]
        Creation_Abris()
        luck=0
        feu=0
        PasAvancement=0
        v_ennemies=1
        col_mob_bonus1=POINT(0,0)
        col_mob_bonus2=POINT(0,0)
        dylaserEnnemi=10
        ennemis_e1=[]
        ennemis_e2=[]
        ennemis_e3=[]
        ennemis_e4=[]
        ennemis_e5=[]
        liste_ennemis=[ennemis_e1,ennemis_e2,ennemis_e3,ennemis_e4,ennemis_e5]

        coordennemis_e1=[]
        coordennemis_e2=[]
        coordennemis_e3=[]
        coordennemis_e4=[]
        coordennemis_e5=[]
        liste_coordennemis=[coordennemis_e1,coordennemis_e2,coordennemis_e3,coordennemis_e4,coordennemis_e5]

        Nb_Ennemise1=11
        Nb_Ennemise2=11
        Nb_Ennemise3=11
        Nb_Ennemise4=11
        Nb_Ennemise5=11
        PasAvancement=0
        Nb_Ennemis=[Nb_Ennemise1,Nb_Ennemise2,Nb_Ennemise3,Nb_Ennemise4,Nb_Ennemise5]

        RangEnnemiChoisi=randrange(0,5,1)

        Ennemi1Choisi=randrange(0,Nb_Ennemis[0],1)
        Ennemi2Choisi=randrange(0,Nb_Ennemis[1],1)
        Ennemi3Choisi=randrange(0,Nb_Ennemis[2],1)
        Ennemi4Choisi=randrange(0,Nb_Ennemis[3],1)
        Ennemi5Choisi=randrange(0,Nb_Ennemis[4],1)

        EnnemiChoisi=[Ennemi1Choisi,Ennemi2Choisi,Ennemi3Choisi,Ennemi4Choisi,Ennemi5Choisi]

        xe,ye,xe2,ye2,xe3,ye3,xe4,ye4,xe5,ye5=96,400,96,350,94,300,94,250,88,200

        launch_Bonus()
        nb_ennemis=0
        nb_ennemis=54
        v=0
        while v<11:
            dessine_mob_10()
            dessine_mob_10_2()
            dessine_mob_20_1()
            dessine_mob_20_2()
            dessine_mob_30_1()
            v+=1
        ChoixTireur=[]
        ChoixTireur.append([liste_coordennemis[0][randrange(0,Nb_Ennemis[0],1)][0],liste_coordennemis[0][randrange(0,Nb_Ennemis[0],1)][1]])
        Xlaser=ChoixTireur[0][0]+9
        Ylaser=ChoixTireur[0][1]+40
        feu_ennemi=0
        ennemis()

def indiq_command():
    P=POINT(180,200)
    texte(Stat,P,"Flèche Droite/D = Mouvement vers la droite",("fixedsys",10),"white","white")
    P=POINT(180,220)
    texte(Stat,P,"Flèche Gauche/Q = Mouvement vers la gauche",("fixedsys",10),"white","white")
    P=POINT(180,240)
    texte(Stat,P,"Barre d'espacement = Tirer un laser",("fixedsys",10),"white","white")
    P=POINT(180,260)
    texte(Stat,P,"Touche Échap = Retour au menu",("fixedsys",10),"white","white")

def open_HighScore():
    with open("E:\python\Space Invaders Python\HighScore.txt",'r') as Hs:
        return Hs.readline()

def new_HighScore(Score):
    a=int(open_HighScore())
    if Score>a:
        with open("E:\python\Space Invaders Python\HighScore.txt",'w') as Nrecord:
            Score=str(Score)
            Nrecord.write(Score)

#Il faut définir si le jeu est lançée ou non
global lancement
lancement=0

def calculateur_vie():
    global vie,lancement
    if vie==3:
        vies()
    if vie==2:
        Stat.delete(vie_1[0])
        Stat.delete(vie_1[1])
        Stat.delete(vie_1[2])
        Stat.delete(vie_1[3])
    elif vie==1:
        Stat.delete(vie_2[0])
        Stat.delete(vie_2[1])
        Stat.delete(vie_2[2])
        Stat.delete(vie_2[3])
    if vie==0:
        lancement=0
        Stat.delete(vie_3[0])
        Stat.delete(vie_3[1])
        Stat.delete(vie_3[2])
        Stat.delete(vie_3[3])
        new_HighScore(Score)
        game.create_text(420,400,font=('Fixedsys',30),text="Game Over",fill='red')
        game.create_text(420,420,font=('Fixedsys',15),text=Score,fill='red')
        game.create_text(420,520,font=('Fixedsys',20),text="Pressez Echap pour retourner au menu",fill='gray')


def score():
    global Your_Score,Stat
    Txt_Sc="Score : 0"
    Your_Score=[]
    Your_Score.append(Stat.create_text(180,15,fill="white",text=Txt_Sc,font=("fixedsys",15)))

def MaJ_Score(point_win):
    global Score,Your_Score,Stat,nb_ennemis
    Score=Score+point_win
    act_Score=str(Score)
    Txt_Sc="Score : "+act_Score
    Stat.delete(Your_Score)
    Your_Score=[]
    Your_Score.append(Stat.create_text(180,15,fill="white",text=Txt_Sc,font=("fixedsys",15)))
    if nb_ennemis==0:
        P=POINT(300,600)
        Starter(P)

def vies():
    global vie_1,vie_2,vie_3
    vie_1=[]
    pos_vaisseau=POINT(180,675)
    vie_1.append(Stat.create_rectangle(pos_vaisseau.x-22,pos_vaisseau.y+6,pos_vaisseau.x+22,pos_vaisseau.y+14,fill='green',outline="green"))
    vie_1.append(Stat.create_rectangle(pos_vaisseau.x-18,pos_vaisseau.y+2,pos_vaisseau.x+18,pos_vaisseau.y+6,fill='green',outline="green"))
    vie_1.append(Stat.create_rectangle(pos_vaisseau.x-6,pos_vaisseau.y-6,pos_vaisseau.x+6,pos_vaisseau.y+2,fill='green',outline="green"))
    vie_1.append(Stat.create_rectangle(pos_vaisseau.x-2,pos_vaisseau.y-10,pos_vaisseau.x+2,pos_vaisseau.y-6,fill='green',outline="green"))
    vie_2=[]
    pos_vaisseau=POINT(180,725)
    vie_2.append(Stat.create_rectangle(pos_vaisseau.x-22,pos_vaisseau.y+6,pos_vaisseau.x+22,pos_vaisseau.y+14,fill='green',outline="green"))
    vie_2.append(Stat.create_rectangle(pos_vaisseau.x-18,pos_vaisseau.y+2,pos_vaisseau.x+18,pos_vaisseau.y+6,fill='green',outline="green"))
    vie_2.append(Stat.create_rectangle(pos_vaisseau.x-6,pos_vaisseau.y-6,pos_vaisseau.x+6,pos_vaisseau.y+2,fill='green',outline="green"))
    vie_2.append(Stat.create_rectangle(pos_vaisseau.x-2,pos_vaisseau.y-10,pos_vaisseau.x+2,pos_vaisseau.y-6,fill='green',outline="green"))
    vie_3=[]
    pos_vaisseau=POINT(180,775)
    vie_3.append(Stat.create_rectangle(pos_vaisseau.x-22,pos_vaisseau.y+6,pos_vaisseau.x+22,pos_vaisseau.y+14,fill='green',outline="green"))
    vie_3.append(Stat.create_rectangle(pos_vaisseau.x-18,pos_vaisseau.y+2,pos_vaisseau.x+18,pos_vaisseau.y+6,fill='green',outline="green"))
    vie_3.append(Stat.create_rectangle(pos_vaisseau.x-6,pos_vaisseau.y-6,pos_vaisseau.x+6,pos_vaisseau.y+2,fill='green',outline="green"))
    vie_3.append(Stat.create_rectangle(pos_vaisseau.x-2,pos_vaisseau.y-10,pos_vaisseau.x+2,pos_vaisseau.y-6,fill='green',outline="green"))

menu()