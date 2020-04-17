import tkinter as tk
from tkinter import Label, Button, StringVar
import time
import calculator as cal
import price_button as pb

localtime = time.asctime(time.localtime(time.time()))


class App1:

    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 25 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

        # _____ Info Food _____

        self.Label1 = tk.Label(master=top, text="Restaurant Management System", background="#091833", font=font11,
                               foreground="#f2a343")
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=507)
        localtime1 = tk.Label(master=top, text=localtime, background="#091833", font=font16,
                               fg="steel blue")
        localtime1.place(relx=0.420, rely=0.12)

        # _____ Label Food _____

        self.Label12 = tk.Label(master=top, text="Order Num :", background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label12.place(relx=0.054, rely=0.25)
        self.Label12 = tk.Label(master=top, text="Fried Potato :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.044, rely=0.32)
        self.Label12 = tk.Label(master=top, text="Chicken Burger :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.021, rely=0.4)
        self.Label12 = tk.Label(master=top, text="Big King :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.070, rely=0.48)
        self.Label12 = tk.Label(master=top, text="Chicken Royal :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.033, rely=0.56)
        self.Label12 = tk.Label(master=top, text="Vegan Salad :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.048, rely=0.64)
        self.Label12 = tk.Label(master=top, text="Drinks :", background="#091833", font=font12,
                                foreground="darkcyan")
        self.Label12.place(relx=0.086, rely=0.71)

        # _____ Entry Food _____

        self.entry1 = tk.Entry(master=top, textvariable=rand, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.16, rely=0.25)
        self.entry1 = tk.Entry(master=top, textvariable=fries, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.16, rely=0.32)
        self.entry1 = tk.Entry(master=top, textvariable=chkburger, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.16, rely=0.4)
        self.entry1 = tk.Entry(master=top, textvariable=bigking, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.16, rely=0.48)
        self.entry1 = tk.Entry(master=top, textvariable=chkroyal, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.16, rely=0.56)
        self.entry1 = tk.Entry(master=top, textvariable=vegsal, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.16, rely=0.64)
        self.entry1 = tk.Entry(master=top, textvariable=drinks, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.16, rely=0.71)

        # _____ Calc _____

        self.entry2 = tk.Entry(master=top, textvariable=equation, background="#d9d9d9", foreground="#102656",
                               selectbackground="#f2a343", font=font13)
        self.entry2.place(relx=0.705, rely=0.24, height=35, relwidth=0.267)
        equation.set('This calculator may help you!')

        self.Button1 = tk.Button(master=top, text='''7''', background="#285fd7", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(7, equation))
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''8''', background="#285fd7", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(8, equation))
        self.Button1.place(relx=0.780, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''9''', background="#285fd7", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(9, equation))
        self.Button1.place(relx=0.856, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''/''', background="#285fd7", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key("/", equation))
        self.Button1.place(relx=0.934, rely=0.34, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''4''', background="#204cac", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(4, equation))
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''5''', background="#204cac", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(5, equation))
        self.Button1.place(relx=0.780, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''6''', background="#204cac", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(6, equation))
        self.Button1.place(relx=0.856, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''*''', background="#204cac", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key("*", equation))
        self.Button1.place(relx=0.934, rely=0.44, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''1''', background="#183981", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(1, equation))
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''2''', background="#183981", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(2, equation))
        self.Button1.place(relx=0.780, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''3''', background="#183981", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(3, equation))
        self.Button1.place(relx=0.856, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''-''', background="#183981", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key("-", equation))
        self.Button1.place(relx=0.934, rely=0.54, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''0''', background="#122c63", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(0, equation))
        self.Button1.place(relx=0.705, rely=0.64, height=35, width=145)
        self.Button1 = tk.Button(master=top, text='''.''', background="#122c63", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key(".", equation))
        self.Button1.place(relx=0.856, rely=0.64, height=35, width=67)
        self.Button1 = tk.Button(master=top, text='''+''', background="#122c63", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.key("+", equation))
        self.Button1.place(relx=0.934, rely=0.64, height=35, width=37)

        self.Button1 = tk.Button(master=top, text='''=''', background="#102656", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.equal_key(equation))
        self.Button1.place(relx=0.705, rely=0.72, height=44, width=222)

        self.Button1 = tk.Button(master=top, text='''C''', background="#102656", font=font14,
                                 foreground="#ffffff", borderwidth='0', command=lambda: cal.clear_key(equation))
        self.Button1.place(relx=0.934, rely=0.72, height=44, width=37)

        # _____ Costs _____

        self.Label12 = tk.Label(master=top, text="Cost :", background="#091833", font=font12,
                                foreground="#e16740")
        self.Label12.place(relx=0.39, rely=0.32)
        self.Label12 = tk.Label(master=top, text="Service charge :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.34, rely=0.4)
        self.Label12 = tk.Label(master=top, text="Tax :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.395, rely=0.48)
        self.Label12 = tk.Label(master=top, text="Subtotal :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.38, rely=0.56)
        self.Label12 = tk.Label(master=top, text="Total :", background="#091833", font=font12,
                                foreground="#bac8bd")
        self.Label12.place(relx=0.39, rely=0.64)

        # ___ Entry Cost ___

        self.entry13 = tk.Entry(master=top, textvariable=cost, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry13.place(relx=0.47, rely=0.33)
        self.entry13 = tk.Entry(master=top,  textvariable=service_charge, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry13.place(relx=0.47, rely=0.41)
        self.entry13 = tk.Entry(master=top, textvariable=tax, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry13.place(relx=0.47, rely=0.49)
        self.entry13 = tk.Entry(master=top, textvariable=subtotal, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry13.place(relx=0.47, rely=0.57)
        self.entry13 = tk.Entry(master=top, textvariable=total, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry13.place(relx=0.47, rely=0.65)

        # ___ Control Buttons ___

        self.Button2 = tk.Button(master=top, text='PRICE', background='#f2a343', font=font16, command=pb.list1)
        self.Button2.place(relx=0.039, rely=0.86, height=36, width=107)
        self.Button2 = tk.Button(master=top, text='TOTAL', background='#f2a343', font=font16)
        self.Button2.place(relx=0.156, rely=0.86, height=36, width=107)
        self.Button2 = tk.Button(master=top, text='RESET', background='#f2a343', font=font16)
        self.Button2.place(relx=0.272, rely=0.86, height=36, width=107)
        self.Button2 = tk.Button(master=top, text='EXIT', background='#f2a343', font=font16, command=close_window)
        self.Button2.place(relx=0.389, rely=0.86, height=36, width=107)


def close_window():
    root.destroy()


root = tk.Tk()
equation = tk.StringVar()
rand = tk.StringVar()
fries = tk.StringVar()
chkburger = tk.StringVar()
bigking = tk.StringVar()
chkroyal = tk.StringVar()
vegsal = tk.StringVar()
drinks = tk.StringVar()


cost = tk.StringVar()
service_charge = tk.StringVar()
tax = tk.StringVar()
subtotal = tk.StringVar()
total = tk.StringVar()

my_gui = App1(root)
root.mainloop()
