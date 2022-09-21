human_turn = 'paper'
computer_turn = 'paper'

if human_turn == computer_turn:
    print('Draw!')
elif human_turn == 'rock' and computer_turn == 'scissors':
    print('Humans wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('Humans wins!')    
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('Humans wins!')    
else:
    print('Computer wins!')
