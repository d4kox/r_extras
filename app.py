import tkinter as tk
from tkinter import mainloop, messagebox
from typing import Text

ventana1=tk.Tk()
ventana1.title("calculadora")
ventana1.geometry("500x520")
ventana1.configure(bg="grey")

a1=tk.Entry(ventana1)
a1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

a2=tk.Entry(ventana1)
a2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

a3=tk.Entry(ventana1)
a3.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
def calcular():
    num1=int(a1.get())
    num2=int(a3.get())
    if a2.get()== "+":
        resultado=num1+num2
    if a2.get()== "-":
        resultado=num1-num2
    if a2.get()== "x":
        resultado=num1*num2
    if a2.get()== "/":
        resultado=num1/num2
    a5.insert(0,resultado)
a4=tk.Button(ventana1,text="resolver",command=calcular)
a4.pack(side=tk.TOP)

a5=tk.Entry(ventana1)
a5.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

ventana1.mainloop()