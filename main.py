def mainmenu():
    print("1 Make a player\n2 Choose a player\n3 Initialize a game\n4 Choose a game\n5 Play a game\n6 Play automated\n7 Exit")

def blackjackmenu():
    print("1 Hit\n2 Stand\n3 Double down\n4 Surrender\n5 Check odds")

def blackjackmenu2():
    print("1 Hit\n2 Stand")


class Player:
    def __init__(self, name, money, strategy):
        self.name = name
        self.money = int(money)


class Game:
    def __init__(self, name, num_decks, standardbet):
        self.suits = ['C','D','H','S']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cardlist = []
        for k in range(num_decks):
            for i in self.suits:
                for j in self.values:
                    self.cardlist.append((j,i))

    def rungame(self, player, automated = False):
        pass


if __name__ == '__main__':
    mainmenu()
    n = int(input())

    player_list = []
    game_list = []
    while n != 7:
        # Make a player
        if n == 1:
            name, money = input().split(',')
            money = int(money)

            # process new player
            player_list.append(Player(name, money))

        # Choose a player
        elif n == 2:
            pass
        # Initialize a game
        elif n == 3:
            name, num_decks, standardbet = input().split(',')
            num_decks, standardbet = int(num_decks), int(standardbet)
            
            # process new game
            game_list.append(Game(name, num_decks, standardbet))
            
        # Choose a game
        elif n == 4:
            pass
        # Play a game
        elif n == 5:
            pass
        # Play automated
        elif n == 6:
            pass
        # Exit
        elif n == 7:
            exit
        
        mainmenu()
        n = int(input())

