import numpy as np

def solve_day1(input):
    data = np.genfromtxt(input, delimiter = " ")

    l1 = data[:, 0]
    l2 = data[:,len(data[0])-1]

    l1 = np.sort(l1)
    l2 = np.sort(l2)

    l3 = np.abs(l2 - l1) 

    a1 = sum(l3)

    num_of_occurences = np.bincount(l2.astype(int))

    a2 = sum([x * num_of_occurences[int(x)] if x in l2 else 0 for x in l1])

    print("Answer to subquestion 1 day 1: ",int(a1))
    print("Answer to subquestion 2 day 1: ", int(a2))

if __name__ == "__main__":
    solve_day1("input.txt")