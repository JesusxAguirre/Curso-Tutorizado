def create_box(m, n):  ## m and n positive integers
    
    return [[min([x+1, y+1, m-x, n-y]) for x in range(m)] for y in range(n)]

print(create_box(7, 8))