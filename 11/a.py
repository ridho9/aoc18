def fuel_cell(x, y, serial):
    r_id = x + 10
    p = r_id * y + serial
    p *= r_id
    p = (p // 100) % 10 - 5
    return p


serial = 3613
grid = {}
for i in range(1, 301):
    for j in range(1, 301):
        grid[(i, j)] = fuel_cell(i, j, serial)

c_max = 0
p_max = -1
# size = 3
for size in range(1, 101):
    print(size)
    for i in range(1, 300 - size + 1):
        for j in range(1, 300 - size + 1):
            p_tot = 0
            for a in range(size):
                for b in range(size):
                    p_tot += grid[(i + a, j + b)]
            if p_tot > p_max:
                c_max = (i, j, size)
                p_max = p_tot
                print(c_max, p_max)
