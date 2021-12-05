def final_answer(board, number):
    sum = 0
    for row in board:
        for cell in row:
            if cell != 'x':
                sum += int(cell)
    return sum * int(number)


def find_winner(numbers, bingo_boards):
    # Loop through each number
    for n in numbers:
        # Loop through each board, mark it off and check if it's a winner
        for board in bingo_boards:
            for index, row in enumerate(board):
                board[index] = ["x" if cell == n else cell for cell in row]
            for i in range(5):
                solution = True
                for j in range(5):
                    if board[j][i] != "x":
                        solution = False
                if board[i].count("x") == 5:
                    solution = True
                if solution:
                    # Removing the board for the purposes of part 2
                    # So the last remaining board is the last winner
                    bingo_boards.remove(board)
                    return final_answer(board, n)
    return -1


with open("input.txt") as f:
    numbers = f.readline().strip().split(",")
    line = f.readline()
    bingo_boards = []
    while line:
        if line == "\n":
            bingo_boards.append([])
        else:
            bingo_boards[len(bingo_boards) - 1].append(line.strip().split())
        line = f.readline()

    # part 1
    ans = find_winner(numbers, bingo_boards)
    print(ans)

    # part 2
    while len(bingo_boards) > 0:
        ans = find_winner(numbers, bingo_boards)
    print(ans)
