# This is just code for solving maze project where some functions like  turn_left() is defined. The exercise is done online in the browser. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Depending on the robot position, you may end up having an infinite while loop.
# I will come back here to debug this code after day 15.

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()        