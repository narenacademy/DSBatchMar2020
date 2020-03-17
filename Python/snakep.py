from random import *
max_value=100
dice_face=6
snake={8:4,18:1,26:10,39:5,51:6,54:36,56:1,60:23,75:28,83:45,85:59,90:48,92:25,97:87,99:63}
ladder={3:20,6:14,11:28,15:34,17:74,22:37,38:59,49:67,57:76,61:78,73:86,81:98,88:91}
def validate_snakeandladder(player_name,current_value,dice_value):
    def get_player_name():
    player_name=input("please enter valid name:")
    print(player_name)
    def diceroll():
    roll=randint(1,6)
    print(roll)
    return roll
def change_pos(position):
    dice=diceroll()
    if(position<=94)
        position=dice+position
        if(validate()=='snake'):
            position=position-snake_length
        elif(validate()=='ladder')
            position=position+ladder-length
        else:
            position=position
    else:
        if(position in ['95','96','97','98','99'] and dice==6):
            diceroll()
        elif(position in ['96','97','98','99'] and dice==5):
            diceroll()
        elif(position in ['97','98','99'] and dice==4):
            diceroll()
        elif(position in ['98','99'] and dice==3):
            diceroll()
        elif(position=='99' and dice==2):
            diceroll()
        else:
            position=dice+position
    print(position)
    return position
def start():
    player1_name = get_player_names()
    player_current_position=0
diceroll()
change_pos()