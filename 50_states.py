import turtle,pandas as pd

screen = turtle.Screen()

screen.title("U.S. states")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pd.read_csv("50_states.csv")

# while True:
answer = screen.textinput("Enter the state","What's another name?")
if answer in states.state:
    turtle.goto(states[states.state == "answer"].x,states[states.state == "answer"].y)
    print(states[states.state == "answer"].x)
    turtle.write(states[states.state == "answer"].state)

print(answer)


turtle.mainloop()


