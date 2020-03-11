#import openpyxl

classrooms = [10, 20, 30, 40, 50]   #Possible Classroom
avl_classrooms = {10:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],  # Semaphore of Classroom
                  20:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],
                  30:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],
                  40:[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]}

faculty = {'f1':[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],  # Semaphore of Faculty
           'f2':[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],
           'f3':[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8],
           'f4':[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]}

req_hrs_dict = {'BTech CS':[0, 2, 3, 4], 'BTech IT':[2, 3, 4, 0], 'MBA Tech CS':[2,4,5,6]}  #Required Hours for each Batch/Week
rem_hrs_dict = {0:[0, 2, 3, 4], 1:[2, 3, 4, 0], 2:[2,4,5,6]}  #Reamaining Hours to be allocated


# Allocate Faculty then classroom for required hours for each batch
def allocate_faculty():
    for i in range(0, len(rem_hrs_dict)):
        pass



