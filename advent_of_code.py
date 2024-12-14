import os 
from days import (solve_day1,
                  solve_day2,
                  solve_day3,
                  solve_day4,
                  solve_day5,
                  solve_day6,
                  solve_day7,
                  solve_day8,
                  solve_day9,
                  solve_day10,
                  solve_day11,
                  solve_day12,
                  solve_day13,
                  solve_day14)

function_map = {
     1: solve_day1,
     2: solve_day2,
     3: solve_day3,
     4: solve_day4,
     5: solve_day5,
     6: solve_day6,
     7: solve_day7,
     8: solve_day8,
     9: solve_day9,
    10: solve_day10,
    11: solve_day11,
    12: solve_day12,
    13: solve_day13,
    14: solve_day14
}

def find_solution(day: int, *args, **kwargs):
    if day in function_map:
        return function_map[day](*args, **kwargs)
    else:
        print(f"Day {day} is either unsupported or unsolved as of now. Try again later!")

current_dir = os.path.dirname(__file__)

print("------------------------------------------------------------------------")
print("Welcome to the Advent of Code 2024 solver!")
print("Type 'quit' if you want to exit the application.")

while True:
    inp = input("Please enter the day (int) you would like to find the solution for:\n------------------------------------------------------------------------\n ")

    if inp.lower() == 'quit':
        break 

    inp_int = int(inp)
    inp = inp.strip()

    if len(inp) == 1: 
        inp = "0" + inp

    input_path = os.path.join(current_dir, "days", f"day{inp}", "input.txt")

    print(f"Printing the solutions for day{inp}")

    if inp_int == 14:
        show_tree_inp = input("Do you want to see the easter egg? y/n ")
        if show_tree_inp.strip().lower() == "y":
            show_tree_inp = True 
        elif show_tree_inp.strip().lower() == "n":
            show_tree_inp = False

        find_solution(inp_int, input_path, show_tree = show_tree_inp)
    else:
        find_solution(inp_int, input_path)

    user_inp = input("Press 'Enter' to choose a new day \nor type 'quit' to exit the application. \n")
    if user_inp.lower() == 'quit':
        break