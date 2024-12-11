import numpy as np 
from tqdm import tqdm

def solve_day10(input):
    with open(input, "r") as file:
        data = file.readlines()
        data = [x.replace("\n", "") for x in data]

    trail = np.empty((len(data), len(data[0])), dtype = int)
    for i in range(len(data)):
        for j in range(len(data[0])):
            trail[i,j] = int(data[i][j])

    trailheads = np.argwhere(trail == 0)
    trailheads = [tuple(x) for x in trailheads]

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    def within_bounds(arr, indx, indy):
        return indx >= 0 and indx < arr.shape[0] and indy >= 0 and indy < arr.shape[1]

    a1 = 0 
    for trailhead in trailheads:
        visited_nines = []
        trail_score = 0
        queue = [trailhead]
        while queue:
            cur_place = queue.pop(0)
            for x,y in dirs:
                new_dir = (cur_place[0] + x, cur_place[1] + y)
                if within_bounds(trail, new_dir[0], new_dir[1]) and trail[new_dir] - trail[cur_place] == 1:
                    if trail[new_dir] == 9 and new_dir not in visited_nines:
                        trail_score += 1 
                        visited_nines.append(new_dir)
                    else:
                        queue.append(new_dir)
                    
        a1 += trail_score 

    print("Answer to subquestion 1 a10: ", a1)


    a2 = 0 
    for trailhead in trailheads:
        visited_nines = []
        trail_score = 0
        queue = [trailhead]
        while queue:
            cur_place = queue.pop(0)
            for x,y in dirs:
                new_dir = (cur_place[0] + x, cur_place[1] + y)
                if within_bounds(trail, new_dir[0], new_dir[1]) and trail[new_dir] - trail[cur_place] == 1:
                    if trail[new_dir] == 9:
                        trail_score += 1 
                        visited_nines.append(new_dir)
                    else:
                        queue.append(new_dir)
                    
        a2 += trail_score 

    print("Answer to subquesiton 2 a10: ", a2)

if __name__ == "__main__":
    solve_day10("input.txt")