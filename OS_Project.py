#import openpyxl

classrooms = [10, 20, 30, 40, 50]   #Possible Classroom
avl_classrooms = {10:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],  # Semaphore of Classroom
                  20:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],
                  30:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],
                  40:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]}

Monday = [[0]*8,[0]*8,[0]*8,[0]*8]]  # Semaphore of Faculty for Mon
Tuesday = [[0]*8,[0]*8,[0]*8,[0]*8]]  # Semaphore of Faculty for Tue
Wednesday = [[0]*8,[0]*8,[0]*8,[0]*8]]  # Semaphore of Faculty for Wed
Thursday = [[0]*8,[0]*8,[0]*8,[0]*8]]  # Semaphore of Faculty for Thur
Friday = [[0]*8,[0]*8,[0]*8,[0]*8]]  # Semaphore of Faculty for Fri

req_hrs_dict = {'BTech CS':[0, 2, 3, 4], 'BTech IT': [2, 3, 4, 0],
                'MBA Tech CS': [2, 4, 5, 6], 'BTech DS':[3,0,5,1]}  #Required Hours for each Batch/Week
rem_hrs_dict = [[0, 2, 3, 4],[2, 3, 4, 0],[2, 4, 5, 6],[3,0,5,1]]  #Reamaining Hours to be allocated


# Allocate Faculty then classroom for required hours for each batch
def allocate_faculty():
    for i in range(0, len(rem_hrs_dict)):
        for k,v in req_hrs_dict.values():
            for j in len(v):
                if v[j]>0:
                    if v[j]==1:
                        rem_hrs_dict[i][j]-=1
                        Monday[j][]




