from tkinter import *

root=Tk()
root.title("give your credit card information to an untrusted site")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

def authentication():
    try:
        input_value = int(input_box.get())
        messagebox.showinfo("YAY","you typed it in succeffly")
    except(ValueError):
        messagebox.showinfo("HEY YOU","only numbers pls")

btn = Button(root, text = "click me to submit information to untrusted site :D", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)

root.mainloop()