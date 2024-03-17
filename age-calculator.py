from tkinter import *
from datetime import date

root = Tk()
root.geometry("700x500")
root.title("age calculator")

photo = PhotoImage(file="sample.png")
myimage = Label(image = photo)
myimage.grid(row=0, column=1)

def calculateage():
    today = date.today
    birthdate = date(int(yearEntry.get())),
    int(monthEntry.get()) ,int(dayEntry.get())
    age = today.year - birthdate.year - ((today.month,today.day)< (birthdate.month,birthdate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6,column=1)
    
    Label(text="Name").grid(row=1,column=0,padx=90)
    Label(text="Year").grid(row=2,column=0)
    Label(text="Month").grid(row=3,column=0)
    Label(text="Day").grid(row=4,column=0)
    nameValue = StringVar()
    yearValue = StringVar()
    monthValue = StringVar()
    dayValue = StringVar()
    nameEntry = Entry(root, textvariable=nameValue)
    yearEntry = Entry(root, textvariable=yearValue)
    monthEntry = Entry(root, textvariable=monthValue)
    dayEntry = Entry(root, textvariable=dayValue)
    nameEntry.grid(row=1,column=1,pady=10)
    yearEntry.grid(row=2,column=1, pady=10)
    monthEntry.grid(row=3,column=1, pady=10)
    dayEntry.grid(row=4,column=1,pady=10)

    Button(text= "Calculate Age", command= calculateage).grid(row=5,column=1,pady=10) 