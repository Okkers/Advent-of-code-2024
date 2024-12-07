from itertools import product
from tqdm import tqdm

def solve_day7(input):
    with open(input) as file:
        data = file.readlines()
        data = [x.replace("\n", "") for x in  data]
        data = [x.split(":") for x in data]
        data = [[x[0], x[1].split(" ")[1:]] for x in data]

    operators = ["+", "*"]


    def evaluate_expression(vars, operation):
        result = vars[0] 
        for indx, op in enumerate(operation):
            if op == "+":
                result += vars[indx+1]
            elif op == "*":
                result *= vars[indx+1]
            elif op == "||":
                result = int(str(result) + str(vars[indx+1]))
        return result
            
    a1 = 0 
    for equation in tqdm(data):
        target, vars = equation
        target = int(target)
        vars = [int(x) for x in vars]
        if 1 not in vars:
            upper_bound_ops = ["*" for _ in range(len(vars)-1)]
            lower_bound_ops = ["+" for _ in range(len(vars)-1)]

            upper_bound = evaluate_expression(vars, upper_bound_ops)
            lower_bound = evaluate_expression(vars, lower_bound_ops)
            if target > upper_bound or target < lower_bound:
                continue

        ops = list(product(*[operators] * (len(vars)-1)))

        for pot_op in ops:
            result = evaluate_expression(vars, pot_op)

            if result == target:
                a1 += target
                break

    a2 = 0
    operators.append("||")
    for equation in tqdm(data):
        target, vars = equation 
        target = int(target)
        vars = [int(x) for x in vars]

        ops = list(product(*[operators] * (len(vars)-1)))

        for pot_op in ops:
            result = evaluate_expression(vars, pot_op)

            if result == target:
                a2 += target 
                break

    print("Answer to subquestion 1 a7: ", a1)
    print("Answer to subquestion 2 a7: ", a2)

if __name__ == "__main__":
    solve_day7("input.txt")