#import openpyxl
from null_list import is_list_null
faculty_list = {0: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8],  # f1             # Semaphore of Faculty       # [0-3][0-4][0-7]   # [Faculty] [Day] [Hour]
                1: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8],  # f2
                2: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8],  # f3
                3: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8]}  # f4

batch_list = {0: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8],   # BTech CS        # Semaphore of Batch       # [0-3][0-4][0-7]      # [Batch] [Day] [Hour]
              1: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8],   # BTech IT
              2: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8],   # MBA Tech CS
              3: [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8]}   # MBA Tech IT

days_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}

req_hrs_dict = {'BTech CS': [0, 2, 3, 4], 'BTech IT': [2, 3, 4, 0], 'MBA Tech CS': [2, 4, 5, 6], 'MBA Tech IT': [1, 3, 0, 2]}  #Required Hours for each Batch/Week

rem_hrs_dict = {0: [0, 2, 2, 1], 1: [2, 2, 1, 0], 2: [1, 2, 1, 0], 3: [1, 3, 0, 2]}  #Reamaining Hours to be allocated

counter_keep = 0
temp1 = faculty_list
temp2 = batch_list

while not is_list_null(rem_hrs_dict):
    for faculty in range(0, 4):
        for batch in range(0, 4):

            if rem_hrs_dict[batch][faculty] != 0:

                for day in range(0, 5):
                    for hour in range(0, 8):
                        if faculty_list[faculty][day][hour] == 0 and batch_list[batch][day][hour] == 0:
                            batch_list[batch][day][hour] = 1
                            faculty_list[faculty][day][hour] = 1
                            print(f"{faculty} allocated to {batch} on {days_dict[day]} day from {hour}")
                            counter_keep += 1
                            print(faculty_list)
                            print(batch_list)
                            break

                        if counter_keep > 75000:
                            break




print("Finished")



