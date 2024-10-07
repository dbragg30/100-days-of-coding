import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)

#answer_state = screen.textinput(title="Guess the State", prompt="What is another state's name?")

#answer_state = answer_state.title()

data = pandas.read_csv("50_states.csv", index_col=False)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What is another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #t.write(state_data.state.item())
        t.write(answer_state)
def states_to_learn(a,b):
    return [x for x in a if x not in b]



df = pandas.DataFrame(states_to_learn(all_states, guessed_states))
df.to_csv("missing_states.csv", index=False)

#state_to_learn.csv



# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#screen.exitonclick()


