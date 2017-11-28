# Prompt the user to enter the arrow base height.
arrow_base_height = int(input('Enter arrow base height: \n'))

# Prompt the user to enter the arrow base width.
arrow_base_width = int(input( 'Enter arrow base width: \n'))


arrow_head_width=0
while arrow_head_width <= arrow_base_width:    
   # Prompt the user to enter the arrow head width.
   print ('Enter arrow head width: ')
   arrow_head_width = int(input())



for i in range(arrow_base_height):
    print("*"*arrow_base_width)
    
    
for j in range(arrow_head_width):
    print("*"*(arrow_head_width-j))
