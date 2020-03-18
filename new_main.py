faculty_list = [[[[0, 0, 0, 0]] * 5] * 8]         # [Hour of Day][Day of Week][Faculty]


for hour in range(0, 8):
    for day in range(0, 5):
        for faculty in range(0, 4):
            print(f"Hour: {hour} Day: {day} Faculty: {faculty}")

        print("\n")
