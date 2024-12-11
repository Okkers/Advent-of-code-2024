from tqdm import tqdm
def solve_day9(input):
    with open(input, "r") as file:
        data = file.readlines()

    ID = 0
    out = []

    for indx, num in enumerate(data[0]):
        if indx % 2 == 0:
            for i in range(int(num)):
                out.append(str(ID))

            ID += 1 
        else:
            for i in range(int(num)):
                out.append(".")

    dot_occ = out.index(".")
    cur_val = len(out)-1 

    while cur_val > dot_occ:
        if out[cur_val].isdigit():
            out[dot_occ] = out[cur_val]
            out[cur_val] = "."
            dot_occ = out.index(".")
            cur_val -= 1 

        else:
            cur_val -= 1

    out = [x for x in out if x.isdigit()]

    a1 = sum([int(x) * int(y) for x,y in zip(out, range(len(out)))])

    print("Answer to subquestion 1 a9: ", a1)

    ID = 0
    out = []

    for indx, num in enumerate(data[0]):
        if indx % 2 == 0:
            block = []
            for i in range(int(num)):
                block.append(str(ID))
            out.append(block)

            ID += 1 
        else:
            block = []
            for i in range(int(num)):
                block.append(".")
            out.append(block)

    for file_id in tqdm(range(ID -1, -1, -1)):
        # print(file_id)
        lst = [x for x in out if str(file_id) in x]
        if len(lst) == 0:
            break 
        lst = lst[0]
        plc = out.index(lst)
        file_size = len(lst)
        # print(plc)
        # print(lst)

        target_start = -1 
        for i in range(len(out) - file_size + 1):
            if "." in out[i] and len(out[i]) >= file_size:
                target_start = i 
                break

        if target_start != -1:
            if target_start > plc:
                continue
            for indx, val in enumerate(lst):
                out[target_start][indx] = val 
                out[plc][indx] = "."

            new_dots = [x for x in out[target_start] if x == "."]
            out[target_start] = [x for x in out[target_start] if x != "."]
            out.insert(target_start+1, new_dots)

            pass

    out = [sublst for lst in out for sublst in lst]


    a2 = sum([int(x) * int(y) if x.isdigit() else 0 for x,y in zip(out, range(len(out)))])

    print("Answer to subquestion 2 a9: ", a2)

if __name__ == "__main__":
    solve_day9("input.txt")