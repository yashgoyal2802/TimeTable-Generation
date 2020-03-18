from req_to_all_list import to_alloc

faculty_list_1 = [[[-1] * 4] * 5]      # [Hour of Day][Day of Week][Faculty]
faculty_list = faculty_list_1 * 8

for hour in range(0, 8):
    print(faculty_list[hour])


fac_list_1 = to_alloc([0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3])
fac_list_2 = to_alloc([0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3])
fac_list_3 = to_alloc([0, 0, 1, 2, 2, 2, 2, 2, 2, 3, 3])
fac_list_4 = to_alloc([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3])

print(fac_list_1)
print(fac_list_2)
print(fac_list_3)
print(fac_list_4)

flag = 0

for hour in range(0, 8):
    if flag == 1:
        break
    for day in range(0, 5):
        if len(fac_list_1) == 0 and len(fac_list_2) == 0 and len(fac_list_3) == 0 and len(fac_list_4) == 0:
            print("Breaking FREE")
            flag = 1
            break
        if len(fac_list_1) > 0:
            print(f'Day {day+1} Hour {hour+8}')
            faculty_list[hour][day][0] = fac_list_1[0]
            fac_list_1.pop(0)

        if len(fac_list_2) > 0:
            faculty_list[hour][day][1] = fac_list_2[0]
            fac_list_2.pop(0)

        if len(fac_list_3) > 0:
            faculty_list[hour][day][2] = fac_list_3[0]
            fac_list_3.pop(0)

        if len(fac_list_4) > 0:
            faculty_list[hour][day][3] = fac_list_4[0]
            fac_list_4.pop(0)

for hour in range(0, 8):
    print(faculty_list[hour])
