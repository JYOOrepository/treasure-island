print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,   
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88   
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP""""""" 
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa 
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

stage1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if stage1.lower() == 'left':
  stage2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if stage2.lower() == 'wait':
    stage3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if stage3.lower() == 'red':
      print("It's a room full of fire. Game Over.")
    elif stage3.lower() == "yellow":
      print("You found the treasure! You Win!")
    elif stage3.lower() == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print('You chose a door that doesn\'t exist. Game Over.') 
  else:
    print('You get attacked by an angry trout. Game Over.')
else:
  print("You fell into a hole. Game Over.")
