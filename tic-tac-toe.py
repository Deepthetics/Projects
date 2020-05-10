# Class containing player information
class Player():

    def __init__(self,name,turn=False):
        self.name = name
        self.mark = ''
        self.turn = turn

    # Returns value of of the variable "name"  
    def get_name(self):
        return self.name

    # Returns value of of the variable "mark"
    def get_mark(self):
        return self.mark

    # Sets value of of the variable "mark"
    # Parameter 'mark' expected as a string of either 'X' or 'O'
    def set_mark(self,mark):
        self.mark = mark

    # Returns value of of the variable "turn"
    def get_turn(self):
        return self.turn

    # Sets value of of the variable "turn"
    def set_turn(self,boolean):
        self.turn = boolean


# Class containing game board information
class Board():

    def __init__(self,positions=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']):
        self.positions = positions

    # Displays the board
    def display(self):
        print(f'\n {self.positions[7]} | {self.positions[8]} | {self.positions[9]} \n---|---|---\n {self.positions[4]} | {self.positions[5]} | {self.positions[6]} \n---|---|---\n {self.positions[1]} | {self.positions[2]} | {self.positions[3]} \n')

    # Clears the board for replay
    def clear_board(self):
        self.positions = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Returns the list of values associated with the board
    def get_positions(self):
        return self.positions

    # Adds a value to the list of values associated with the board
    def add_mark(self,player,position):
        self.positions[position] = player.get_mark()

    # Returns True if the position is empty 
    # Parameter 'position' expected to be the player chosen position for their mark on the game board
    def position_is_empty(self,position):
        
        if self.positions[position] == ' ':
            return True
        else:
            return False

    # Returns True if the 'X' wins the game
    def check_X_win(self):
        
        if self.positions[1] == 'X' and self.positions[2] == 'X' and self.positions[3] == 'X':
            return True
        elif self.positions[4] == 'X' and self.positions[5] == 'X' and self.positions[6] == 'X':
            return True
        elif self.positions[7] == 'X' and self.positions[8] == 'X' and self.positions[9] == 'X':
            return True
        elif self.positions[1] == 'X' and self.positions[4] == 'X' and self.positions[7] == 'X':
            return True
        elif self.positions[2] == 'X' and self.positions[5] == 'X' and self.positions[8] == 'X':
            return True
        elif self.positions[3] == 'X' and self.positions[6] == 'X' and self.positions[9] == 'X':
            return True
        elif self.positions[1] == 'X' and self.positions[5] == 'X' and self.positions[9] == 'X':
            return True
        elif self.positions[3] == 'X' and self.positions[5] == 'X' and self.positions[7] == 'X':
            return True
        else:
            return False

    # Returns True if the 'O' wins the game
    def check_O_win(self):
        
        if self.positions[1] == 'O' and self.positions[2] == 'O' and self.positions[3] == 'O':
            return True
        elif self.positions[4] == 'O' and self.positions[5] == 'O' and self.positions[6] == 'O':
            return True
        elif self.positions[7] == 'O' and self.positions[8] == 'O' and self.positions[9] == 'O':
            return True
        elif self.positions[1] == 'O' and self.positions[4] == 'O' and self.positions[7] == 'O':
            return True
        elif self.positions[2] == 'O' and self.positions[5] == 'O' and self.positions[8] == 'O':
            return True
        elif self.positions[3] == 'O' and self.positions[6] == 'O' and self.positions[9] == 'O':
            return True
        elif self.positions[1] == 'O' and self.positions[5] == 'O' and self.positions[9] == 'O':
            return True
        elif self.positions[3] == 'O' and self.positions[5] == 'O' and self.positions[7] == 'O':
            return True
        else:
            return False

    # Returns True if the game ends in a tie
    def check_tie(self):
        
        for i in self.positions:
            if i == ' ':
                return False
        return True


# Asks and returns player's name for Player-object init
def ask_player_name(player):
    
    name = input('{} please type in your name: '.format(player))
    return name


# Defines player marks between 'X' and "O"
def define_player_marks(player1,player2):

    while True:
        mark = input('\n{}, do you want to be an "X" or an "O"? '.format(player1.get_name()))
    
        if mark.upper() == 'X':
            player1.set_mark(mark.upper())
            player2.set_mark('O')
            break
        elif mark.upper() == 'O':
            player1.set_mark(mark.upper())
            player2.set_mark('X')
            break
        else:
            print('Please type either "X" or "O".')
            continue


# Prints information about the players
def print_player_information(player):
    print('{} is "{}".'.format(player.get_name(),player.get_mark()))

# Print the instruction game board
def print_instruction_board():
    instruction_board = Board(['#',1,2,3,4,5,6,7,8,9])
    instruction_board.display()

# Prints game instructions
def print_game_instructions():
    print('\n//INSTRUCTIONS//')
    print('The game board is shown below.\nIt has nine slots total and each slot has its own numeric code.\nThe layout of the numeric codes is the same as on keyboard NumPad.\nWhen placing your mark during the game, type the number of corresponding slot where you want to place your mark.\n')
    print_instruction_board()


# Changes player turn
def change_player_turn(player1,player2):
    player1.set_turn(not(player1.get_turn()))
    player2.set_turn(not(player2.get_turn()))


from random import randint

# Chooses the starting player
def randomize_starting_player(player1,player2):
    
    random_integer = randint(1,2)
    
    if random_integer == 1:
        player1.set_turn(True)
        player2.set_turn(False)
        print('{} will go first.'.format(player1.get_name()))
    else:
        player1.set_turn(False)
        player2.set_turn(True)
        print('{} will go first.'.format(player2.get_name()))


# Asks the player for the mark position
def ask_mark_position(player):
    while True:
        try:
            position = int(input('{}, where do you want to place your mark? Choose a position between 1 and 9: '.format(player.get_name())))
            if position < 1 or position > 9:
                print('Please enter a number between 1 and 9.')
                continue
            else:
                return position
        except:
            print('Please enter a whole number between 1 and 9.')


# Executes player turn 
def player_turn(board,player):
    
    while True:
        # Asking for mark position
        position = ask_mark_position(player)
        # Checking is the chosen position available
        if board.position_is_empty(position):
            # Adding mark to the chosen position
            board.add_mark(player,position)
            break
        else:
            print('The position you chose is already taken. Please choose a different position.')
            continue


# Returns True if there is a win
def game_is_won(board):
    
    if board.check_X_win() == True or board.check_O_win() == True:
        return True
    else:
        return False


# Return True if the game is a tie
def game_is_tie(board):
    if board.check_tie() == True:
        print('The game is a tie.')
        return True


# Prints information about the winner
def print_winner_information(board,player1,player2):
    
    if board.check_X_win() == True:
        if player1.get_mark() == 'X':
            print('{} has won!'.format(player1.get_name()))
        else:
            print('{} has won!'.format(player2.get_name()))
            
    elif board.check_O_win() == True:
        if player1.get_mark() == 'O':
            print('{} has won!'.format(player1.get_name()))
        else:
            print('{} has won!'.format(player2.get_name()))


# Asks for replay and returns True if the replay is wanted
def ask_replay():
    
    while True:
        decision = input('Do you want to play again? Answer "Yes" or "No": ')
        if decision.lower() == 'yes':
            return True
        elif decision.lower() == 'no':
            return False
        else:
            print('Please type either "Yes" or "No".')
            continue


# Informative printing
print('Welcome to the game of Tic Tac Toe!\n')

# Creating players
player1 = Player(ask_player_name("Player 1"))
player2 = Player(ask_player_name("Player 2"))

# Defining player marks
define_player_marks(player1,player2)

print_player_information(player1)
print_player_information(player2)

# Printing game instructions
print_game_instructions()

# Creating board
board = Board()

# Game starting
while True:
    
    # Randomizing the starting player
    randomize_starting_player(player1,player2)
    
    # Displaying board
    board.display()
    
    # Loop of the gameplay
    while True:
        
        # Checking whose turn it is
        if player1.get_turn() == True:
            # Player 1 turn
            player_turn(board,player1)
        else:
            # Player 2 turn
            player_turn(board,player2)
        
        # Displaying the board after player turn
        print_instruction_board()
        board.display()
        
        # Checking for win
        if game_is_won(board) == True:
            # Informative printing 
            print_winner_information(board,player1,player2)
            break
        # Checking for tie
        elif game_is_tie(board) == True:
            break
        # Changing player turn
        else:            
            change_player_turn(player1,player2)
            continue
    
    # Asking for replay
    play_again = ask_replay()        
    if play_again == True:
        # Clearing the board
        board.clear_board()
        continue
    else:
        break

# Informative printing
print('Thank you for playing!')

