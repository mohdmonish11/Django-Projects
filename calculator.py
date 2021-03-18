from tkinter import *
import logging
num=0
l=[]
def zeroclick():
    global num
    num=num*10+0
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def oneclick():
    global num
    num=num*10+1
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def twoclick():
    global num
    num=num*10+2
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def threeclick():
    global num
    num=num*10+3
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def fourclick():
    global num
    num=num*10+4
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def fiveclick():
    global num
    num=num*10+5
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def sixclick():
    global num
    num=num*10+6
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def sevenclick():
    global num
    num=num*10+7
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def eightclick():
    global num
    num=num*10+8
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def nineclick():
    global num
    num=num*10+9
    blank_lb.delete(0,END)
    blank_lb.insert(0,str(num))
def addition():
    global num
    l.append(num)
    num=0
    l.append("+")
def subtraction():
    global num
    l.append(num)
    num=0
    l.append("-")
def divide():
    global num
    l.append(num)
    num=0
    l.append("/")
def multiply():
    global num
    l.append(num)
    num=0
    l.append("*")
try:
    def evaluate ():
        print(l)
        if "+" in l:
            l.append(num)
            y=l[0]+l[2]
            blank_lb.delete(0,END)
            blank_lb.insert(0,y)
            l.clear()
            l.append(y)
        elif "-" in l:
            l.append(num)
            y=l[0]-l[2]
            blank_lb.delete(0,END)
            blank_lb.insert(0,y)
            l.clear()
            l.append(y)
        elif "/" in l:
            l.append(num)
            y=l[0]/l[2]
            blank_lb.insert(0,y)
            l.clear()
            l.append(y)
        elif "*" in l:
            l.append(num)
            print(l)
            y=l[0]*l[2]
            blank_lb.delete(0,END)
            blank_lb.insert(0,y)
            l.clear()
            l.append(y)
except Exception as p:
    logging.basicConfig(filename="a.log",level=logging.ERROR)
    logging.info(str(p))
    #l.append(num)
    #blank_lb.delete(0,END)
    #blank_lb.insert(0,l)
    #print(l[0]+l[2])
def clearclick():
    global num
    num=0
    blank_lb.delete(0,END)
    l.clear()
window=Tk()
window.title("Calculator")
window.minsize(450,450)
window.config(bg="#E8E8E8")
blank_lb=Entry(window,width =20,font=("Calibri (Body)",20),fg="#6600CC",bg="#E8E8E8")
b1=Button(window,width=5,text="0",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=zeroclick)
b2=Button(window,width=5,text="1",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=oneclick)
b3=Button(window,width=5,text="2",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=twoclick)
b4=Button(window,width=5,text="3",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=threeclick)
b5=Button(window,width=5,text="4",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=fourclick)
b6=Button(window,width=5,text="5",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=fiveclick)
b7=Button(window,width=5,text="6",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=sixclick)
b8=Button(window,width=5,text="7",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=sevenclick)
b9=Button(window,width=5,text="8",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=eightclick)
b10=Button(window,width=5,text="9",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=nineclick)
b11=Button(window,width=5,text="+",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=addition)
b12=Button(window,width=5,text="-",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=subtraction)
b13=Button(window,width=5,text="/",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=divide)
b14=Button(window,width=5,text="*",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=multiply)
b15=Button(window,width=5,text="=",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=evaluate)
b16=Button(window,width=5,text="clear",font=("Times New Roman",18),fg="#6600CC",bg="#E8E8E8",command=clearclick)
blank_lb.place(x=100,y=20 )
b1.place(x=100,y=80)
b16.place(x=180,y=80)
b2.place(x=100,y=130)
b3.place(x=180,y=130)
b4.place(x=260,y=130)
b11.place(x=340,y=130)
b5.place(x=100,y=180)
b6.place(x=180,y=180)
b7.place(x=260,y=180)
b12.place(x=340,y=180)
b8.place(x=100,y=230)
b9.place(x=180,y=230)
b10.place(x=260,y=230)
b14.place(x=340,y=230)
b13.place(x=260,y=80)
b15.place(x=340,y=80)
window.mainloop()#what this function does

