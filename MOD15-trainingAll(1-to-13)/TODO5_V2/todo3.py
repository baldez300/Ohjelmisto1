import random
import time
import os

# Training

width = 30
hight = 5

player_x = 1
player_y = 1


def render():
    os.system("cls")
    for y in range(hight):
        if y == 0 or y == hight -1:
            print("#" * width)
        elif y == player_y + 1:
            print("#" + " " * player_x + "P" + " " * (width - player_x - 3) + "#")
        else:
            print("#" + " " * (width - 2) + "#")


def move_player():
    global player_x
    global player_y

    try_moving_player = True
    while try_moving_player:
        r = random.randint(1, 4)
        try_moving_player = False

        if r == 1 and player_x > 0:
            player_x -= 1
        elif r == 2 and player_x < width - 3:
            player_x += 1
        elif r == 3 and player_y > 0:
            player_y -= 1
        elif r == 4 and player_y < hight - 3:
            player_y += 1
        else:
            try_moving_player = True


for i in range(200):
    move_player()
    render()
    time.sleep(0.05)