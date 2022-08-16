from tkinter import *

root= Tk()

root.title("PARITY CHECKER")
 
label1=Label(root, text=" Enter the data:- ")
inp=Entry(root,width=50)
label1.grid(column=0,row=0,pady=20)

inp.grid(column=1, row=0)

def evenBit():
    s=inp.get()
    data=""
    if(s.count('1')%2==0):
        data=s+'0'
    else:
        data=s+'1'


    output= Label(root, text= "Data after adding parity bit --> "+data,pady=20)
    output.grid(row=3,column=0)

def oddBit():
    s=inp.get()
    data=""
    if(s.count('1')%2==0):
        data=s+'1'
    else:
        data=s+'0'


    output= Label(root, text= "Data after adding parity bit --> "+data,pady=20)
    output.grid(row=3,column=1)




btn1= Button(root, text=" Click to add even bit parity  ", command=evenBit)


btn2= Button(root, text=" Click to add odd bit parity  ", command=oddBit)

btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)

root.mainloop() 



