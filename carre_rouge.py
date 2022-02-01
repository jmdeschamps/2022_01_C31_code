from tkinter import *
import time

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.modele=self.parent.modele
        self.root=Tk()
        self.root.title("Carre Rouge, alpha_0.1")
        self.cadres=self.creer_interface()

    def creer_interface(self):
        # cadre HUD affichant la duree
        self.cadre_info=Frame(self.root, bg="lightgreen")
        self.var_duree=StringVar()
        label_duree=Label(self.cadre_info,text="0",textvariable=self.var_duree)
        label_duree.pack()
        # le canevas de jeu
        self.canevas=Canvas(self.root,width=self.modele.largeur,height=self.modele.hauteur,bg="white")
        self.canevas.tag_bind("pion","<Button>",self.debuter_partie)
        # visualiser
        self.cadre_info.pack(expand=1,fill=X)
        self.canevas.pack()


        self.afficher_partie()

    def debuter_partie(self,evt):
        self.canevas.tag_unbind("pion","<Button>")
        self.canevas.bind("<B1-Motion>",self.recibler_pion)
        self.canevas.bind("<ButtonRelease>",self.arreter_jeu)
        self.parent.debuter_partie()

    def arreter_jeu(self,evt):
        self.parent.partie_en_cours=0
        self.canevas.tag_bind("pion","<Button>",self.debuter_partie)
        self.canevas.unbind("<B1-Motion>")
        self.canevas.unbind("<ButtonRelease>")

    def recibler_pion(self,evt):
        x=evt.x
        y=evt.y
        self.parent.recibler_pion(x,y)

    def afficher_partie(self):
        self.canevas.delete(ALL)
        x=self.modele.pion.x
        y=self.modele.pion.y
        d=self.modele.pion.demitaille
        self.canevas.create_rectangle(x-d,y-d,x+d,y+d,
                                      fill="red",tags=("pion",))

        x=self.modele.poteau.x
        y=self.modele.poteau.y
        d=self.modele.poteau.demitaille
        self.canevas.create_rectangle(x-d,y-d,x+d,y+d,
                                      fill="black",tags=("poteau",))

        self.var_duree.set(str(round(self.modele.duree,2)))

class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.largeur=400
        self.hauteur=400
        self.debut=None
        self.duree=0
        self.pion=Pion(self)
        self.poteau=Poteau(self)

    def recibler_pion(self,x,y):
        self.pion.recibler(x,y)

    def jouer_tour(self):
        self.duree=time.time()-self.debut

class Poteau():
    def __init__(self,parent):
        self.parent=parent
        self.x=100
        self.y=100
        self.demitaille=3

class Pion():
    def __init__(self,parent):
        self.parent=parent
        self.x=self.parent.largeur/2
        self.y=self.parent.largeur/2
        self.demitaille=10

    def recibler(self,x,y):
        self.x=x
        self.y=y

class Controleur():
    def __init__(self):
        self.partie_en_cours=0
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()

    def recibler_pion(self,x,y):
        self.modele.recibler_pion(x,y)

    def debuter_partie(self):
        self.modele.debut=time.time()
        self.partie_en_cours=1
        self.jouer_partie()

    def jouer_partie(self):
        if self.partie_en_cours:
            self.modele.jouer_tour()
            self.vue.afficher_partie()
            self.vue.root.after(50,self.jouer_partie)

if __name__ == '__main__':
    c=Controleur()
    print("L'application se termine")


