import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=942, height=721)
screen.title("European Capital Game")
image = "european_capital.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("european_capital.csv")
all_capitals = data.capital.to_list()

# def get_mouse_click_coor(x, y):  # Get hold of capital x and y coordinates
#    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

guessed_capitals = []

while len(guessed_capitals) < 45:
    answer_capital = screen.textinput(title=f"{len(guessed_capitals)}/45 capitals guessed",
                                    prompt="Name one of capital in Europe").title()
    if answer_capital == "Exit":
        missing_capitals = []
        for capital in all_capitals:
            if capital not in guessed_capitals:
                missing_capitals.append(capital)
        new_data = pandas.DataFrame(missing_capitals)
        new_data.to_csv("capitals_to_learn.csv")
        break
    if answer_capital in all_capitals:
        guessed_capitals.append(answer_capital)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        capital_data = data[data.capital == answer_capital]
        t.goto(int(capital_data.x), int(capital_data.y))
        t.write(answer_capital)