from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while count < 3: 
  num = random.randint(1, 6) 
  print(num) 
  if num == 5: 
    print("Sorry, you lose!") 
    break 
  count += 1 
 else: 
    print("You win!")
