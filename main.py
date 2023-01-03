def mainmenu():
    print("1 Make a player\n2 Choose a player\n3 Initialize a game\n4 Choose a game\n5 Play a game\n6 Play automated\n7 Exit")

def blackjackmenu():
    print("1 Hit\n2 Stand\n3 Double down\n4 Surrender\n5 Check odds")

def blackjackmenu2():
    print("1 Hit\n2 Stand")


class Player:
    default_strat = {
        21:['s','s','s','s','s','s','s','s','s','s'], 20:['s','s','s','s','s','s','s','s','s','s'], 19:['s','s','s','s','s','s','s','s','s','s'],
        18:['s','s','s','s','s','s','s','s','s','s'], 17:['s','s','s','s','s','s','s','s','s','us'], 16:['s','s','s','s','s','h','h','uh','uh','uh'],
        15:['s','s','s','s','s','h','h','h','uh','uh'], 14:['s','s','s','s','s','h','h','h','h','h'], 13:['s','s','s','s','s','h','h','h','h','h'],
        12:['h','h','s','s','s','h','h','h','h','h'], 11:['dh','dh','dh','dh','dh','dh','dh','dh','dh','dh'], 10:['dh','dh','dh','dh','dh','dh','dh','dh','h','h'],
        9:['h','dh','dh','dh','dh','h','h','h','h','h'], 8:['h','h','h','h','h','h','h','h','h','h'], 7:['h','h','h','h','h','h','h','h','h','h'],
        6:['h','h','h','h','h','h','h','h','h','h'], 5:['h','h','h','h','h','h','h','h','h','h'], 4:['h','h','h','h','h','h','h','h','h','h']
    }
    def __init__(self, name, money = 89000, strategy = default_strat):
        self.name = name
        self.money = int(money)
        self.strategy = strategy
    
    def __str__(self):
        return f'{self.name} {self.money}'
    
    def addMoney(self, amount):
        self.money += int(amount)
    
    def subMoney(self, amount):
        self.money -= int(amount)

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

    def checksum(hand, single_card = False):
        sum = 0
        if single_card == False:
            for i in range(len(hand)):
                if hand[i][0] == 'A' and (sum + 11) <= 21:
                    sum += 11
                elif hand[i][0] == 'A' and (sum + 11) > 21:
                    sum += 1
                elif hand[i][0] in 'JQK':
                    sum += 10
                else:
                    sum += int(hand[i][0])
        else:
            if hand[0] == 'A' and (sum + 11) <= 21:
                sum += 11
            elif hand[0] == 'A' and (sum + 11) > 21:
                sum += 1
            elif hand[0] in 'JQK':
                sum += 10
            else:
                sum += int(hand[0])
        return sum

    def printhand(dealer_cards, player_cards, dealer_reveal = False):
        strPlayer = ','.join([f'{x}-{y}' for (x,y) in player_cards])
        if dealer_reveal == False:
            strDealer = '-'.join(dealer_cards[0])
            print(f'Dealer: {strDealer},?-?\nPlayer: {strPlayer}')
        else:
            strDealer = ','.join([f'{x}-{y}' for (x,y) in dealer_cards])
            print(f'Dealer: {strDealer}\nDealer sum: {Game.checksum(dealer_cards)}\nPlayer: {strPlayer}\nPlayer sum: {Game.checksum(player_cards)}')
    
    def scoregame(self, dealer_hand, player_hand, player, surrender = False, player_bust = False):
        print('Final Cards')
        Game.printhand(dealer_hand, player_hand, True)
        if surrender == True:
            print(f'House wins\n{player.money}')
            player.subMoney(self.standardbet / 2)
            print(player.money)
        elif player_bust == True:
            print(f'House wins\n{player.money}')
            player.subMoney(self.standardbet)
            print(player.money)
        elif Game.checksum(dealer_hand) > 21:
            print(f'Player wins\n{player.money}')
            player.addMoney(self.standardbet)
            print(player.money)
        else:
            if abs(Game.checksum(dealer_hand) - 21) < abs(Game.checksum(player_hand) - 21):
                print(f'House wins\n{player.money}')
                player.subMoney(self.standardbet)
                print(player.money)
            elif abs(Game.checksum(dealer_hand) - 21) > abs(Game.checksum(player_hand) - 21):
                print(f'Player wins\n{player.money}')
                player.addMoney(self.standardbet)
                print(player.money)
            else:
                print('Tie\nNo effect on money')

    def rungame(self, player, automated = False):
        dealer_cards, player_cards = [self.cardlist[0], self.cardlist[2]], [self.cardlist[1], self.cardlist[3]]
        del self.cardlist[0:4]

        def getinput(first_pick = False, prev_n = None):
            strat = player.strategy[Game.checksum(player_cards)][Game.checksum(dealer_cards[0], True) - 2]
            if automated == True and first_pick == True:
                if strat == 'h': n = 1
                elif strat == 's': n = 2
                elif strat == 'dh': n = 3
                elif strat == 'uh' or strat == 'us': n = 4
            elif automated == True and first_pick == False:
                if strat == 'h': n = 1
                elif strat == 's': n = 2
                elif strat == 'dh':
                    if prev_n == 1: n = 1
                    else: n = 3
                elif strat == 'uh': n = 1
                else: n = 2
            else:
                n = int(input())
            return n
        
        Game.printhand(dealer_cards, player_cards)
        blackjackmenu()
        n = getinput(True)
        pick_surrender_checkodds = True

        while Game.checksum(player_cards) < 21:
            if n == 1:
                print('Hit')
                pick_surrender_checkodds = False
                player_cards.append(self.cardlist[0])
                del self.cardlist[0]
                Game.printhand(dealer_cards, player_cards)
                if Game.checksum(player_cards) > 21:
                    print('Bust')
                    Game.scoregame(self, dealer_cards, player_cards, player, False, True)
                    break
                blackjackmenu2()

            elif n == 2:
                print('Stand')
                pick_surrender_checkodds = False
                while Game.checksum(dealer_cards) < 17:
                    dealer_cards.append(self.cardlist[0])
                    del self.cardlist[0]
                Game.scoregame(self, dealer_cards, player_cards, player)
                break

            elif n == 3:
                print('Double Down')
                pick_surrender_checkodds = False
                self.standardbet *= 2
                player_cards.append(self.cardlist[0])
                del self.cardlist[0]
                Game.printhand(dealer_cards, player_cards)
                if Game.checksum(player_cards) > 21:
                    print('Bust')
                    Game.scoregame(self, dealer_cards, player_cards, player, False, True)
                else:
                    while Game.checksum(dealer_cards) < 17:
                        dealer_cards.append(self.cardlist[0])
                        del self.cardlist[0]
                    Game.scoregame(self, dealer_cards, player_cards, player)
                self.standardbet /= 2
                self.standardbet = int(self.standardbet)
                break

            elif n == 4:
                if pick_surrender_checkodds == True:
                    print('Surrender')
                    Game.scoregame(self, dealer_cards, player_cards, player, True)
                    break
                else:
                    blackjackmenu()
                    n = getinput(False, n)
                    continue

            elif n == 5:
                if pick_surrender_checkodds == True:
                    good_handvalue = 0
                    for i in self.cardlist:
                        temp_hand = player_cards.copy()
                        temp_hand.append(i)
                        if Game.checksum(temp_hand) <= 21:
                            good_handvalue += 1
                    print(f'Odds that hand value will still be 21 or below: {good_handvalue}/{len(self.cardlist)}')
                    blackjackmenu()
                else:
                    blackjackmenu()
                    n = getinput(False, n)
                    continue

            n = getinput(False, n)

    def __str__(self):
        return f'{self.name} {self.standardbet}'


if __name__ == '__main__':
    cards = input().split(',')
    newcardlist = []
    for card in cards:
        fv = card.split('-')
        newcardlist.append((fv[0],fv[1]))

    player_list, game_list = [], []
    selected_player, selected_game = None, None
    player_list.append(Player('default', 89000))
    default_g = Game('defaultgame', 8, 10)
    default_g.cardlist = newcardlist.copy()
    game_list.append(default_g)

    mainmenu()
    n = int(input())

    while n != 7:
        if n == 1:
            name, money = input().split(',')
            money = int(money)
            player_list.append(Player(name, money))

        elif n == 2:
            list_idx = 1
            for p in sorted(player_list, key = lambda x:x.name):
                 print(list_idx, p)
                 list_idx += 1
            idx_select = int(input())
            selected_player = sorted(player_list, key = lambda x:x.name)[idx_select - 1]

        elif n == 3:
            name, num_decks, standardbet = input().split(',')
            num_decks, standardbet = int(num_decks), int(standardbet)
            game_list.append(Game(name, num_decks, standardbet))

        elif n == 4:
            list_idx = 1
            for g in sorted(game_list, key = lambda x:x.name):
                 print(list_idx, g)
                 list_idx += 1
            idx_select = int(input())
            selected_game = sorted(game_list, key = lambda x:x.name)[idx_select - 1]

        elif n == 5: selected_game.rungame(selected_player)

        elif n == 6: selected_game.rungame(selected_player, True)

        elif n == 7: exit
        
        mainmenu()
        n = int(input())