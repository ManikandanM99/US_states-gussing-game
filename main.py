import turtle 
import pandas

screen = turtle.Screen()
screen.title('US state game')
# screen.bgpic('C:/Users/Gnanam/Desktop/w&ip/US-states-game-start/blank_states_img.gif')
image = 'C:/Users/Gnanam/Desktop/w&ip/US-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('C:/Users/Gnanam/Desktop/w&ip/US-states-game-start/50_states.csv')
states = data.state.to_list()
guessed_states = []

 # turtle to write guessed states on the map
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states Correct', prompt='What is the state name?').title()

    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
       
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('C:/Users/Gnanam/Desktop/w&ip/US-states-game-start/missing_states.csv')
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        
    