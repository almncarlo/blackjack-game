def mainmenu():
    print("1 Make a player\n2 Choose a player\n3 Initialize a game\n4 Choose a game\n5 Play a game\n6 Play automated\n7 Exit")

def blackjackmenu():
    print("1 Hit\n2 Stand\n3 Double down\n4 Surrender\n5 Check odds")

def blackjackmenu2():
    print("1 Hit\n2 Stand")


class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
    
    def __str__(self):
        return f'{self.name} {self.money}'


class Game:
    def __init__(self, name, num_decks, standardbet):
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
        dealer_cards = [self.cardlist[0], self.cardlist[2]]
        player_cards = [self.cardlist[1], self.cardlist[3]]
        
        strDealer = '-'.join(dealer_cards[0])
        strPlayer = ','.join([f'{x}-{y}' for (x,y) in player_cards])

        print(f'Dealer: {strDealer},?-?\nPlayer: {strPlayer}')

        n = int(input())

        if n == 1:
            print('Hit')
            # player takes additional card
            blackjackmenu2()
            # if additional hand causes player to bust, proceed to scoring
        elif n == 2:
            print('Stand')
        elif n == 3:
            print('Double down')
        elif n == 4:
            print('Surrender')
        else:
            print('Check odds')
            print(f'Odds that hand value will still be 21 or below: /')

    def __str__(self):
        return f'{self.name} {self.standardbet}'


if __name__ == '__main__':
    # given code snippet
    cards = input().split(',')
    newcardlist = []
    for card in cards:
        fv = card.split('-')
        newcardlist.append((fv[0],fv[1]))

    player_list = []
    game_list = []
    selected_player = None
    selected_game = None

    # initialize default player and game
    default_p = Player('default', 89000)
    default_g = Game('defaultgame', 8, 10)
    default_g.cardlist = newcardlist.copy()
    player_list.append(default_p)
    game_list.append(default_g)

    mainmenu()
    n = int(input())

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
            
            idx_select = int(input())
            selected_player = sorted(player_list, key = lambda x:x.name)[idx_select - 1]
            print(selected_player)

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
            
            idx_select = int(input())
            selected_game = sorted(game_list, key = lambda x:x.name)[idx_select - 1]
            print(selected_game)

        # Play a game
        elif n == 5:
            blackjackmenu()
            selected_game.rungame(selected_player)

        # Play automated
        elif n == 6:
            blackjackmenu()
            selected_game.rungame(selected_player, True)

        # Exit
        elif n == 7:
            exit
        
        mainmenu()
        n = int(input())

