from tkinter import *

#Interface graphique du jeu CasinoPy en cours de développement, .pyw pour qu'aucun terminal ne se lance en même temps (normalement :)

#je crée la fenêtre
window = Tk()

#je définis ma fonction blackjack qui va ouvrir une nouvelle page afin de lancer une partie de blackjack
def blackjack():
    #un ensemble de variables que j'ai besoin d'être globale pour pouvoir avoir leur accès dans d'autres fonctions
    global frame1
    global build
    global usernameinput
    global moneyinput
    global colorinput
    #Personnaliser la page
    window.config(background='#310E35')
    window.title("CasinoPy - Create a party")
    frame.destroy()
    frame.pack_forget()
    window.update()
    
    #Créer les frames de la page
    frame1 = Frame(window, bg="#310E35")
    build = Frame(window, bg="#310E35")

    #Menu de navigation de la page avec des boutons
    buttonhome = Button(frame1, text="Home", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(homeclearfirst)   ).grid(padx=5, pady=10, row=0, column=0)
    label_title = Label(frame1, text="CasinoPy", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=0, column=1)
    buttonplus = Button(frame1, text="About", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(aboutclearfirst)).grid(padx=5, pady=10, row=0, column=2)
    
    #Contenu de la page
    title = Label(build, text="Create a blackjack party :", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=2)
    username = Label(build, text="Username :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=1, column=1, pady=10)
    #input
    usernameinput = Entry(build)
    usernameinput.grid(row=1, column=2, pady=5)
    money = Label(build, text="Money :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)
    #input
    moneyinput = Entry(build)
    moneyinput.grid(row=2, column=2, pady=5)
    color = Label(build, text="color :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=3, column=1, pady=10)
    #input
    colorinput = Entry(build)
    colorinput.grid(row=3, column=2, pady=5)
    #button pour éxecuter la foction pushbj dans command=()
    pushbutton = Button(build, text="Confirm", command=(pushbj)).grid(row=4, column=2)
    build.pack(expand=YES)
    frame1.pack()
    window.mainloop()

#je définis ma fonction dice qui va ouvrir une nouvelle page afin de lancer une partie de dice
def dice():
    #un ensemble de variables que j'ai besoin d'être globale pour pouvoir avoir leur accès dans d'autres fonctions
    global frame1
    global build
    global usernameinput2
    global moneyinput2
    global colorinput2
    window.config(background='#310E35')
    window.title("CasinoPy - Create a party")
    frame.destroy()
    frame.pack_forget()
    window.update()
    
    frame1 = Frame(window, bg="#310E35")
    build = Frame(window, bg="#310E35")

    buttonhome = Button(frame1, text="Home", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(homeclearfirst)   ).grid(padx=5, pady=10, row=0, column=0)
    label_title = Label(frame1, text="CasinoPy", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=0, column=1)
    buttonplus = Button(frame1, text="About", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(aboutclearfirst)).grid(padx=5, pady=10, row=0, column=2)
    
    #Contenu de la page
    title = Label(build, text="Create a dice party :", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=2)
    username2 = Label(build, text="Username :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=1, column=1, pady=10)
    #input
    usernameinput2 = Entry(build)
    usernameinput2.grid(row=1, column=2, pady=5)
    money2 = Label(build, text="Money :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)
    #input
    moneyinput2 = Entry(build)
    moneyinput2.grid(row=2, column=2, pady=5)
    color2 = Label(build, text="color :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=3, column=1, pady=10)
    #input
    colorinput2 = Entry(build)
    colorinput2.grid(row=3, column=2, pady=5)
    #button pour aller sur la fonction pushdice dans command=()
    pushbutton = Button(build, text="Confirm", command=(pushdice)).grid(row=4, column=2)
    build.pack(expand=YES)
    frame1.pack()
    window.mainloop()

def homeclearfirst():
    #Afin d'éffacer le contenu des précedentes variables qu'affiche tkinter, je dois passer par une première fonction comme celle ci qui efface les frames précedentes et renvoi sur la fonction home()
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update()
    home()

def aboutclearfirst():
    #Afin d'éffacer le contenu des précedentes variables qu'affiche tkinter, je dois passer par une première fonction comme celle ci qui efface les frames précedentes et renvoi sur la fonction about()
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update()
    about()

def pushbj():
    #un ensemble de variables que j'ai besoin d'être globale pour pouvoir avoir leur accès dans d'autres fonctions
    global usernameinput
    global moneyinput
    global colorinput
    global frame3
    global build1
    global timeentry
    #Je récupère les valeurs des input avec le nom du joueur, son argent, sa couleur
    usernameblackjack = usernameinput.get()
    moneyblackjack = moneyinput.get()
    colorblackjack = colorinput.get()
    #Vérification assez faible mais sur laquelle je ne m'attarde pas pour l'instant pour vérifier que les input sont correctement remplis
    if len(usernameblackjack) == 0:
        return
    if len(moneyblackjack) == 0:
        return
    if len(colorblackjack) == 0:
        return
    #Personaliser la fenêtre
    window.config(background='#310E35')
    window.title("CasinoPy")
    #Supprimer les frames dont je n'ai pas besoin pour éviter les conflits de contenu
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update()

    #créer deux nouvelles frames pour le contenu de la page de cette fonction
    frame3 = Frame(window, bg="#310E35")
    build1 = Frame(window, bg="#310E35")

    timelabel = Label(build1, text="New game :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)
    timeentry = Entry(build1)
    timeentry.grid(row=2, column=2, pady=5)
    pushbutton = Button(build1, text="Confirm", command=()).grid(row=4, column=2)

    buttonhome = Button(frame3, text="Home", font=("Courrier, 15"), bg='white', fg="#A200FF", command=()).grid(padx=5, pady=10, row=0, column=0)
    label_title = Label(frame3, text="CasinoPy", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=0, column=1)
    buttonplus = Button(frame3, text="About", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(aboutclearfirst)).grid(padx=5, pady=10, row=0, column=2)

def pushdice():
    #un ensemble de variables que j'ai besoin d'être globale pour pouvoir avoir leur accès dans d'autres fonctions
    global usernameinput2
    global moneyinput2
    global colorinput2
    global frame3
    global build1
    global timeentry
    #Je récupère les valeurs des input avec le nom du joueur, son argent, sa couleur
    usernamedice = usernameinput2.get()
    moneydice = moneyinput2.get()
    colordice = colorinput2.get()
    #Vérification assez faible mais sur laquelle je ne m'attarde pas pour l'instant pour vérifier que les input sont correctement remplis
    if len(usernamedice) == 0:
        return
    if len(moneydice) == 0:
        return
    if len(colordice) == 0:
        return
    #Personaliser la fenêtre
    window.config(background='#310E35')
    window.title("CasinoPy")
    #Supprimer les frames dont je n'ai pas besoin pour éviter les conflits de contenu
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update()

    #créer deux nouvelles frames pour le contenu de la page de cette fonction
    frame3 = Frame(window, bg="#310E35")
    build1 = Frame(window, bg="#310E35")

    #contenu de la page
    timelabel = Label(build1, text="Temps entre chaque screenshot :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)
    timeentry = Entry(build1)
    timeentry.grid(row=2, column=2, pady=5)
    pushbutton = Button(build1, text="Confirm", command=()).grid(row=4, column=2)

    #bouton d'un petit menu de navigation
    buttonhome = Button(frame3, text="Home", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(homeclearfirst)).grid(padx=5, pady=10, row=0, column=0)
    label_title = Label(frame3, text="CasinoPy", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=0, column=1)
    buttonplus = Button(frame3, text="About", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(aboutclearfirst)).grid(padx=5, pady=10, row=0, column=2)

def home():
    #fonction que j'ai besoin de mettre en global pour pouvoir avoir son accès dans d'autres fonctions
    global frame
    #personnaliser cette fenêtre
    window.title("CasinoPy - Home")
    window.geometry("720x480")
    window.minsize(480, 360)
    window.maxsize(1920, 1080)
    window.config(background='#310E35')
    
    #créer la frame
    frame = Frame(window, bg='#310E35')
    frame2 = Frame(frame, bg="#310E35")
    
    #ajouter un texte
    label_title = Label(frame, text="CasinoPy", font=("Courrier", 30), bg='#310E35', fg="white")
    label_title.pack(expand=YES)
    label_subtitle = Label(frame, text="A simple casino game with different modes such as Blackjack and Dice.", font=("Courrier", 20), bg='#310E35', fg="white")
    label_subtitle.pack(expand=YES)
    label_test = Label(frame2, text="       ", fg="#310E35", bg="#310E35").grid(row=0, column=1)
    
    #bouton d'un petit menu de navigation
    bouton = Button(frame2, text="Blackjack", font=("Courrier", 20), bg='white', fg="#A200FF", command=(blackjack)).grid(row=1, column=0)
    about = Button(frame2, text="Dice", font=("Courrier", 20), bg='white', fg="#A200FF", command=(dice)).grid(row=1, column=2)
    
    #ajouter frame
    frame.pack(expand=YES)
    frame2.pack(expand=YES)
    #afficher
    window.mainloop()

def about():
    #fonction que j'ai besoin de mettre en global pour pouvoir avoir son accès dans d'autres fonctions
    global frame
    window.title("CasinoPy - About")
    window.geometry("720x480")
    window.minsize(480, 360)
    window.maxsize(1920, 1080)
    window.config(background='#310E35')
    
    #créer la frame
    frame = Frame(window, bg='#310E35')
    frame2 = Frame(frame, bg="#310E35")
    
    #Ajouter le contenu de la page
    label_title = Label(frame, text="CasinoPy", font=("Courrier", 30), bg='#310E35', fg="white")
    label_title.pack(expand=YES)
    label_subtitle = Label(frame, text="A simple casino game created by @loutchoo.", font=("Courrier", 20), bg='#310E35', fg="white")
    label_subtitle.pack(expand=YES)
    label_subtitle2 = Label(frame, text="https://github.com/loutchoo !", font=("Courrier", 20), bg='#310E35', fg="white")
    label_subtitle2.pack(expand=YES)
    label_test = Label(frame2, text="       ", fg="#310E35", bg="#310E35").grid(row=0, column=1)
    
    #Ajouter un petit menu de navigation
    bj = Button(frame2, text="Blackjack", font=("Courrier", 20), bg='white', fg="#A200FF", command=(blackjack)).grid(row=1, column=0)

    dice = Button(frame2, text="Dice", font=("Courrier", 20), bg='white', fg="#A200FF", command=(dice)).grid(row=1, column=2)
    
    #ajouter frame
    frame.pack(expand=YES)
    frame2.pack(expand=YES)
    #afficher la fenêtre
    window.mainloop()

#démarrage le programme
home()