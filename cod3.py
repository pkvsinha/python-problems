# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def diagonal(i, j, k, l):
    return f'{i+1}{chr(ord(j)+1)}' == f'{k}{l}'

def horizontal(i, j, k, l):
    return i == k

def vertical(i, j, k, l):
    return j == l

def map_cells(top_left, bottom_right):
    row1 = int(top_left[:-1])
    col1 = top_left[-1:]
    row2 = int(bottom_right[:-1])
    col2 = bottom_right[-1:]
    if diagonal(row1, col1, row2, col2):
        return [top_left, f'{row1}{chr(ord(col1)+1)}', f'{row1+1}{col1}', bottom_right]
    elif horizontal(row1, col1, row2, col2):
        cells = [top_left]
        cell = top_left
        while cell != bottom_right:
            col1 = chr(ord(col1)+1)
            cell = f'{row1}{col1}'
            cells.append(cell)
        return cells
    elif vertical(row1, col1, row2, col2):
        cells = [top_left]
        cell = top_left
        while cell != bottom_right:
            row1 += 1
            cell = f'{row1}{col1}'
            cells.append(cell)
        return cells

def solution(N, S, T):
    # write your code in Python 3.6
    mat = [[None] * N for _ in range(N)]
    ships = []
    for pos in S.split(","):
        top_left, bottom_right = pos.split(' ')
        ships.append(map_cells(top_left, bottom_right))
    for pos in T.split(' '):
        i = int(pos[:-1]) - 1
        j = ord(pos[-1:])-ord('A')
        mat[i][j] = 'X'
    hits = 0
    sunks = 0
    for ship in ships:
        ship_hit_count = 0
        for ship_pos in ship:
            i = int(ship_pos[:-1]) - 1
            j = ord(ship_pos[-1:])-ord('A')
            if mat[i][j] == 'X':
                ship_hit_count += 1
        if ship_hit_count == len(ship):
            sunks += 1
        elif ship_hit_count > 0:
            hits += 1
    return f'{sunks},{hits}'

print(solution(12, '1A 2A,12A 12A', '12A'))