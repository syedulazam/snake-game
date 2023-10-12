from tkinter import*
import random

GAME_WIDTH = 700 # the naming convention of constants in pythin tends to be all in upper case
GAME_HEIGHT = 700
SPEED = 55
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"

class Snake:

    def __init__(self):
        self.coordinates = []
        self.rectangle = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
           rectangle = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
           self.rectangle.append(rectangle)

class Food:

    def __init__(self):

        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)* SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOUR,tag="food") # We used the tag function so
        # that we could delete the rectangle canvas

def next_turn(snake,food):

    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    rectangle = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)

    snake.rectangle.insert(0,rectangle)

    if x == food.coordinates[0] and y == food.coordinates[1]: # We are using this syntax to check if the coordinates of
        # the food and teh snake coincide so that we can delete the food.

        global score

        score+=1
        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.rectangle[-1])

        del snake.rectangle[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):

    global direction

    if direction == "down":
        if direction != "up": # We are using a second if statement is because this if statement is to ensure that
                              # the snake doesn't go 180 degrees
           direction = new_direction
    elif direction == "up":
        if direction != "down":
           direction = new_direction
    elif direction == "right":
        if direction != "left":
           direction = new_direction
    elif direction == "left":
        if direction != "right":
           direction = new_direction

def handle_key(event):
    if event.keysym == "Left":
        change_direction("left")
    elif event.keysym == "Right":
        change_direction("right")
    elif event.keysym == "Up":
        change_direction("up")
    elif event.keysym == "Down":
        change_direction("down")

def restart_game():
    global score, direction, snake, food

    score = 0
    direction = "down"
    label.config(text="Score:{}".format(score))
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    next_turn(snake, food)

def check_collision(snake):

    x,y = snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        print("Game over")
        return True
    elif y<0 or y>=GAME_HEIGHT:
        print("Game over")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game over")
            return True


def game_over():

    canvas.delete(ALL)
    canvas.create_text(window.winfo_width()/2,window.winfo_height()/2,font=("Consolas",35),fill=FOOD_COLOUR,text="Game Over")

window = Tk()
window.title("Snake game")
window.resizable(False,False)

score = 0
direction = "down"

label = Label(text="Score:{}".format(score),fg=SNAKE_COLOR,bg="black",font=("cONSOLAS",20))
label.pack()

frame = Frame(window)
frame.pack()

restart_button = Button(window, text="Restart", font=("Consolas", 12),width=8,command=restart_game,state=NORMAL,
                        relief=RAISED,bd=5,fg =SNAKE_COLOR,bg=FOOD_COLOUR)
restart_button.pack(side=TOP)

canvas = Canvas(window,bg=BACKGROUND_COLOUR,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

snake = Snake()
food = Food()

window.bind("<Left>", handle_key)
window.bind("<Right>", handle_key)
window.bind("<Up>", handle_key)
window.bind("<Down>", handle_key)

# NOTE - It is necessary to mention the left, right, down and up in upper case letter for the first letter only.

next_turn(snake,food)

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.config(bg="Black")
window.mainloop()



