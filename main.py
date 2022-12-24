def mainmenu():
    print("1 Make a player\n2 Choose a player\n3 Initialize a game\n4 Choose a game\n5 Play a game\n6 Play automated\n7 Exit")

def blackjackmenu():
    print("1 Hit\n2 Stand\n3 Double down\n4 Surrender\n5 Check odds")

def blackjackmenu2():
    print("1 Hit\n2 Stand")


class Player:
    def __init__(self, name='default', money=89000):
        self.name = name
        self.money = int(money)
    
    def __str__(self):
        return f'{self.name} {self.money}'


class Game:
    def __init__(self, name='defaultgame', num_decks=8, standardbet=10):
        self.suits = ['C','D','H','S']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cardlist = []
        for k in range(num_decks):
            for i in self.suits:
                for j in self.values:
                    self.cardlist.append((j,i))

        self.name = name
        self.standardbet = standardbet

    def rungame(self, player, automated = False):
        pass

    def __str__(self):
        return f'{self.name} {self.standardbet}'


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
            player_list.append(Player(name, money))

        # Choose a player
        elif n == 2:
            list_idx = 1
            for p in sorted(player_list, key = lambda x:x.name):
                 print(list_idx, p)
                 list_idx += 1

        # Initialize a game
        elif n == 3:
            name, num_decks, standardbet = input().split(',')
            num_decks, standardbet = int(num_decks), int(standardbet)
            game_list.append(Game(name, num_decks, standardbet))

        # Choose a game
        elif n == 4:
            list_idx = 1
            for g in sorted(game_list, key = lambda x:x.name):
                 print(list_idx, g)
                 list_idx += 1

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

