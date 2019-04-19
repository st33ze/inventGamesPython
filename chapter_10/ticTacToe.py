# Implementation of Tic Tac Toe game.

import random
import data as d

def main():
    letters = game_initialize() # [player_letter, computer_letter]
    turn = random.randint(0,1)
    
    # Play the game.
    while True:
        # Player's turn.
        if turn == 0:
            draw_board(d.game_fields)
            get_player_field(letters[0])
            turn = 1
        
        # Computer's turn.
        else:
            computer_move(letters)
            turn = 0

        status = game_over_check(letters)
        if status:
            # Ask if user wants to play again. If yes, reset needed variables.
            re_match = input('If you want to play again type \'y\': ').lower()
            if re_match == 'y':
                d.game_fields = list(' ' * 10)
                letters = game_initialize()
                turn = random.randint(0,1)
            else: break

def game_initialize():
    '''
        Welcomes user, prints guide and allows to choose letter. Returns list with 
        letters 'X' and 'O'in specific order. Player's letter is the first letter in the
        returend list and computer's is second.
    '''

    print('Welcome to TIC TAC TOE :)')
    print('Fields numbers:')
    draw_board(list(range(10)))

    while True:
        chosen_letter = input('Would you like to play as "X" or "O"? ').upper()
        if chosen_letter == 'X': return ['X', 'O']
        elif chosen_letter == 'O': return ['O', 'X']

def draw_board(fields):
    '''Draws board with current d.game_fields values.'''
     
    print(' ___ ___ ___')
    print(f'| {fields[7]} | {fields[8]} | {fields[9]} |')
    print('|---+---+---|')
    print(f'| {fields[4]} | {fields[5]} | {fields[6]} |')
    print('|---+---+---|')
    print(f'| {fields[1]} | {fields[2]} | {fields[3]} |')
    print(' --- --- ---')

def get_player_field(letter):
    '''Gets and validates player's input. Updates d.game_fields.'''

    while True:
        p_field = input('Choose a field: ')
        try:
            p_field = int(p_field)
            if p_field >= 1 and p_field <= 9 and d.game_fields[p_field] == ' ':
                d.game_fields[p_field] = letter
                return
        except ValueError: continue

def computer_move(letters):
    '''Algorithm to look for the best move. If found, updates d.game_fields.'''

    # Check win possibility.
    for opt in d.win_options:
        line = [d.game_fields[opt[0]], d.game_fields[opt[1]], d.game_fields[opt[2]]]
        if line.count(letters[1]) == 2 and ' ' in line:
            d.game_fields[opt[line.index(' ')]] = letters[1]
            return

    # Check block possibility.
    for opt in d.win_options:
        line = [d.game_fields[opt[0]], d.game_fields[opt[1]], d.game_fields[opt[2]]]
        if line.count(letters[0]) == 2 and ' ' in line:
            d.game_fields[opt[line.index(' ')]] = letters[1]
            return

    # Take middle field.
    if d.game_fields[5] == ' ': 
        d.game_fields[5] = letters[1]
        return
    
    # Take one of the corner fields.
    for index, field in enumerate(d.game_fields):
        if index in (1, 3, 7, 9) and field == ' ': 
            d.game_fields[index] = letters[1]
            return
    
    # Take other field.
    for index, field in enumerate(d.game_fields):
        if field == ' ' and index > 0: 
            d.game_fields[index] = letters[1]

def game_over_check(letters):
    '''Check for win or tie conditions. If found returns True.'''

    # Check if player or computer won.
    for opt in d.win_options:
        line = [d.game_fields[opt[0]], d.game_fields[opt[1]], d.game_fields[opt[2]]]
        if line.count(letters[0]) == 3:
            print_result('Congratulations, you win! :)')
            return True
        elif line.count(letters[1]) == 3:
            print_result('Computer wins!')
            return True

    # Check for the tie.
    if not ' ' in d.game_fields[1:]:
        print_result('It\'s a tie!')
        return True

def print_result(result):

    print()
    print('= GAME OVER =')
    draw_board(d.game_fields)
    print(result)
    print()


if __name__ == "__main__":
    main()