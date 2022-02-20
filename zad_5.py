import tkinter

def btn1_click():
    window['bg'] = "yellow"

def btn2_click():
    window['bg'] = "red"

def btn3_click():
    window['bg'] = "blue"

def btn4_click():
    window['bg'] = "pink"

window = tkinter.Tk()
window.title("Завдання 5")
window.geometry("600x600")
btn1 = tkinter.Button(window, text = "Жовтий", width = 20, height = 2, bg = "yellow", font = "Arial 16", command = btn1_click)
btn1.pack()
btn2 = tkinter.Button(window, text = "Червоний", width = 25, height = 2, bg = "red", font = "Arial 16", command = btn2_click)
btn2.pack()
btn3 = tkinter.Button(window, text = "Синій", width = 15, height = 2, bg = "blue", font = "Arial 16", command = btn3_click)
btn3.pack()
btn4 = tkinter.Button(window, text = "Рожевий", width = 30, height = 2, bg = "pink", font = "Arial 16", command = btn4_click)
btn4.pack()

window.mainloop()


