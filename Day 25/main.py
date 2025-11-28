import turtle, pandas

IMAGE = "blank_states_img.gif"
FONT = ("Courier", 10, "normal")
FONT2 = ("Courier", 15, "bold")

# def learning_file():
#     """generate a file with states to learn"""
#     data = pandas.DataFrame(states_correct)
#     data.to_csv("states_to_learn.csv", index=False)

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)
st = turtle.Turtle()
st.hideturtle()
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
states_correct = []
all_states = data.state.to_list()


game_is_over = False
while not game_is_over:
    answer_state = screen.textinput(title=f"{len(states_correct)}/50 States Correct", prompt="What's another state's name?").title()


    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in states_correct]
        new_data = pandas.DataFrame(missing_states)
        new_data.columns = ["States to learn"]
        new_data.to_csv("states_to_learn.csv", index = False)
        break

    if answer_state in data["state"].values:
        state_data = data[data["state"] == answer_state]
        state_x = state_data.x.values[0] # .item() = .values[0]
        state_y = state_data.y.item()
        st.penup()
        st.teleport(state_x,state_y)
        screen.update()
        st.write(answer_state, align="left", font = FONT)
        states_correct.append(answer_state)

    if len(states_correct) == 50:
        game_is_over = True
        st.goto(0,260)
        st.write("Congratulations! You've guessed all U.S. States!", align="center", font = FONT2)
