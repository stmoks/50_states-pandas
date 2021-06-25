import turtle,pandas as pd

screen = turtle.Screen()

screen.title("U.S. states")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen_draw = turtle.Turtle()
pen_draw.hideturtle()
pen_draw.penup()

states = pd.read_csv("50_states.csv")


def lower(s):
    return s.lower()

states_list = states.state.to_list()
guessed_states = []




while len(guessed_states) < 50:
    answer = screen.textinput((f"{len(guessed_states)}/50"),"Enter the state").title()
    if answer == "Exit":
        break

    if answer in states.state.to_list():
        guessed_states.append(answer)
        x_coor = states[states["state"] == answer].x
        y_coor = states[states["state"] == answer].y

        pen_draw.goto(x_coor.to_list()[0],y_coor.to_list()[0])
        pen_draw.write(states[states.state == answer].state.to_list()[0]) 
        # can use the original answer or the below
        # pen_draw.write(states.item())


missed_states = [x for x in states_list if x not in guessed_states]
missed_states = pd.DataFrame(missed_states)
missed_states.to_csv("missed_states.csv")






