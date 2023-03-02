import tkinter as tk

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("800x250")

sonuc = tk.Label(pencere, text="Sonuc",font="Courier 16 bold", width=30, justify="center")
sonuc.place(x=500, y=50)
sayi1 = tk.Entry(pencere, font="Courier 14 bold", width=25, justify="right")
sayi1.place(x=70, y=50)
sayi2 = tk.Entry(pencere, font="Courier 14 bold", width=25, justify="right")
sayi2.place(x=380, y=50)

tus1 = tk.Button(pencere, text="+", font="courier 14 bold", width=10)
tus1.place(x=90, y=110)
tus2 = tk.Button(pencere, text="-", font="courier 14 bold", width=10)
tus2.place(x=220, y=110)
tus3 = tk.Button(pencere, text="*", font="courier 14 bold", width=10)
tus3.place(x=350, y=110)
tus4 = tk.Button(pencere, text="/", font="courier 14 bold", width=10)
tus4.place(x=480, y=110)

sayi1.focus()
 

pencere.mainloop()