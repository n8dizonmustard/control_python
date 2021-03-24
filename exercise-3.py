# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

x = input("Input a dog's age in human years: ")

dog_age = 0

if int(x) == 2:
  dog_age += 20
  print("The dog's age in dog years is " + str(dog_age))
elif int(x) == 1:
  dog_age += 10
  print("The dog's age in dog years is " + str(dog_age))
elif int(x) >= 3:
  dog_age += 20+(int(x)-2)*7
  print("The dog's age in dog years is " + str(dog_age))