from req_to_all_list import to_alloc

faculty_list = [[[[-1, -1, -1, -1]] * 5] * 8]         # [Hour of Day][Day of Week][Faculty]

for hour in range(0, 8):
    for day in range(0, 5):
        for faculty in range(0, 4):
            print(faculty_list[hour][day])

mylist = [0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3]
fac_list_1 = to_alloc(mylist)
fac_list_2 = to_alloc(mylist)
fac_list_3 = to_alloc(mylist)
fac_list_4 = to_alloc(mylist)

for hour in range(0, 8):
    for day in range(0, 5):
        if len(fac_list_1) != 0:
            faculty_list[hour][day][0] = fac_list_1[0]
            fac_list_1.pop(0)

        if len(fac_list_2) != 0:
            faculty_list[hour][day][1] = fac_list_2[0]
            fac_list_2.pop(0)

        if len(fac_list_3) != 0:
            faculty_list[hour][day][2] = fac_list_3[0]
            fac_list_3.pop(0)

        if len(fac_list_4) != 0:
            faculty_list[hour][day][3] = fac_list_4[0]
            fac_list_4.pop(0)


print(faculty_list)
