#display the original map when starts
def display_map(game_map,player):
    print(' _'*game_map.width)
    for row in game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            else:
                print(tile,end='')
        print('|')

#in each step, input "a" will move the character to the left (updated map must be shown)
def move_player(player,move):
    x,y = player.x,player.y
    if move == 'a':
        x -= 1
    if move == 'd':
        x += 1
    if move == 'UP':
        y -= 1

    return x,y


#in each step, other input will not move the character (updated map must be shown) 
def get_moves(player):
    moves = ['UP','DOWN','LEFT','RIGHT','a','d']
    x,y = player.x,player.y
    if x == 0:
        moves.remove('LEFT')
    if x == player.game_map.width - 1:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == player.game_map.height - 1:
        moves.remove('DOWN')
    return moves

# colliding with a coin increases score by 10 (must be true for every coin)
def coin_collect(player,coin):
    if player.x == coin.x and player.y == coin.y:
        player.score += 10
        return True
    return False

#colliding with a wall 
	

def wall_crash(player,wall):
    if player.x == wall.x and player.y == wall.y:
        return True
    return False

# produces a crash screen (crash point shown by "*").
def crash_screen(player,wall):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            elif tile == wall:
                print('*',end='')
            else:
                print(tile,end='')
        print('|')  

# and then game over screen is shown.
def game_over(player):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            else:
                print(tile,end='')
        print('|')
    print('Game Over!')
    print('Final Score: {}'.format(player.score))

#colliding with a finish line
def finish_line(player,finish):
    if player.x == finish.x and player.y == finish.y:
        return True
    return False


#produces a screen where the character is at the finish line.
def finish_screen(player,finish):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            elif tile == finish:
                print('F',end='')
            else:
                print(tile,end='')
        print('|')
    print('You Win!')
    print('Final Score: {}'.format(player.score))


#and then congratuations screen is shown.
def congratuations_screen(player):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            else:
                print(tile,end='')
        print('|')
    print('Congratulations!')
    print('Final Score: {}'.format(player.score))

# if the player score is enough as one of the high score, prompt the player to enter his/her name.
def high_score_screen(player):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            else:
                print(tile,end='')
        print('|')
    print('Congratulations!')
    print('You made the high score list!')
    print('Please enter your name:')
    player.name = input()
    print('Your name is {}'.format(player.name))
    print('Final Score: {}'.format(player.score))

# if the player score is not enough as one of the high score, do not prompt the player to enter his/her name.
def not_high_score_screen(player):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            else:
                print(tile,end='')
        print('|')
    print('Congratulations!')
    print('You did not make the high score list!')
    print('Final Score: {}'.format(player.score))

# high score is displayed correctly at the end of the game.
#  With number of lines, combining with game over/congratulations screen, 
# equal to 10 (not including the input name prompt).
def display_high_score(player):
    print(' _'*player.game_map.width)
    for row in player.game_map:
        print('|',end='')
        for tile in row:
            if tile == player:
                print('X',end='')
            else:
                print(tile,end='')
        print('|')
    print('High Score:')
    for score in player.high_score:
        print('{} - {}'.format(score[0],score[1]))
    

 #high score saved in a file.

 display_map(game_map,player)
    while True:
    