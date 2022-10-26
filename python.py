# from tkinter import *
# top = Tk()
# top.geometry("450x300")
# top.title(" Bank Details")
# top.configure(bg='skyblue')
# Custid = Label(top, text="Custid").place(x=40, y=60)
# Custid_entry = Entry(top, width=30).place(x=150, y=60)
# Name = Label(top, text="Customer Name").place(x=40, y=90)
# Name_entry = Entry(top, width=30).place(x=150, y=90)
# Branch = Label(top, text="Branch").place(x=40, y=120)
# Branch_entry = Entry(top, width=30).place(x=150, y=120)
# Account_type = Label(top, text="Account type").place(x=40, y=150)
# var = IntVar()
# Saving = Radiobutton(top, text="Saving", variable=var, value=1).place(x=150, y=150)
# Non_saving = Radiobutton(top, text="Non Saving", variable=var, value=2).place(x=250, y=150)
# Amount = Label(top, text="Amount").place(x=40, y=180)
# scale = Scale(top, variable=var, orient=HORIZONTAL).place(x=100, y=180)
# Insert = Button(top, text="Insert").place(x=40, y=220)
# Insert = Button(top, text="Update").place(x=120, y=220)
# Insert = Button(top, text="Delete").place(x=40, y=260)
# Insert = Button(top, text="Select").place(x=120, y=260)
# top.mainloop()



# largerst from two
# a=int (input("Enter 1st no:"))
# b=int (input("Enter 2nd no:"))
# if(a>b):
#     print("Largest nuber is",a)
# else:
#     print("Largest number is",b)


# swap
# a= int(input("Enter the 1st no:"))
# b= int(input("Enter the 2nd no:"))
# print("Number before swap a=",a,"b=",b)
# c=a
# a=b
# b=c
# print("Number after swap: a=",a,"b= ",b)


# class parent():
#     def dispaly1(self):
#         print('This is parent class')
        
# class Child(parent):
#     def display2(self):
#         print('This is a child class')
        
# object1=Child()
# object1.diaplay1()
# object1.diaplay2()




# 

# from tkinter import*
# top =Tk()
# top.geometry("450x300")
# top.title("Registration")
# top.configure(bg='skyblue')
# Regno = Label(top,text="Regno").place( x=40,y=40)
# Regno_entry = Entry(top,width=30).place (x=110,y=40)
# Name = Label(top,text="Name").place(x=40,y=80)
# Name_entry = Entry(top,width=30).place(x=110,y=80)
# Dept = Label(top,text="Dept").place(x=40,y=120)
# Dept_entry = Entry(top,width=30).place(x=110,y=120)
# Gender = Label(top,text="Gender").place(x=40,y=150)
# var = IntVar()
# male =Radiobutton(top,text="Male",variable=var,value=1).place(x=110,y=150)
# female =Radiobutton(top,text="Female",variable=var,value=2).place(x=170,y=150)
# Age=Label(top,text="Age").place(x=40,y=180)
# sp=Spinbox(top,from_=0,to=20).place(x=110,y=180)
# Insert=Button(top,text="Insert").place(x=40,y=210)
# Insert=Button(top,text="Update").place(x=110,y=210)
# Insert=Button(top,text="Delete").place(x=40,y=250)
# Insert=Button(top,text="Select").place(x=110,y=250)
# top.mainloop()


# key press event
# import turtle
# Windows=turtle.Screen()
# Windows.setup(400,500)
# Windows.title("handelling keypress")
# Windows.bgcolor("green")

# marker=turtle.Turtle()
# def up():
#     marker.setheading(90)
#     marker.forward(100)
# def down():
#     marker.setheading(270)
#     marker.forward(100)
# def left():
#     marker.setheading(180)
#     marker.forward(100)
# def right():
#     marker.setheading(0)
#     marker.forward(100)
# turtle.listen()
# turtle.onkey(up,"up")
# turtle.onkey(down,"down")
# turtle.onkey(left,"left")
# turtle.onkey(right,"right")
# turtle.mainloop()


# mouse press event

import turtle
Windows=turtle.Screen()

Windows.title("handelling Mouse Click")
Windows.bgcolor("lightgreen")

marker=turtle.Turtle()
marker.color("purple")
marker.pensize(3)
marker.shape('square')

def right_click_handler(x,y):
    marker.penup()
    marker.goto(x,y)
    marker.pendown()
turtle.listen()
Windows.onclick(marker.goto)
Windows.onclick(right_click_handler,3)

Windows.mainloop()
