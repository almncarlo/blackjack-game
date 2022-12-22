def mainmenu():
    print("1 Make a player\n2 Choose a player\n3 Initialize a game\n4 Choose a game\n5 Play a game\n6 Play automated\n7 Exit")

def blackjackmenu():
    print("1 Hit\n2 Stand\n3 Double down\n4 Surrender\n5 Check odds")

def blackjackmenu2():
    print("1 Hit\n2 Stand")

class Game:
    def __init__(self, name, num_decks, standardbet):
        self.suits = ['C','D','H','S']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cardlist = []
        for k in range(num_decks):
            for i in self.suits:
                for j in self.values:
                    self.cardlist.append((j,i))

if __name__ == '__main__':
    mainmenu()
    n = int(input())

    while n != 7:
        if n == 1:
            pass
        elif n == 2:
            pass
        elif n == 3:
            pass
        elif n == 4:
            pass
        elif n == 5:
            pass
        elif n == 6:
            pass
        elif n == 7:
            exit
        
        mainmenu()
        n = int(input())

