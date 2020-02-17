import turtle, time, random

#initialise structs
forest = []
colour_dictionary = {0:"teal.gif",1:"white.gif"}

#changable screen variables
screen_size = 500
grid_size = 50

#screen setup
square = screen_size / grid_size

#Turtle setup
turtle.tracer(False)
turtle.addshape("teal.gif")
turtle.addshape("white.gif")

turtle.setup(screen_size + 100,screen_size + 100)
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.goto(-250, 250)


#populate forest struct
def populate(in_forest):
    in_forest = []
    for i in range(0, grid_size):
        temp_ylist = []
        for j in range(0, grid_size):
            temp_ylist.append(1)
        in_forest.append(temp_ylist)
    return in_forest

def random_populate(in_forest):
    in_forest = []
    for i in range(0, grid_size):
        temp_ylist = []
        for j in range(0, grid_size):
            temp_ylist.append(random.randint(0,1))
        in_forest.append(temp_ylist)
    return in_forest

def game_of_life_save():
    with open('output.txt', 'w') as output_file:
        for i in range(0, len(forest)):
            for j in range(0, len(forest[i])):
                output_file.write(str(forest[i][j]))
            output_file.write("\n")

def game_of_life_load():
    with open('output.txt', 'r') as input_file:
        i = 0
        for line in input_file:
            if (i != grid_size):
                for j in range(0, 49):
                    forest[i][j] = int(line[j])
            i+= 1
                            

def forest_output(in_forest):

    my_turtle.clear()
    my_turtle.goto(-250, 250)
    for i in range(0, len(in_forest)):
        for j in range(0, len(in_forest[i])):
            my_turtle.shape(colour_dictionary[in_forest[i][j]])
            my_turtle.stamp()
            my_turtle.forward(square)
        my_turtle.left(180)
        my_turtle.forward(square * len(in_forest[i]))
        my_turtle.left(90)
        my_turtle.forward(square)
        my_turtle.left(90)
    my_turtle.hideturtle()
    turtle.update()
    

def life_tick():
    global forest
    forest_temp = []
    forest_temp = populate(forest_temp)
    for i in range(0, len(forest)):
        for j in range(0, len(forest[i])):
            count = 0
            
            if (i > 0 and forest[i-1][j] == 0):
                count+=1
            if (i < grid_size - 1 and forest[i+1][j] == 0):
                count+=1
            if (j > 0 and forest[i][j-1] == 0):
                count+=1
            if (j < grid_size - 1 and forest[i][j+1] == 0):
                count+=1
            if (i > 0 and j > 0 and forest[i-1][j-1] == 0):
                count+=1
            if (i > 0 and j < grid_size - 1 and forest[i-1][j+1] == 0):
                count+=1
            if (i < grid_size - 1 and j > 0 and forest[i+1][j-1] == 0):
                count+=1
            if (i < grid_size - 1 and j < grid_size - 1 and forest[i+1][j+1] == 0):
                count+=1
            
                
            if (forest[i][j] == 0):
                if (count > 3):
                    forest_temp[i][j] = 1
                elif (count < 2):
                    forest_temp[i][j] = 1
                else:
                    forest_temp[i][j] = 0
            else:
                if (count == 3):
                    forest_temp[i][j] = 0
    forest = forest_temp
 
forest = random_populate(forest)
#game_of_life_load()
while(True):
    forest_output(forest)
    life_tick()
    time.sleep(0.01)
game_of_life_save()