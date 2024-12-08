import numpy as np

def solve_day8(input):

    with open(input) as file:
        data = file.readlines()
        data = [x.replace("\n", "") for x in data]

    arr = np.empty((len(data), len(data[0])), dtype = str)

    for i in range(len(data)):
        for j in range(len(data[0])):
            arr[i,j] = data[i][j]

    frequency_pos = {}

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            val = arr[i,j]
            if val != ".":
                if val not in frequency_pos.keys():
                    frequency_pos[val] = [(i,j)]
                else:
                    frequency_pos[val].append((i,j))

    def within_bounds(arr, i, j):
        return i >= 0 and i < arr.shape[0] and j >= 0 and j < arr.shape[1]

    antinodes = []

    a1 = 0
    for key in frequency_pos.keys():
        poses = frequency_pos[key]
        if len(poses) == 1:
            continue 

        for i in range(len(poses)):
            for j in range(i+1, len(poses)):
                tower_1 = poses[i]
                tower_2 = poses[j]
                diff = (tower_2[0] - tower_1[0], tower_2[1] - tower_1[1])

                antinode1 = (tower_1[0] - diff[0], tower_1[1] - diff[1])
                antinode2 = (tower_2[0] + diff[0], tower_2[1] + diff[1])

                if within_bounds(arr, antinode1[0], antinode1[1]) and antinode1 not in antinodes:
                    a1 += 1 
                    antinodes.append(antinode1)

                if within_bounds(arr, antinode2[0], antinode2[1]) and antinode2 not in antinodes:
                    a1 += 1 
                    antinodes.append(antinode2)

    print("Answer to subquestion 1 a8: ", a1)


    antinodes = []

    a2 = 0 
    for key in frequency_pos.keys():
        poses = frequency_pos[key]
        if len(poses) == 1:
            continue 

        for i in range(len(poses)):
            for j in range(i+1, len(poses)):
                tower_1 = poses[i]
                tower_2 = poses[j]
                diff = (tower_2[0] - tower_1[0], tower_2[1] - tower_1[1])
                
                antinode1 = tower_1
                antinode2 = tower_2 

                while within_bounds(arr, antinode1[0], antinode1[1]):
                    if antinode1 not in antinodes:
                        a2 += 1
                        antinodes.append(antinode1)

                    antinode1 = (antinode1[0] - diff[0], antinode1[1] - diff[1])

                while within_bounds(arr, antinode2[0], antinode2[1]):
                    if antinode2 not in antinodes:
                        a2 += 1
                        antinodes.append(antinode2)
                    antinode2 = (antinode2[0] + diff[0], antinode2[1] + diff[1])

    print("Answer to subquestion 2 a8: ", a2)

if __name__ == "__main__":
    solve_day8("input.txt")