def solve_day2(input):
    with open(input, "r") as file:
        data = file.readlines()

    cleaned = []

    for line in data:
        if "\n" in line: 
            line = line.replace("\n", "")
        
        line = [int(x) for x in line.split(" ")]
        cleaned.append(line)

    def find_true_reports(cleaned, question):
        true_reps = 0

        for report in cleaned: 
            for remove_indx in range(len(report)+1):
                diffs = []
                diff_with_removed_val = report.copy()

                if question == 2:
                    if remove_indx != 0:    
                        diff_with_removed_val.pop(remove_indx-1)

                is_increasing = False 
                is_decreasing = False 
                is_in_range = True

                for x in range(1, len(diff_with_removed_val)):
                    diffs.append(diff_with_removed_val[x]-diff_with_removed_val[x-1])

                    if diff_with_removed_val[x] > diff_with_removed_val[x-1]:
                        is_increasing = True 
                    if diff_with_removed_val[x] < diff_with_removed_val[x-1]:
                        is_decreasing = True 


                    if abs(diff_with_removed_val[x] - diff_with_removed_val[x-1]) not in [1,2,3]:
                        is_in_range = False

                if is_decreasing and is_increasing:
                    continue 

                if not is_in_range:
                    continue 

                true_reps += 1
                break

        return true_reps

    print("Answer to subquestion 1 day2: ", find_true_reports(cleaned, 1))
    print("Answer to subquestion 2 day2: ", find_true_reports(cleaned, 2))

if __name__ == "__main__":
    solve_day2("input.txt")