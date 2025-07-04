from tkinter import *

window = Tk()

window.geometry('500x500')
window.title('Calculator')

e=Entry(window , width = 48 , borderwidth = 2 )
e.place(x = 96 , y = 100)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))


#BUTTONS

b=Button(window , width = 10 , borderwidth = 2 , text = "1" , command = lambda:click(1) )
b.place(x = 100 , y = 130)

b=Button(window , width = 10 , borderwidth = 2 , text = "2" , command = lambda:click(2))
b.place(x = 180 , y = 130)

b=Button(window , width = 10 , borderwidth = 2 , text = "3" , command = lambda:click(3))
b.place(x = 260 , y = 130)

b=Button(window , width = 10 , borderwidth = 2 , text = "4" , command = lambda:click(4))
b.place(x = 100 , y = 160)

b=Button(window , width = 10 , borderwidth = 2 , text = "5" , command = lambda:click(5))
b.place(x = 180 , y = 160)

b=Button(window , width = 10 , borderwidth = 2 , text = "6" , command = lambda:click(6))
b.place(x = 260 , y = 160)

b=Button(window , width = 10 , borderwidth = 2 , text = "7" , command = lambda:click(7))
b.place(x = 100 , y = 190)

b=Button(window , width = 10 , borderwidth = 2 , text = "8" , command = lambda:click(8))
b.place(x = 180 , y = 190)

b=Button(window , width = 10 , borderwidth = 2 , text = "9" , command = lambda:click(9))
b.place(x = 260 , y = 190)

b=Button(window , width = 10 , borderwidth = 2 , text = "0" , command = lambda:click(0))
b.place(x = 180 , y = 220)

#Operators

def add():
    n1=e.get()
    global math
    math = 'addition'
    global i
    i=int(n1)
    e.delete(0, END)

def sub():
    n1=e.get()
    global math
    math='subtraction'
    global i
    i=int(n1)
    e.delete(0, END)

def mul():
    n1=e.get()
    global math
    math = 'multiplication'
    global i
    i=int(n1)
    e.delete(0, END)

def div():
    n1=e.get()
    global math
    math = 'division'
    global i
    i=int(n1)
    e.delete(0, END)

def clear():
    e.delete(0, END)

def equal():
    n2=e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0,i+int(n2))
    elif math == "subtraction":
        e.insert(0,i-int(n2))
    elif math == "multiplication":
        e.insert(0,i*int(n2))
    elif math == "division":
        e.insert(0,i/int(n2))




b=Button(window , width = 5 , borderwidth = 2 , text = "+" , command = add)
b.place(x = 340 , y = 130)

b=Button(window , width = 5 , borderwidth = 2 , text = "*" , command = mul)
b.place(x = 340 , y = 190)

b=Button(window , width = 5 , borderwidth = 2 , text = "-" , command = sub)
b.place(x = 340 , y = 160)

b=Button(window , width = 5 , borderwidth = 2 , text = "/" , command = div)
b.place(x = 340 , y = 220)

b=Button(window , width = 10 , borderwidth = 2 , text = "Clear" , command = clear)
b.place(x = 100 , y = 220)

b=Button(window , width = 10 , borderwidth = 2 ,text = '=' , command = equal)
b.place(x = 260 , y = 220)




mainloop()