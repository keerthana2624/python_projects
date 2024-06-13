def initialize_grid(n, m):
    grid = []
    for i in range(n):
        r = []
        for j in range(m):
            r.append(0)
        grid.append(r)
    return grid