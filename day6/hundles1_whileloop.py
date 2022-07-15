   
# This is just code for solving Reeborg's challenge where some functions like  turn_left() is defined. The exercise is done online in the browser at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hundles = 6
while number_of_hundles > 0:
    jump()
    number_of_hundles -= 1
    print(number_of_hundles)
