# Date: 9/30/24
# Name: Calculation Cruncher (Python)
# Author: Andrea B.
# Contact: baciuandrea04@gmail.com
# Description: This was a project game I made to learn and apply math functions I was learning about.

# import modules
import random
import time

# DISPLAYING PROBLEM ASPECT

# variables
operators = ["+", "-"]

min_operator = 1
max_operator = 20
total_problems = 15

# ANSI escape codes
bold_start = "\033[1m"
bold_end = "\033[0m"

def calculate_problems():
    # generate problem for left and right sides of problem displayed
    left = random.randint(min_operator, max_operator)
    right = random.randint(min_operator, max_operator)
    # randomly selects operator
    operator = random.choice(operators) #'choice' function picks elements from 'operators' list

    #Output
    problem = str(left) + " " + operator + " " + str(right)
    solution = eval(problem) # 'eval' function evaluates string as if they were expression (to avoid if statements)
    
    return problem, solution

# TIMER ASPECT

#stores all the problems user got incorrect
incorrect_problems = 0
# asks user if they are ready to begin
input(f"🎉 Welcome to {bold_start}Calculation Cruncher{bold_end}! 🎉\n\nGet ready to put your math skills to the ultimate test!\nYou will be given 15 problems to solve. See how fast you can do it!\n\nAre you ready to begin? Press enter: ")

# stores time user begins game
start_time = time.time() # Unix timestamp in second

# Display output
for i in range (total_problems):
    problem, solution = calculate_problems()
    while True:
        user_problem = input("%s. " % (str(i + 1)) + problem + " = ")
        if user_problem == str(solution): # 'solution' is an integer, 'user_problem" is a string, so convert 'solution' to string    
            break
        else:
            print(f"Wrong! Try again")
        incorrect_problems += 1

# when user finishes problems, displays total time taken
end_time = time.time()
total_time = round(end_time - start_time, 2) # 'round' function rounds a decimal number to whatever decimal place parameter
print(f"Total time taken: {total_time} seconds")