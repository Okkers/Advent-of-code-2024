def solve_day11(input):
    with open(input, "r") as file:
        data = file.readlines()
        data = data[0].split(" ")
        data = [int(x) for x in data]

    rocks_a1 = data 

    def blink(rocks):
        out = []
        for rock in rocks:
            if rock == 0:
                out.append(1)
            elif len(str(rock)) % 2 == 0:
                rock = str(rock)
                left = rock[:len(rock)//2]
                right = rock[len(rock)//2:]
                out.append(int(left))
                out.append(int(right))
            else:
                out.append(rock*2024)


        return out 

    for _ in range(25):
        rocks_a1 = blink(rocks_a1)


    print("Answer to subquestion 1 a11: ", len(rocks_a1))

    memoize = {}

    def blink_rock(rock, blinks):
        if blinks == 0:
            return 1 
        elif (rock, blinks) in memoize:
            return memoize[(rock, blinks)]
        elif rock == 0:
            val = blink_rock(1, blinks-1)
        elif len(str(rock)) % 2 ==  0:
            rock = str(rock)
            left = rock[:len(rock) // 2]
            right = rock[len(rock) // 2:]

            val = blink_rock(int(left), blinks-1) + blink_rock(int(right), blinks-1)
        else:
            val = blink_rock(rock * 2024, blinks-1)

        memoize[(rock, blinks)] = val 
        return val 

    a2 = sum([blink_rock(x, 75) for x in data])
    print("Answer to subquestion 2 a11: ", a2)

if __name__ == "__main__":
    solve_day11("input.txt")