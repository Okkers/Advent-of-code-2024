import numpy as np 
from tqdm import tqdm 

def solve_day12(input):
    with open(input, "r") as file:
        data = file.readlines()
        data = [x.replace("\n", "") for x in data]

    field = np.empty((len(data), len(data[0])), dtype = str)

    for i in range(len(data)):
        for j in range(len(data[0])):
            field[i,j] = data[i][j]

    areas = []
    visited_squares = []

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    def within_bounds(arr, i, j):
        return i >= 0 and i < arr.shape[0] and j >= 0 and j < arr.shape[1]

    for i in tqdm(range(field.shape[0])):
        for j in range(field.shape[1]):
            queue = [(i,j, field[i,j])]
            field_area = 0
            field_perimeter = 0
            while queue:
                indx, indy, val = queue.pop(0)
                if (indx, indy) in visited_squares:
                    continue

                field_area += 1

                visited_squares.append((indx, indy))
                n_neighbors = 0 
                for x,y in dirs: 
                    new_x = indx + x 
                    new_y = indy + y 
                    if within_bounds(field, new_x, new_y):
                        if field[new_x, new_y] == val:
                            n_neighbors += 1 
                            queue.append((new_x, new_y, field[new_x, new_y]))
                field_perimeter += 4 - n_neighbors

            areas.append((field_area, field_perimeter))

    a1 = sum([x*y for x,y in areas])

    print("Answer to subquestion 1 a12: ", a1)

    areas = []
    visited_squares = []

    dirs_2 = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

    for i in tqdm(range(field.shape[0])):
        for j in range(field.shape[1]):
            queue = [(i,j, field[i,j])]
            field_area = 0
            field_perimeter = 0
            field_num_sides = 0
            while queue:
                indx, indy, val = queue.pop(0)
                if (indx, indy) in visited_squares:
                    continue

                field_area += 1

                visited_squares.append((indx, indy))
                neighbors = []
                for x,y in dirs_2: 
                    new_x = indx + x 
                    new_y = indy + y 
                    if within_bounds(field, new_x, new_y):
                        if field[new_x, new_y] == val:
                            neighbors.append((x,y))
                            if(x,y) in dirs:
                                queue.append((new_x, new_y, field[new_x, new_y]))

                if (0,1) not in neighbors and (1,0) not in neighbors and (0,-1) not in neighbors and (-1,0) not in neighbors:
                    n_corners = 4
                elif (1,0) in neighbors and (0,1) in neighbors and (-1,0) in neighbors and (0,-1) in neighbors:
                    n_corners = 4 
                    if (-1,-1) in neighbors:
                        n_corners -= 1
                    if (-1,1) in neighbors:
                        n_corners -= 1
                    if (1,1) in neighbors:
                        n_corners -= 1
                    if (1,-1) in neighbors:
                        n_corners -= 1 
                elif (-1,0) in neighbors and (0,-1) in neighbors and (0,1) in neighbors:
                    n_corners = 2
                    if (-1,-1) in neighbors:
                        n_corners -= 1 
                    if (-1,1) in neighbors:
                        n_corners -= 1
                elif(-1,0) in neighbors and (0,1) in neighbors and (1,0) in neighbors:
                    n_corners = 2
                    if (-1,1) in neighbors:
                        n_corners -= 1
                    if (1,1) in neighbors:
                        n_corners -= 1
                elif (-1,0) in neighbors and (1,0) in neighbors and (0,-1) in neighbors:
                    n_corners = 2
                    if (-1,-1) in neighbors:
                        n_corners -= 1 
                    if (1,-1) in neighbors:
                        n_corners -= 1 
                elif(0,-1) in neighbors and (0,1) in neighbors and (1,0) in neighbors:
                    n_corners = 2 
                    if (1,-1) in neighbors:
                        n_corners -= 1
                    if (1,1) in neighbors:
                        n_corners -= 1 
                elif (0,1) in neighbors and (0,-1) in neighbors:
                    n_corners = 0
                elif (1,0) in neighbors and (-1,0) in neighbors:
                    n_corners = 0
                elif (-1,0) in neighbors and (0,-1) in neighbors:
                    n_corners = 2
                    if (-1,-1) in neighbors:
                        n_corners -= 1
                elif (-1,0) in neighbors and (0,1) in neighbors:
                    n_corners = 2 
                    if (-1,1) in neighbors:
                        n_corners -= 1
                elif (1,0) in neighbors and (0,1) in neighbors:
                    n_corners = 2 
                    if (1,1) in neighbors:
                        n_corners -= 1
                elif (0,-1) in neighbors and (1,0) in neighbors:
                    n_corners = 2 
                    if (1,-1) in neighbors:
                        n_corners -= 1
                else:
                    n_corners = 2 

                field_num_sides += n_corners

            areas.append((field_area, field_num_sides))

    a2 = sum([x*y for x,y in areas])

    print("Answer to subquestion 2 a12: ", a2)

if __name__ == "__main__":
    solve_day12("input.txt")