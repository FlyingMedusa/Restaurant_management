import tkinter as tk
from tkinter import Label, Button, StringVar


def list1():
    price = tk.Tk()
    price.geometry("300x250+350+200")
    price.title("Price List")
    price.configure(background="#091833")

    labelinfo = Label(price, text="ITEM", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=0, column=0)
    labelinfo = Label(price, text="PRICE", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=0, column=1)

    labelinfo = Label(price, text="Fried Potato", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=1, column=0)
    labelinfo = Label(price, text="30", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=1, column=1)

    labelinfo = Label(price, text="Chicken Burger", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=2, column=0)
    labelinfo = Label(price, text="40", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=2, column=1)

    labelinfo = Label(price, text="Big King", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=3, column=0)
    labelinfo = Label(price, text="35", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=3, column=1)

    labelinfo = Label(price, text="Chicken Royal", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=4, column=0)
    labelinfo = Label(price, text="45", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=4, column=1)

    labelinfo = Label(price, text="Vegan Salad", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=5, column=0)
    labelinfo = Label(price, text="25", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=5, column=1)

    labelinfo = Label(price, text="Drinks", foreground="#bac8bd", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=6, column=0)
    labelinfo = Label(price, text="20", foreground="#f2a343", font="Al-Aramco 19 bold", background="#091833")
    labelinfo.grid(row=6, column=1)