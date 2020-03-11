from tkinter import *

window = Tk()
window.title("Timetable Generation OS Project")


def set_values():
    list_1 = [label3_1.get(), label3_2.get(), label3_3.get(), label3_4.get()]
    list_2 = [label4_1.get(), label4_2.get(), label4_3.get(), label4_4.get()]
    list_3 = [label5_1.get(), label5_2.get(), label5_3.get(), label5_4.get()]
    list_4 = [label6_1.get(), label6_2.get(), label6_3.get(), label6_4.get()]



text1 = Label(window, text="Enter the faculty hours required for each branch")

text2 = Label(window, text="Branch Name")
text2_1 = Label(window, text="Faculty 1")
text2_2 = Label(window, text="Faculty 2")
text2_3 = Label(window, text="Faculty 3")
text2_4 = Label(window, text="Faculty 4")

text1.grid(row=0)


text3 = Label(window, text="B.Tech CS")
label3_1 = Entry(window)
label3_2 = Entry(window)
label3_3 = Entry(window)
label3_4 = Entry(window)


text2.grid(row=1, column=0)
text2_1.grid(row=1, column=1)
text2_2.grid(row=1, column=2)
text2_3.grid(row=1, column=3)
text2_4.grid(row=1, column=4)


text3.grid(row=2, column=0)
label3_1.grid(row=2, column=1)
label3_2.grid(row=2, column=2)
label3_3.grid(row=2, column=3)
label3_4.grid(row=2, column=4)


text4 = Label(window, text="B.Tech IT")
label4_1 = Entry(window)
label4_2 = Entry(window)
label4_3 = Entry(window)
label4_4 = Entry(window)
text4.grid(row=3, column=0)
label4_1.grid(row=3, column=1)
label4_2.grid(row=3, column=2)
label4_3.grid(row=3, column=3)
label4_4.grid(row=3, column=4)

text5 = Label(window, text="MBA.Tech CS")
label5_1 = Entry(window)
label5_2 = Entry(window)
label5_3 = Entry(window)
label5_4 = Entry(window)
text5.grid(row=4, column=0)
label5_1.grid(row=4, column=1)
label5_2.grid(row=4, column=2)
label5_3.grid(row=4, column=3)
label5_4.grid(row=4, column=4)

text6 = Label(window, text="MBA.Tech IT")
label6_1 = Entry(window)
label6_2 = Entry(window)
label6_3 = Entry(window)
label6_4 = Entry(window)
text6.grid(row=5, column=0)
label6_1.grid(row=5, column=1)
label6_2.grid(row=5, column=2)
label6_3.grid(row=5, column=3)
label6_4.grid(row=5, column=4)

button1 = Button(window, text="Submit Request", command = set_values)
button1.grid(row=6, column=2)

window.mainloop()


