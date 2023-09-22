import tkinter
from tkinter import *

root = Tk()
root.title("//CALCULATOR//")
root.geometry("550x620+500+100")
root.resizable(False, False)
root.configure(bg= "#000000")
icon = PhotoImage(file='CalculatorIcon.png')
root.iconphoto(True, icon)

equation = ""

def show(value):
    global equation
    equation += value
    label_view.config(text=equation)

def clear():
    global equation
    equation = " "
    label_view.config(text=equation)

def calculate():
    global equation
    result= " "
    if equation != "":
        try:
            result =eval(equation)
        except:
            result = "Error"
            equation = ""
    label_view.config(text=result)

label_view = Label(root, width=25, height= 3,text="", font=("arial", 30), bg ="#52595D")
label_view.pack(padx=20, pady=20)

Button(root, text="C", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#87CEFA",bg="#0041C2",command=lambda: clear()).place(x=20,y=170)
Button(root, text="%", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#FFAE42", command=lambda:show("%")).place(x=155,y=170)
Button(root, text="/", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#FFAE42", command=lambda:show("/")).place(x=290,y=170)
Button(root, text="*", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#FFAE42", command=lambda:show("*")).place(x=427,y=170)

Button(root, text="7", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("7")).place(x=20,y=260)
Button(root, text="8", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("8")).place(x=155,y=260)
Button(root, text="9", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("9")).place(x=290,y=260)
Button(root, text="-", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#FFAE42", command=lambda:show("-")).place(x=427,y=260)

Button(root, text="4", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("4")).place(x=20,y=350)
Button(root, text="5", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("5")).place(x=155,y=350)
Button(root, text="6", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("6")).place(x=290,y=350)
Button(root, text="+", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#FFAE42", command=lambda:show("+")).place(x=427,y=350)

Button(root, text="1", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("1")).place(x=20,y=440)
Button(root, text="2", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("2")).place(x=155,y=440)
Button(root, text="3", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("3")).place(x=290,y=440)
Button(root, text="0", width=9, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show("0")).place(x=20,y=530)

Button(root, text=".", width=4, height= 1, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#E5E4E2", command=lambda:show(".")).place(x=290,y=530)
Button(root, text="=", width=4, height= 3, font=("Arial", 30,"bold"), bd=1,fg="#033E3E",bg="#FFAE42", command=lambda:calculate()).place(x=427,y=440)

root.mainloop()