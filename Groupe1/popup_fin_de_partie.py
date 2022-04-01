from tkinter import*
import time

root = Tk()
root.geometry("800x600")
root.configure(bg = "#141414")


def pop_up_victoire():
    # On cache la fenêtre du jeu
    root.withdraw()   
    victoire_wp = Tk()
    victoire_wp.configure(bg = "#141414")
    print("victory")
    
    
    # Création d'une grille ixj invisible pour le bon placement des widgets
    def carreaux_victoire_wp():
        for i in range(31):
            victoire_wp.rowconfigure(i, weight = 1)
        for j in range(31):
            victoire_wp.columnconfigure(j, weight = 1)
            
            
    # Création des boutons dans le frame principal
    def creation_boutons_victoire_wp():
        
        
        # Modèle de bouton (similaire à une classe en objet)
        def modele_boutons_victoire_wp(i, j, text, bgcolor, fgcolor, command):
            
            
            # Fonctions liés aux binds (permet un changement de couleur du bouton et ainsi de mieux visualiser la souris sur le bouton)
            def survol(event):
                bouton_victoire_wp.config(background = bgcolor,
                                       foreground = fgcolor)
                
                
            def fin_survol(event):
                bouton_victoire_wp.config(background = fgcolor,
                                       foreground = bgcolor)
                
            
            bouton_victoire_wp = Button(victoire_wp,
                                            text = text,
                                            bg = fgcolor,
                                            fg = bgcolor,
                                            border = 0,
                                            activeforeground = fgcolor,
                                            activebackground = bgcolor,
                                            font = ("Benguiat", 15),
                                            command = command)
            
            # Attribution des intéractions utilisateurs aux fontions du seesus (survol...)
            bouton_victoire_wp.bind("<Enter>", survol)
            bouton_victoire_wp.bind("<Leave>", fin_survol)
            
            # Positionnement du bouton dans le frame principal
            bouton_victoire_wp.grid(row = i, column = j, sticky = "nsew")
        
        
        # Ici on crée des boutons à partir du modèle
        modele_boutons_victoire_wp(11, 15, "R E J O U E R", "#ffcc66", "#141414", test)
        modele_boutons_victoire_wp(13, 15, "Q U I T T E R", "#25dae9", "#141414", test2)
    
    
    def test():
        print("rejouer")
        
    def test2():
        print("quitter")
        root.deiconify()
        
        
    carreaux_victoire_wp()
    creation_boutons_victoire_wp()
    victoire_wp.mainloop()
    
    
def pop_up_defaite():
    # On cache la fenêtre du jeu
    root.withdraw()   
    
    # On crée une fenêtre de défaite
    defaite_wp = Tk()
    
    # Attribution d'une couleur à la fenêtre
    defaite_wp.configure(bg = "#141414")
    print("defeat")
    
    
    # Création d'une grille ixj invisible pour le bon placement des widgets
    def carreaux_defaite_wp():
        for i in range(31):
            defaite_wp.rowconfigure(i, weight = 1)
        for j in range(31):
            defaite_wp.columnconfigure(j, weight = 1)
            
            
    # Création des boutons dans le frame principal
    def creation_boutons_defaite_wp():
        
        
        # Modèle de bouton (similaire à une classe en objet)
        def modele_boutons_defaite_wp(i, j, text, bgcolor, fgcolor, command):
            
            
            # Fonctions liés aux binds (permet un changement de couleur du bouton et ainsi de mieux visualiser la souris sur le bouton)
            def survol(event):
                bouton_defaite_wp.config(background = bgcolor,
                                              foreground = fgcolor)
                
                
            def fin_survol(event):
                bouton_defaite_wp.config(background = fgcolor,
                                              foreground = bgcolor)
                
            
            bouton_defaite_wp = Button(defaite_wp,
                                       text = text,
                                       bg = fgcolor,
                                       fg = bgcolor,
                                       border = 0,
                                       activeforeground = fgcolor,
                                       activebackground = bgcolor,
                                       font = ("Benguiat", 15),
                                       command = command)
            
            # Attribution des intéractions utilisateurs aux fontions du seesus (survol...)
            bouton_defaite_wp.bind("<Enter>", survol)
            bouton_defaite_wp.bind("<Leave>", fin_survol)
            
            # Positionnement du bouton dans le frame principal
            bouton_defaite_wp.grid(row = i, column = j, sticky = "nsew")
        
        
        # Ici on crée des boutons à partir du modèle
        modele_boutons_defaite_wp(11, 15, "R E J O U E R", "#ffcc66", "#141414", test)
        modele_boutons_defaite_wp(13, 15, "Q U I T T E R", "#25dae9", "#141414", test2)
    
    
    def test():
        print("rejouer")
        
    def test2():
        print("quitter")
        root.deiconify()
    
    carreaux_defaite_wp()
    creation_boutons_defaite_wp()
    defaite_wp.mainloop()
    
    

b1 = Button(root, text = "Victoire", command = pop_up_victoire)
b1.pack()
b2 = Button(root, text = "Défaite", command = pop_up_defaite)
b2.pack()

root.mainloop()
