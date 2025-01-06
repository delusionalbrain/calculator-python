from tkinter import *

root=Tk()
def click(b):
    labell.insert(END,b)

def express():
    calculate=labell.get()
    try:
        newc=eval(calculate)
        newlabel.config(text=f"Result:{newc}")
    except(ZeroDivisionError):
        newlabel.config(text="Can not divide by Zero")   
    except:
        newlabel.config(text="Error")


def clear():
    labell.delete(0,END)

newlabel=Button(root,text="Result: ")
newlabel.grid(row=2,columnspan=3,column=1,sticky=W)

labell=Entry(root,relief=GROOVE)
labell.grid(column=1,columnspan=4,row=1)

label1= Button(root,text=1,command=lambda: click("1")).grid(row=5,column=3)
label2= Button(root,text=2,command=lambda: click("2")).grid(row=5,column=2)
label3= Button(root,text=3,command=lambda: click("3")).grid(row=5,column=1)
label4= Button(root,text=4,command=lambda: click("4")).grid(row=4,column=3)
label5= Button(root,text=5,command=lambda: click("5")).grid(row=4,column=2)
label6= Button(root,text=6,command=lambda: click("6")).grid(row=4,column=1)
label7= Button(root,text=7,command=lambda: click("7")).grid(row=3,column=3)
label8= Button(root,text=8,command=lambda: click("8")).grid(row=3,column=2)
label9= Button(root,text=9,command=lambda: click("9")).grid(row=3,column=1)
label0= Button(root,text=0,command=lambda: click("0")).grid(row=6,column=1)
label11=Button(root,text=".",command=lambda: click(".")).grid(row=6,column=2)
label12=Button(root,text="=",command=express,fg="blue").grid(row=6,column=3)
label13=Button(root,text="+",fg="orange",command=lambda: click("+")).grid(row=3,column=4)
label14=Button(root,text="-",fg="orange",command=lambda: click("-")).grid(row=4,column=4)
label15=Button(root,text="*",fg="orange",command=lambda: click("*")).grid(row=5,column=4)
label16=Button(root,text="/",fg="orange",command=lambda: click("/")).grid(row=6,column=4)
label100=Button(root,text="C",fg="blue",command=clear).grid(row=2,column=4)

root.mainloop()