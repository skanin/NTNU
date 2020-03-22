weights = [[3, 6, 8, 6, 3], [7, 6, 5, 7, 3], [4, 10, 4, 1, 6], [10, 4, 3, 1, 2], [6, 1, 7, 3, 9]]


def cumulative(weights):
    rows, cols = len(weights), len(weights[0])
    new = weights
    for i in range(0, rows):
        for j in range(0, cols):
            if j == 0:
                new[i][j] += min(new[i][j] + new[i+1][j], new[i][j+1] + new[i+1][j])
            elif


print(cumulative(weights))
