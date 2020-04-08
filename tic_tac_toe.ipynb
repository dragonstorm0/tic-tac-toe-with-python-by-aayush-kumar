
#project of tic tac toe
#from Ipython.display import clear_output
#the above is only for ipython notebook incase you are using any
import random
def display_board(board):
    clear_output() #  :-  in case you are using ipython notebook
    print(' '+board[7]+ ' | ' +board[8]+  ' | ' +board[9])
    print('-----------')
    print(' '+board[4]+  ' | ' +board[5]+  ' | ' +board[6])
    print('-----------')
    print(' '+board[1]+  ' | ' +board[2]+  ' | ' +board[3])
    
def player_input():
    marker=''
    while(marker !='X' and marker!='O'):
        marker=input('player 1, choose X or O : ').upper()
        
    player1=marker

    if player1=='X':
        player2='O'
    else:
        player2='X'
    print(f'player 1\'s marker is : {player1} || AND || player 2\'s marker is : {player2}.')

    return (player1,player2)


def place_marker(board,marker,position):

    board[position]=marker

def win_cheak(board, mark):
    ((board[1]==mark and board[2]==mark and board[3]==mark)
     or (board[4]==mark and board[5]==mark and board[6]==mark)
     or (board[7]==mark and board[8]==mark and board[9]==mark)
     or (board[1]==mark and board[5]==mark and board[9]==mark)
     or (board[3]==mark and board[5]==mark and board[7]==mark)
     or (board[1]==mark and board[4]==mark and board[7]==mark)
     or (board[2]==mark and board[5]==mark and board[8]==mark)
     or (board[3]==mark and board[6]==mark and board[9]==mark))

def choose_first():
    flip=random.randint(0,1)

    if(flip==0):
        return ('player 1')
    else:
        return ('player 2')

def space_cheak(board,position):
    return board[position]==' '

def full_board_cheak(board):
    for i in range(1,10):
        if space_cheak(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_cheak(board,position):
        position=int(input('choose a position (from 1 to 9) : '))

    return position

def replay():
    choice =input('wanna play again? enter yes or no. ').lower()
    if(choice=='yes'):
        play_game()
    else:
        print('thanks for playing. ')
        


print('welcome to tic tac toe by aayush kumar')
def play_game():
    
    while True:

        the_board=[' ']*10
        player1_marker , player2_marker= player_input()

        turn= choose_first()
        print(f'{turn} will go first . Let\'s continue')

        play_game =input('ready to play? y or n?').lower()
        if play_game =='y':
            game_on=True
        else:
            game_on=False

        while game_on:
            if (turn=='player 1'):
                #show the board
                display_board(the_board)
                #choose the position
                position=player_choice(the_board)
                #put the marker on position
                place_marker(the_board,player1_marker,position)
                #cheak if they won
                if win_cheak(the_board,player1_marker):
                    display_board(the_board)
                    print('congrats, player 1 has WON!!')
                    game_on=False
                else:
                    if full_board_cheak(the_board):
                        display_board(the_board)
                        print('game TIE')
                        game_on=False
                    else:
                        turn= 'player 2'

            else:
                display_board(the_board)
                position=player_choice(the_board)
                place_marker(the_board,player2_marker,position)
                if win_cheak(the_board,player2_marker):
                    display_board(the_board)
                    print('congrats, player 2 has WON!!')
                    game_on=False
                else:
                    if full_board_cheak(the_board):
                        display_board(the_board)
                        print('game TIE')
                        game_on=False
                    else:
                        turn= 'player 1'


        if not replay():
            break
        


play_game() #if not using ipython notebook you may need this to run your file
    

