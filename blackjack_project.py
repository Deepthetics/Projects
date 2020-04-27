class Funds():
    
    def __init__(self,value=0):
        self.value = value
    
    # Adds player funds when player wins or adds more to the table
    def add_funds(self,amount):
        
        self.value = self.value + amount
    
    # Removes player funds when betting
    def remove(self,amount):
        
        self.value = self.value - amount

    
import random

class Deck():
    
    # list of cards
    def __init__(self,name,list_of_cards=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]):
        self.name = name
        self.list_of_cards = list_of_cards
    
    # Picks a random card from the deck removing it from the list of cards
    def pick_card(self):
        
        card = random.choice(self.list_of_cards)
        self.list_of_cards.remove(card)
        return card
    
    # Resets the deck
    def reset(self):
        self.list_of_cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
    
    def __str__(self):
        return f'{self.list_of_cards}'

    
class Hand():
    
    # list of cards
    def __init__(self,name):
        self.name = name
        self.list_of_cards = []
    
    # Adds a card to the hand
    # Method is expecting an integer value as its parameter representing the value of a card
    def add_card(self,card):
        
        self.list_of_cards.append(card)
    
    # Returns the value of the hand
    def get_value(self):
        
        value = 0
        for card in self.list_of_cards:
            value = value + card
        return value

    def length(self):
        return len(list_of_cards)
                
    # Used to return only the first card of the dealer's hand
    def return_first(self):
        return self.list_of_cards[0]
    
    # Used to return all the cards in the hand
    def return_all(self):
        return_string = ''
        i = 0
        for card in self.list_of_cards:
            if i == 0:
                return_string = '{}'.format(card)
            elif len(self.list_of_cards) - 1 == i:
                return_string = return_string + ' and {}'.format(card)
            else:
                return_string = return_string + ', {}'.format(card)
            i = i + 1
        return return_string
    
    def elevens_to_one(self):
        
        return_value = 0
        for card in self.list_of_cards:
            if card == 11:
                return_value = return_value + 10
        return return_value
        
    # Empties the hand
    def empty(self):
        self.list_of_cards.clear()
                        
    def __str__(self):
        return f'{self.list_of_cards}'
    

# Program

# Creating player funds
player_funds = Funds()

# Creating a new deck
deck = Deck(name="Blackjack Deck")

# Creating dealer and player hands
dealer_hand = Hand(name='Dealer')
player_hand = Hand(name='Player')

print('Welcome to the game of Blackjack!')

# Asking for starting funds
while True:
    
    try:
        starting_value = int(input('\nType the amount of funds you want to start with: '))
    except ValueError:
        print('\nPlease type a number of positive value.')
        continue
        
    if starting_value > 0:
        player_funds.add_funds(starting_value)
        break
    else:
        print('\nPlease type a whole number of positive value.')
        continue

print('\nYour funds are now {}.'.format(player_funds.value))

# Loop of the game
while True:
    
    # Asking for the bet or to add more funds to the table
    player_input = input('\nIf you want to play, place your bet for the upcoming hand.\nIf you want to add more funds, type "add".\nIf you want to stop playing, type "quit." ')
    player_bet = 0
    
    # Adding more funds to the table
    if player_input == 'add': 
        try:
            amount = int(input('\nType the amount of funds you want to add: '))
        except:
            print('\nPlease type a whole number of positive value.')
            continue
        if amount > 0:
            player_funds.add_funds(amount)
            print('\nYou have added {} to your funds. Your funds are now {}.'.format(amount,player_funds.value))
            continue
        else:
            print('\nPlease type a number of positive value.')
            continue
    # Quitting the game
    elif player_input == 'quit':
        print('\nThank you for playing!')
        break
    # Placing the bet
    else:
        try:
            player_bet = int(player_input)
        except:
            print('\nPlease type a number of positive value as your bet.')
            continue
        if player_bet > player_funds.value:
            print('\nIt is not possbile to bet more than your funds are. Add more funds to bet that much.')
            continue
        elif player_bet > 0:
            print('\nYour bet is {}.'.format(int(player_input)))
            player_funds.remove(player_bet)
        else:
            print('\nPlease type a number of positive value as your bet.')
            continue
     
    # Dealing two cards to both dealer and the player
    dealer_hand.add_card(deck.pick_card())
    dealer_hand.add_card(deck.pick_card())    
    player_hand.add_card(deck.pick_card())
    player_hand.add_card(deck.pick_card())
    
    # Informative printing
    print(f'\nDealer has {dealer_hand.return_first()} and one other card.')

    if player_hand.get_value() == 22:
        print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value() - player_hand.elevens_to_one()} ')
    else:
        print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value()}.')
    
    # Checking for player win
    if player_hand.get_value() == 21:
        print('\nYou have won!')
        player_funds.add_funds(player_bet * 2)
        print('\nYour funds are now {}.'.format(player_funds.value))
        deck.reset()
        dealer_hand.empty()
        player_hand.empty()   
        continue
    
    # Asking for player decision
    while True:
        player_choice = input('\nType "hit" to hit a card or type "stay" to stay where you at: ')
        
        # If player decides to hit
        if player_choice == 'hit':
            player_hand.add_card(deck.pick_card())
            
            # Checking for player win
            if player_hand.get_value() == 21:
                print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value()}.')
                print('\nYou have won!')
                player_funds.add_funds(player_bet * 2)
                print('\nYour funds are now {}.'.format(player_funds.value))
                break
                
            # Checking if player is busted
            if player_hand.get_value() > 21:
                if player_hand.get_value() - player_hand.elevens_to_one() > 21:
                    print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value() - player_hand.elevens_to_one()}.')
                    print('\nYou busted!')
                    print('\nYour funds are now {}.'.format(player_funds.value))
                    break
                elif player_hand.get_value() - player_hand.elevens_to_one() == 21:
                    print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value() - player_hand.elevens_to_one()}.')
                    print('\nYou have won!')
                    player_funds.add_funds(player_bet * 2)
                    print('\nYour funds are now {}.'.format(player_funds.value))
                    break
                else:
                    print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value() - player_hand.elevens_to_one()}.')
                    continue
            if player_hand.get_value() < 21:
                print(f'\nYou have {player_hand.return_all()}. The value of your hand is {player_hand.get_value()}.')
                    
        # If player decides to stay           
        elif player_choice == 'stay':
            if player_hand.get_value() < 21:
                print(f'\nYou decided to stay at {player_hand.get_value()}.')
            else:
                print(f'\nYou decided to stay at {player_hand.get_value() - player_hand.elevens_to_one()}.')
            while True:
                if dealer_hand.get_value() < 22:
                    print(f"\nDealer has {dealer_hand.return_all()}. The value of the dealer's hand is {dealer_hand.get_value()}.")
                else:
                    print(f"\nDealer has {dealer_hand.return_all()}. The value of the dealer's hand is {dealer_hand.get_value() - dealer_hand.elevens_to_one()}.")	
                # Checking for dealer win
                if dealer_hand.get_value() >= player_hand.get_value() and dealer_hand.get_value() < 22:
                    print('\nDealer wins.')
                    print('\nYour funds are now {}.'.format(player_funds.value))
                    break
                    
                # Checking if dealer is busted
                if dealer_hand.get_value() > 21:
                    if dealer_hand.get_value() - dealer_hand.elevens_to_one() > 21:
                        print('\nDealer busted. You win!')
                        player_funds.add_funds(player_bet * 2)
                        print('\nYour funds are now {}.'.format(player_funds.value))
                        break
                    elif dealer_hand.get_value() - dealer_hand.elevens_to_one() == 21:
                        print('\nDealer wins.')
                        print('\nYour funds are now {}.'.format(player_funds.value))
                        break
                    elif dealer_hand.get_value() - dealer_hand.elevens_to_one() == 22 and dealer_hand.length() == 2:
                        continue
                    else:
                        continue

                print('\nDealer hits a card.')
                dealer_hand.add_card(deck.pick_card())
                continue
            break         
        else:
            print('\nPlease type either "hit or "stay".')
    
    deck.reset()
    dealer_hand.empty()
    player_hand.empty()