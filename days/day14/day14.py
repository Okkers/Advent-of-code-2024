import numpy as np 
import re
import matplotlib.pyplot as plt 

def solve_day14(input, show_tree = False):

    with open(input, "r") as file:
        data = file.readlines()
        data = [x.replace("\n", "") for x in data]
        data = [[x[2:].split(",") for x in y.split(" ")] for y in data]

    m = 103 
    n = 101
    board = np.full((m,n), 0)

    elapse = 100
    for robot in data:
        init_x, init_y = [int(x) for x in robot[0]]
        vel_x, vel_y = [int(x) for x in robot[1]]

        final_x = (init_x + elapse*vel_x) % board.shape[1]
        final_y = (init_y + elapse*vel_y) % board.shape[0]

        board[final_y, final_x] += 1

    quadrants = []
    quadrants.append(board[:board.shape[0]//2, :board.shape[1]//2].sum())
    quadrants.append(board[:board.shape[0]//2, board.shape[1]//2 + 1:].sum())
    quadrants.append(board[(board.shape[0]//2) + 1:, :board.shape[1]//2].sum())
    quadrants.append(board[(board.shape[0]//2) +1:, (board.shape[1]//2) + 1:].sum())
    a1 = 1 
    for i in quadrants:
        a1 *= i

    print("Answer to subquestion 1 a14: ", a1)

    def parse(file):
        pattern = re.compile(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)')
        with open(file, 'r') as f:
            matches = pattern.findall(f.read())
        data = np.array(matches, dtype=int)
        return data[:, :2], data[:, 2:]

    def simulate(pos, vel, w, h, sec):
        return (pos + vel * sec) % [w, h]

    def calc_entropy(pos, w, h):
        grid = np.zeros((h, w), dtype=int)
        np.add.at(grid, (pos[:,1], pos[:,0]), 1)
        counts = np.bincount(grid.flatten())
        probs = counts[counts > 0] / counts.sum()
        entropy = -np.sum(probs * np.log2(probs))
        return entropy

    def find_pattern_sec(pos, vel, w, h, max_sec=10000):
        min_sec, min_ent = None, float('inf')
        for sec in range(1, max_sec + 1):
            curr_pos = simulate(pos, vel, w, h, sec)
            ent = calc_entropy(curr_pos, w, h)
            if ent < min_ent:
                min_ent, min_sec = ent, sec
        return min_sec

    pos, vel = parse(input)
    w, h = 101, 103

    a2 = find_pattern_sec(pos, vel, w, h)

    print("answer to subquestion 2 a14: ", a2 )

    if show_tree:
        m = 103 
        n = 101
        board = np.full((m,n), 0)

        elapse = a2
        for robot in data:
            init_x, init_y = [int(x) for x in robot[0]]
            vel_x, vel_y = [int(x) for x in robot[1]]

            final_x = (init_x + elapse*vel_x) % board.shape[1]
            final_y = (init_y + elapse*vel_y) % board.shape[0]

            board[final_y, final_x] += 1

        plt.imshow(board)
        plt.show()

if __name__ == "__main__":
    solve_day14("input.txt", show_tree=True)