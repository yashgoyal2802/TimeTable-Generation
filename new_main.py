faculty_list = [[[[0, 0, 0, 0]] * 5] * 8]         # [Hour of Day][Day of Week][Faculty]

req_hrs_dict = {'BTech CS': [0, 2, 3, 4], 'BTech IT': [2, 3, 4, 0], 'MBA Tech CS': [2, 4, 5, 6], 'MBA Tech IT': [1, 3, 0, 2]}  #Required Hours for each Batch/Week

rem_hrs_dict = {0: [0, 2, 2, 1], 1: [2, 2, 1, 0], 2: [1, 2, 1, 0], 3: [1, 3, 0, 2]}  #Reamaining Hours to be allocated


for hour in range(0, 8):
    for day in range(0, 5):
        for faculty in range(0, 4):
            print(f"Hour: {hour} Day: {day} Faculty: {faculty}")

        print("\n")
