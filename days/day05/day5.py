def solve_day5(input):    
    with open(input, "r") as file:
        data = file.readlines()

    page_break = data.index("\n")

    ordering_rules = data[:page_break]
    updates = data[page_break+1:]

    ordering_rules = [[int(y) for y in x.replace("\n", "").split("|")] for x in ordering_rules]
    updates = [[int(y) for y in x.replace("\n", "").split(",")] for x in updates]

    a1 = 0
    a2 = 0
    for list in updates:
        all_rules = []
        for i in range(len(list)):
            cur_order_rules  = [x for x in ordering_rules if list[i] in x]
            valid_order_rules = []

            for order_rule in cur_order_rules:
                plc = order_rule
                if plc[0] == list[i]:
                    if plc[1] in list:
                        valid_order_rules.append(order_rule)
                if plc[1] == list[i]:
                    if plc[0] in list:
                        valid_order_rules.append(order_rule)

            all_rules.append(valid_order_rules)

        all_rules = [x for y in all_rules for x in y]
        is_valid_list = True

        for first_val, second_val in all_rules: 
            if list.index(second_val) < list.index(first_val):
                is_valid_list = False 
                break

        if is_valid_list: 
            a1 += list[len(list)//2]

        else:
            sorted_list = []

            while list:
                first_val = [x for x in list if x not in [y[1] for y in all_rules]]
                last_val = [x for x in list if x not in [y[0] for y in all_rules]]

                if first_val:
                    list.remove(first_val[0])
                    sorted_list.append(first_val[0])

                    all_rules = [x for x in all_rules if first_val[0] not in x]

                elif last_val:
                    list.remove(last_val[0])
                    sorted_list.insert(len(sorted_list)-1, last_val[0])

                    for indx, rule in enumerate(all_rules):
                        if last_val[0] in rule:
                            all_rules.pop(indx)

            a2 += sorted_list[len(sorted_list)//2]

    print("Answer to subquestion 1 a5: ", a1)
    print("Answer to subquestion 2 a5: ", a2)

if __name__ == "__main__":
    solve_day5("input.txt")