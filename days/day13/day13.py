from collections import namedtuple
import re

def solve_day13(input):
    with open(input) as file:
        data= file.readlines()
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    Claw = namedtuple('Claw', ['button_a', 'button_b', 'prize'])
    claws = []
    for i in range(0, len(lines)//4 + 1):
        a = tuple([int(x) for x in re.findall('\d+', lines[i*4])])
        b = tuple([int(x) for x in re.findall('\d+', lines[i*4+1])])
        p = tuple([int(x) for x in re.findall('\d+', lines[i*4+2])])
        claws.append(Claw(a, b, p))

    buttons = []
    init_a = []
    for line in data:
        if line == "\n":
            buttons.append(init_a)
            init_a = []
        else:
            init_a.append(line)

    a1 = 0
    for button in buttons:
        button_a = button[0].replace("\n", "").split(":")[1].split(",")
        button_b = button[1].replace("\n", "").split(":")[1].split(",")
        prize = button[2].replace("\n", "").split(":")[1].split(",")

        button_a = [[x for x in y if x.isdigit()] for y in button_a]
        button_b = [[x for x in y if x.isdigit()] for y in button_b]
        prize = [[x for x in y if x.isdigit()] for y in prize]

        button_a = [int("".join(x)) for x in button_a]
        button_b = [int("".join(x)) for x in button_b]
        prize = [int("".join(x)) for x in prize]

        A = (prize[0]*button_b[1] - prize[1] * button_b[0]) // (button_a[0] * button_b[1] - button_a[1] * button_b[0])
        B = (button_a[0] * prize[1] - button_a[1] * prize[0]) // (button_a[0] * button_b[1] - button_a[1] * button_b[0])

        if ((button_a[0] * A + button_b[0] * B) == prize[0]) and ((button_a[1] * A + button_b[1] * B) == prize[1]):
            a1 += 3*A + B

    print("Answer to subquestion 1 a13: ", a1)

    a2 = 0
    for this_claw in claws:
        ax, ay = this_claw.button_a
        bx, by = this_claw.button_b
        px, py = this_claw.prize
        px += 10000000000000
        py += 10000000000000
        solution_a, solution_b = None, None     
        if (bx * py - by * px) / (bx * ay - by * ax) == (bx * py - by * px) // (bx * ay - by * ax):
            solution_a = (bx * py - by * px) // (bx * ay - by * ax)
            if (py - solution_a * ay) / by == (py - solution_a * ay) // by:
                solution_b = (py - solution_a * ay) // by
        if solution_a is not None and solution_b is not None:
            a2 += solution_a * 3 + solution_b

    print("Answer to subquestion 2 a13: ", a2)

if __name__ == "__main__":
    solve_day13("input.txt")