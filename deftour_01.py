from tkinter import *

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        self.root.title("Tower Defense JMD")

class Modele():
    def __init__(self,parent):
        self.parent=parent

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()

if __name__ == '__main__':
    c=Controleur()
    print("L'application se termine")