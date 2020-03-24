from quantum_time_splitter import quantum_splitter

faculty_list = [[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]]     # [Hour of Day][Day of Week][Faculty]

# Initial Matrix
# for hour in range(0, 8):
#     print(faculty_list[hour])


fac_list_1 = quantum_splitter([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
fac_list_2 = quantum_splitter([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
fac_list_3 = quantum_splitter([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
fac_list_4 = quantum_splitter([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3])

print('============================   REQUIREMENT HOURS   ==================================')


print(fac_list_1)
print(fac_list_2)
print(fac_list_3)
print(fac_list_4)

flag = 0

print('==============================   ALLOCATED TIMETABLE   ================================')

for hour in range(0, 8):
    # if flag == 1:
    #     break
    for day in range(0, 5):
        # if len(fac_list_1) == 0 and len(fac_list_2) == 0 and len(fac_list_3) == 0 and len(fac_list_4) == 0:
        #     # print("Breaking FREE")
        #     flag = 1
        #     break

        semaphore_list = []

        if len(fac_list_1) > 0:
            try:
                for x in range(0, 4):
                    if fac_list_1[x] not in semaphore_list:
                        faculty_list[hour][day][0] = fac_list_1[x]
                        semaphore_list.append(fac_list_1[x])
                        fac_list_1.pop(x)
                        break
            except IndexError:
                pass

        if len(fac_list_2) > 0:
            try:
                for x in range(0, 4):
                    if fac_list_2[x] not in semaphore_list:
                        faculty_list[hour][day][1] = fac_list_2[x]
                        semaphore_list.append(fac_list_2[x])
                        fac_list_2.pop(x)
                        break
            except IndexError:
                pass

        if len(fac_list_3) > 0:
            try:
                for x in range(0, 4):
                    if fac_list_3[x] not in semaphore_list:
                        faculty_list[hour][day][2] = fac_list_3[x]
                        semaphore_list.append(fac_list_3[x])
                        fac_list_3.pop(x)
                        break
            except IndexError:
                pass

        if len(fac_list_4) > 0:
            try:
                for x in range(0, 4):
                    if fac_list_4[x] not in semaphore_list:
                        faculty_list[hour][day][3] = fac_list_4[x]
                        semaphore_list.append(fac_list_4[x])
                        fac_list_4.pop(x)
                        break
            except IndexError:
                pass


for hour in range(0, 8):
    print(faculty_list[hour])
