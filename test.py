import tkinter as tk


def createNewWindow():
    newWindow = tk.Toplevel(app)
    buttonExample2 = tk.Button(newWindow,
                               text="Create new window",
                               command=createNewWindow)
    buttonExample2.pack()


app = tk.Tk()
buttonExample = tk.Button(app,
                          text="Create new window",
                          command=createNewWindow)
buttonExample.pack()

app.mainloop()
