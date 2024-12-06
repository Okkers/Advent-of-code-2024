def solve_day4(input):

    import numpy as np 

    with open(input, "r") as file:
        data = file.readlines()
        data = [line.replace("\n", "") for line in data]

    word_search = np.empty((len(data), len(data[0])), dtype = str)

    for x in range(len(data)):
        for y in range(len(data[0])):
            word_search[x,y] = data[x][y]

    potential_words = [[(0,0), (0,1), (0,2), (0,3)], 
                    [(0,0), (1,0), (2,0), (3,0)], 
                    [(0,0), (0,-1), (0,-2), (0,-3)],
                    [(0,0), (-1,0), (-2,0), (-3,0)],
                    [(0,0), (1,1), (2,2), (3,3)],
                    [(0,0), (1,-1), (2,-2), (3,-3)],
                    [(0,0), (-1,1), (-2,2), (-3,3)],
                    [(0,0), (-1,-1), (-2,-2), (-3,-3)]]

    def within_bounds(arr, index):
        x = index[0]
        y = index[1]

        return x >= 0 and x < arr.shape[0] and y >= 0 and y < arr.shape[1]

    xmas = "XMAS"

    a1 = 0
    for i in range(140):
        for j in range(140):
            for pot_word in potential_words:
                is_word = True
                new_word_count = 0

                for indx, coords in enumerate(pot_word): 
                    if within_bounds(word_search, (i+coords[0], j+coords[1])):
                        if word_search[i+coords[0], j+coords[1]] != xmas[indx]:
                            is_word = False 

                    else:
                        is_word = False

                if is_word and new_word_count != 4:
                    a1 += 1

    print("Answer to subquestion 1 a4: ", a1)

    indices_for_mas = [(0,0), (-1,-1), (1,1), (1,-1), (-1,1)]
    mas_words = ["AMSMS", "ASMSM", "AMSSM", "ASMMS"]

    a2 = 0
    for i in range(140):
        for j in range(140):
            word = ""
            for x,y in indices_for_mas:
                if within_bounds(word_search, (i+x, j+y)):
                    word += word_search[i+x, j+y]
            if len(word) == 5:
                if word in mas_words:
                    a2 += 1

    print("Answer to subquestion 2 a4: ", a2)

if __name__ == "__main__":
    solve_day4("input.txt")