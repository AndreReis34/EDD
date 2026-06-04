from functions import isSafe

def orangeRot01(mat):
    n = len(mat)
    m = len(mat[0])

    changed = False

    elapsedTime = 0

    directions = [[1,0], [0,1], [-1,0], [0,-1]]

    while True:
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    for di in directions:
                        x = i + di[0]
                        y = j + di[1]

                        if isSafe(x, y, n, m) and mat[x][y] == 1:
                            mat[x][y] = 2
                            changed = True

        if not changed:
            break

        changed = False
        elapsedTime += 1 

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                return -1

    return elapsedTime




def dfs(mat, i, j, time):
    n = len(mat)
    m = len(mat[0])

    # update minimum time
    mat[i][j] = time

    # all four directions
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # change 4-directionally connected cells
    for dir in directions:
        x = i + dir[0]
        y = j + dir[1]

        # if cell is in the matrix and
        # the orange is fresh
        if isSafe(x, y, n, m) and (mat[x][y] == 1 or mat[x][y] > time + 1):
            dfs(mat, x, y, time + 1)


def orangeRot02(mat):
    n = len(mat)
    m = len(mat[0])

    # counter of elapsed time
    elapsedTime = 0

    # iterate through all the cells
    for i in range(n):
        for j in range(m):

            # if orange is initially rotten
            if mat[i][j] == 2:
                dfs(mat, i, j, 2)

    # iterate through all the cells
    for i in range(n):
        for j in range(m):

            # if orange is fresh
            if mat[i][j] == 1:
                return -1

            # update the maximum time
            elapsedTime = max(elapsedTime, mat[i][j] - 2)

    return elapsedTime


