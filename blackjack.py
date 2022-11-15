import random
import time

#Le code de blackjack qui va prochainent être ajouté à mon interface graphique tkinter

#Je définis toutes les cartes
suits = ("Piques ♠", "Trèfles ♣", "Coeurs ♥", "Carreaux ♦")
ranks = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
#Je définis la valeur de chacunes de ces cartes
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

playing = True

#Je définis mes classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " de " + self.suit

#Je définis mes classes
class Deck:
    def __init__(self):
        self.deck = []  #Commence avec une liste vide
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""  #Crée une variable vide
        for card in self.deck:
            deck_comp += "\n " + card.__str__()
        return "Le deck a:" + deck_comp

    def shuffle(self):
        #Mélanger les cartes
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Je définis mes classes
class Main: 
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "A":
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#L'ensemble des fonctions définies
def hit(deck, main):
    #Fonction hit pour ajouter une carte au deck
    main.add_card(deck.deal())
    main.adjust_for_ace()


def hit_or_stand(deck, main):
    global playing

    while True:
        x = input("\nSouhaiterais tu tirer ou rester ? Entres [t/r] ")

        if x[0].lower() == "t":
            hit(deck, main)  #on utilise la fonction hit définit juste au dessus pour tirer une nouvelle carte

        elif x[0].lower() == "r":
            print("Le joueur reste, le dealer joue.")
            playing = False

        else:
            print("Désolé, tu t'es trompé, tires ou restes : [t/r].")
            continue
        break


def show_some(player, dealer):
    #Montre les cartes du joueur et du dealer respectivement, tout en cachant la deuxième carte du dealer
    print("\nMain du joueur :", *player.cards, sep="\n ")
    print("Main du joueur =", player.value)
    print("\nMain du dealer :")
    print(" <carte cachée>")
    print("", dealer.cards[1])


def show_all(player, dealer):
    #Montre cette fois si aussi la deuxième carte du dealer
    print("\nMain du joueur :", *player.cards, sep="\n ")
    print("Main du joueur =", player.value)
    print("\nMain du dealer:", *dealer.cards, sep="\n ")
    print("Main du dealer =", dealer.value)


def player_busts(player, dealer):
    #Fonction pour quand le joueur perd
    print("\n--- Le joueur perd ! ---")


def player_wins(player, dealer):
    #Fonction pour quand le joueur a un blackjack et donc gagnes
    print("\n--- Le joueur a un blackjack ! Tu gagnes :) ---")


def dealer_busts(player, dealer):
    #Fonction pour quand le dealer perd
    print("\n--- Le dealer perd ! Tu gagnes :) ---")


def dealer_wins(player, dealer):
    #Fonction pour quand le dealer gagne
    print("\n--- Le dealer gagne ! ---")


def push(player, dealer):
    #Fonction pour quand il y a égalité
    print("\nEgalité !")

#Partie
while True:
    print("\n----------------------------------------------------------------")
    print("                ♠♣♥♦ CasinoPy Casino ♠♣♥♦")
    print("                         Jouons !")
    print("----------------------------------------------------------------")
    print(
        "Règles:  se rapprocher autant de 21 sans le dépasser pour avoir des chances de gagner !\n\
        Le dealer tire tant qu'il n'a pas au moins 17.\n\
        Un as compte 1 si la total du joueur est >11 ou 11 si le total du joueur est <11"
    )

    #Créer le deck et le mélanger, donner une carte à chaque joueur
    deck = Deck()
    deck.shuffle()

    player_main = Main()
    player_main.add_card(deck.deal())
    player_main.add_card(deck.deal())

    dealer_main = Main()
    dealer_main.add_card(deck.deal())
    dealer_main.add_card(deck.deal())

    #Montrer les cartes
    show_some(player_main, dealer_main)

    while playing:
        hit_or_stand(deck, player_main)
        show_some(player_main, dealer_main)

        if player_main.value > 21:
            player_busts(player_main, dealer_main)
            break

    #Une fois que le joueur a stay, faire jouer le dealer
    if player_main.value <= 21:
        #Continuer de faire tirer le dealer jusqu'à ce qu'il n'est pas au moins 17 en valeur totale de ses cartes
        while dealer_main.value < 17:
            hit(deck, dealer_main)

        #Fin de la partie
        time.sleep(1)
        print("\n----------------------------------------------------------------")
        print("                     ★ Résultat final ★")
        print("----------------------------------------------------------------")

        #Montrer toutes les cartes des deux camps
        show_all(player_main, dealer_main)

        #Arrêter le jeu quand l'un des deux camps à gagné ou en cas d'égalité
        if dealer_main.value > 21:
            dealer_busts(player_main, dealer_main)

        elif dealer_main.value > player_main.value:
            dealer_wins(player_main, dealer_main)

        elif dealer_main.value < player_main.value:
            player_wins(player_main, dealer_main)

        else:
            push(player_main, dealer_main)

    #Demander au joueur si il souhaite jouer à nouveau
    nouvelle_game = input("\nJouer une autre main ? [O/N] ")
    while nouvelle_game.lower() not in ["o", "n"]:
        nouvelle_game = input("Invalide réponse. Entre oui ou non 'o' or 'n' ")
    if nouvelle_game[0].lower() == "o":
        playing = True
        continue
    else:
        print("\n------------------------Merci d'avoir joué !---------------------\n")
        break