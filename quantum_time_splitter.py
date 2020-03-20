
def quantum_splitter(mylist):
    w, x, y, z, = 0, 0, 0, 0

    for element in mylist:
        if element == 0:
            w += 1
        elif element == 1:
            x += 1
        elif element == 2:
            y += 1
        else:
            z += 1
    # print(f'0-{w}  1-{x}  2-{y}  3-{z}')
    final_list = []

    while w != 0 or x != 0 or y != 0 or z != 0:
        if w != 0:
            final_list.append(0)
            w -= 1

        if x != 0:
            final_list.append(1)
            x -= 1

        if y != 0:
            final_list.append(2)
            y -= 1

        if z != 0:
            final_list.append(3)
            z -= 1
    return final_list



