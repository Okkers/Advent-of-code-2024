
def solve_day3(input):
    import re 
    from functools import reduce

    with open(input, "r") as file:
        data = "".join(file.readlines())

    valid_muls = re.findall(r"mul\([0-9]+,[0-9]+\)", data)

    a1 = 0 
    for mul in valid_muls:
        n1, n2 = mul.split(",")
        n1 = n1[4:]
        n2 = n2[:len(n2)-1]
        
        a1 += int(n1) * int(n2)

    print("Answer to subquestion 1 a3: ", a1)

    do_indices = re.finditer(r"do\(\)", data)
    do_indices = reduce(lambda x, y: x + [y.start()], do_indices, [])
    do_indices.insert(0,0)
    dont_indices = re.finditer(r"don\'t\(\)", data)
    dont_indices = reduce(lambda x, y: x + [y.start()], dont_indices, [])

    valid_mul_indices = []
    check = 0 

    threshold = max(max(do_indices), max(dont_indices))

    while check <= threshold:
        if not do_indices:
            break 
        if not dont_indices:
            break

        if min(do_indices) < min(dont_indices):
            if check != min(dont_indices):
                valid_mul_indices.append([check, min(dont_indices)])
            check = min(dont_indices)
            do_indices.remove(min(do_indices))

        else:
            check = min(do_indices)
            dont_indices.remove(min(dont_indices))


    valid_mul_indices.append([17731, len(data)])

    a2 = 0
    for mul_min, mul_max in valid_mul_indices:
        sliced = data[mul_min:mul_max]
        valid_sliced_muls = re.findall(r"mul\([0-9]+,[0-9]+\)", sliced)

        a1 = 0 
        for mul in valid_sliced_muls:
            n1, n2 = mul.split(",")
            n1 = n1[4:]
            n2 = n2[:len(n2)-1]
            
            a1 += int(n1) * int(n2)

        a2 += a1

        
    print("Answer to subquestion 2 a3: ", a2)

if __name__ == "__main__":
    solve_day3("input.txt")