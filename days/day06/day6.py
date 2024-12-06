import numpy as np 
from tqdm import tqdm 

def solve_day6(input):
    with open(input, "r") as file:
        data = file.readlines()
        data = [x.replace("\n", "") if "\n" in x else x for x in data]

    lab = np.empty((len(data), len(data[0])), dtype = str)
    walked_path = np.full(lab.shape, False)

    for i in range(len(data)):
        for j in range(len(data[0])):
            lab[i,j] = data[i][j]

    start = np.argwhere(lab == "^")[0]
    s_x, s_y = start

    def within_bounds(arr, indx):
        return indx[0] >= 0 and indx[0] < arr.shape[0] and indx[1] >= 0 and indx[1] < arr.shape[1]

    def flood_fill(lab, start):
        visited = np.full(lab.shape, False)
        stack = [tuple(start)]
        while stack:
            x, y = stack.pop()
            if visited[x, y]:
                continue
            visited[x, y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if within_bounds(lab, (nx, ny)) and not visited[nx, ny] and lab[nx, ny] != "#":
                    stack.append((nx, ny))
        return visited

    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    cur_dir = 0

    end = False

    while not end:
        walked_path[s_x, s_y] = True

        new_x = s_x + dirs[cur_dir][0]
        new_y = s_y + dirs[cur_dir][1]

        if within_bounds(lab, (new_x, new_y)):
            if lab[new_x, new_y] == "#":
                cur_dir = (cur_dir + 1) % 4 
                s_x = s_x + dirs[cur_dir][0]
                s_y = s_y + dirs[cur_dir][1]
            else:
                s_x = new_x 
                s_y = new_y

        else:
            end = True 

    a1 = sum(sum(walked_path))


    walked_path = flood_fill(lab, start)

    potential_obstructions = list(zip(*np.where(walked_path)))
    potential_obstructions.remove(tuple(start))

    num_of_obstructions = 0
    for potential_obstruction in tqdm(potential_obstructions, desc = "Loading ..."):
            plc_lab = lab.copy()
            plc_lab[potential_obstruction] = "#"

            visited_states = set()
            s_x, s_y = start 
            cur_dir = 0
            end = False 

            while not end:
                state = (s_x, s_y, cur_dir)

                if state in visited_states:
                    num_of_obstructions += 1
                    break

                visited_states.add(state)

                new_x = s_x + dirs[cur_dir][0]
                new_y = s_y + dirs[cur_dir][1]

                if within_bounds(plc_lab, (new_x, new_y)):
                    if plc_lab[new_x, new_y] == "#":
                        cur_dir = (cur_dir + 1) % 4 
                    else:
                        s_x = new_x 
                        s_y = new_y

                else:
                    end = True 

    print("Answer to subquestion 1 a6: ", a1)
    print("Answer to subquestion 2 a6: ", num_of_obstructions)
    return 

if __name__ == "__main__":
    solve_day6("input.txt")