import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width


#Prompt the user to input wall's height
wallHeight = float(input('Enter wall height (feet): \n'))

#Prompt the user to input wall's width
wallWidth = float(input('Enter wall width (feet): \n'))

# Calculate and output wall area
wallArea=wallHeight * wallWidth
print('Wall area: ' + str(wallArea) +' square feet')

#calculate and output the amount of paint in gallons needed to paint the wall.
Paint_needed=wallArea/350
print('Paint needed: ' +str(Paint_needed) +' gallons')

#calculate and output the number of 1 gallon cans needed to paint the wall.
Cans_needed=math.ceil(Paint_needed)
print('Cans needed: ' +str(Cans_needed) +' can(s)\n')

#Calculate and output the total cost of the paint cans depending on color
color_choose=input("Choose a color to paint the wall: \n")
cost = Cans_needed * paintColors[color_choose]
print("Cost of purchasing "+color_choose+" paint: $"+str(cost))
   
