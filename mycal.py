from tkinter import  *
root = Tk()
root.title("simple calculator")
e = Entry(width = 40,borderwidth = 5)
e.grid(row=0,column=0,columnspan= 3,padx = 10,pady = 10)
def badd(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))
    return
def b_cleark():
    e.delete(0,END)
def b_addition():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "addition"
    e.delete(0,END)
def b_equals():
    second_num = e.get()
    e.delete(0,END)
    global s_num

    s_num = int(second_num)
    if math == "addition":
        e.insert(0, f_num + s_num)
    elif math == "subraction":
        e.insert(0, f_num - s_num)
    elif math == "multiplication":
        e.insert(0, f_num * s_num)
    elif math == "division":
        e.insert(0, f_num / s_num)


def b_subs():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "subraction"
    e.delete(0, END)
def b_muls():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "multiplication"
    e.delete(0, END)
def b_divs():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "division"
    e.delete(0, END)
b0 = Button(root,text="0",padx= 40,pady=20,command=lambda : badd(0))
b1 = Button(root,text="1",padx= 40,pady=20,command=lambda : badd(1))
b2 = Button(root,text="2",padx= 40,pady=20,command=lambda : badd(2))
b3 = Button(root,text="3",padx= 40,pady=20,command=lambda : badd(3))
b4 = Button(root,text="4",padx= 40,pady=20,command=lambda : badd(4))
b5 = Button(root,text="5",padx= 40,pady=20,command=lambda : badd(5))
b6 = Button(root,text="6",padx= 40,pady=20,command=lambda : badd(6))
b7 = Button(root,text="7",padx= 40,pady=20,command=lambda : badd(7))
b8 = Button(root,text="8",padx= 40,pady=20,command=lambda : badd(8))
b9 = Button(root,text="9",padx= 40,pady=20,command=lambda : badd(9))
b_add = Button(root,text="+",padx= 40,pady=20,command= b_addition)
b_equal = Button(root,text="=",padx= 85,pady=20,command= b_equals)
b_clear = Button(root,text="clear",padx= 76 ,pady=20,command= b_cleark)


b_sub = Button(root,text="-",padx= 45,pady=20,command= b_subs)
b_mul = Button(root,text="*",padx= 40,pady=20,command= b_muls)
b_div = Button(root,text="/",padx= 40,pady=20,command= b_divs)
#display button
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)
b_clear.grid(row=4,column=1,columnspan=2)
b_add.grid(row=5,column=0)
b_equal.grid(row=5,column=1,columnspan=2)
b_sub.grid(row=6,column=0)
b_mul.grid(row=6,column=1)
b_div.grid(row=6,column=2)


root.mainloop()
