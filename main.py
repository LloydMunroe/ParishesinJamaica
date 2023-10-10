import turtle
import pandas


screen = turtle.Screen()
screen.title("My_Jamaica_Game")
image = ("jm-02.gif")
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("jamaica_parishes.csv")
# print(data)
all_parishes = data.parishes.to_list()

guessed_parishes = []
Tries = 6
td = turtle.Turtle()

while len(guessed_parishes) < 27:

    guess = screen.textinput(title=f"{len(guessed_parishes)}/27 Parishes and capital correct",
                             prompt="Please enter the name of a parish or capital town").title()
    if guess == "Exit":
        missing_parishes = []
        for parish in all_parishes:
            if parish not in all_parishes:
                missing_parishes.append(parish)
        new_data = pandas.DataFrame(missing_parishes)
        new_data.to_csv("Parishes and capitals to learn.csv")
        break

    if guess in all_parishes:
        guessed_parishes.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        parish_cor = data[data.parishes == guess]
        t.goto(int(parish_cor.x), int(parish_cor.y))
        t.write(guess)
        #t.write(parish_cor.parish.item()) # item gives the first item in a panda data series Item() is a method in panda.

    # for (index,row) in data.iterrows(): # we can use this to get the cordinate of a parish, GET a CEll value.
    #     cor = (row.x, row.y)
    #     #print(cor)

    if guess not in all_parishes:
        Tries -= 1
        td.penup()
        td.hideturtle()
        td.goto(-129, 122)
        td.clear()# for clear to work, create the turtle outside the loop.
        td.write(f"You have {Tries} tries left!")
        if Tries == 0:
            guess = "Exit"
            break



        #new_data.to_csv("Parishes and capitals to learn.csv") # not creating a readable csv
        # t.write(parish





# def get_mouse_click_coor(x,y):  # Used for getting the location on the map
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

#screen.exitonclick()
turtle.mainloop()

# does the same as exit on click. Keep the screen up until you remove it.