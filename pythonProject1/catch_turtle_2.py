import random
import turtle

screen = turtle.Screen()
game_over = False
score = 0
FONT = ('Arial', 30, 'normal')

# turtle list
turtle_list = []

# combined display turtle
display_turtle = turtle.Turtle()

grid_size = 10

def setup_display_turtle():
    display_turtle.hideturtle()
    display_turtle.color("blue")
    display_turtle.penup()
    display_turtle.setposition(0, screen.window_height() / 2 - 50)
    update_display()

def update_display(time=10):
    display_turtle.clear()
    display_turtle.write(arg=f'Score: {score}  Time: {time}', move=False, align='center', font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        update_display()
        print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    if time > 0:
        update_display(time)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        hide_turtles()
        update_display(0)
        display_turtle.setposition(0, 0)  # Move the display turtle to the center
        display_turtle.color("red")
        display_turtle.write("Game Over!", align='center', font=FONT)


def start_game():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_display_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game()
turtle.mainloop()
