from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
num = random.randint(1, 6) 
while guesses_left > 0: 
  guess = int(input("Your guess: "))  
  if num == 5: 
    print("Sorry, you lose!") 
    break 
  count += 1 
 else: 
    print("You win!")
