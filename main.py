import os 
from days import (solve_day1,
                  solve_day2,
                  solve_day3,
                  solve_day4,
                  solve_day5,
                  solve_day6)

function_map = {
    1: solve_day1,
    2: solve_day2,
    3: solve_day3,
    4: solve_day4,
    5: solve_day5,
    6: solve_day6
}

def find_solution(day: int, *args, **kwargs):
    if day in function_map:
        return function_map[day](*args, **kwargs)
    else:
        print(f"Day {day} is either unsupported or unsolved as of now. Try again later!")

current_dir = os.path.dirname(__file__)

print("------------------------------------------------------------------------")
print("Welcome to the Advent of Code 2024 solver!")
inp = input("Please enter the day (int) you would like to find the solution for:\n------------------------------------------------------------------------")

inp_int = int(inp)
inp = inp.strip()

if len(inp) == 1: 
    inp = "0" + inp

input_path = os.path.join(current_dir, "days", f"day{inp}", "input.txt")

print(f"Printing the solutions for day{inp}")

find_solution(inp_int, input_path)