from tkinter import *
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length <= 0:
        result_label.config(text=f"Error: Length Cannot Be {length}")
    else:
        char = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
        password = "".join(random.sample(char, length))
        result_label.config(text= password)

window = Tk()
window.title("PASSWORD GENERATOR")
window.geometry("340x190+600+300")
window.configure(bg="#413430")
Icon = PhotoImage(file="Password Generator Icon.png")
window.iconphoto(True, Icon)

label = Label(window, text= "Enter the Length of Password you want",font= ("Arial", 12, "bold"),bg="#E6BF83",fg="#413430")
label.pack(padx=10, pady=10)

entry_length = Entry(window,font= ("Arial", 12, "bold"))
entry_length.pack(pady=10)

generate_Button = Button(window,width=15, text= "Generate Password",font=("Arial",12,"bold"), bg="#E6BF83",fg="#413430",command= generate_password)
generate_Button.pack(pady=10)

result_label = Label(window, text="",width=30,font= ("Arial", 12, "bold"), bg="#E6BF83")
result_label.pack(pady=5)

window.mainloop()