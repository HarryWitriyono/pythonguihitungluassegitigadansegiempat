#!/usr/bin/python3
import tkinter as tk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        def hapuspage():
            for root.frame in frame2.winfo_children():
                root.frame.destroy()
        def page1():
            def hitungluassegitiga():
                alas=0.0
                tinggi=0.0
                alas = float(entryalas.get())
                tinggi=float(entrytinggi.get())
                luas=1/2*alas*tinggi
                labelluassegitiga.configure(text="Luas segi tiga = "+str(luas))
            hapuspage()
            frame3 = tk.Frame(frame2)
            frame3.configure(
             height=200,
             highlightbackground="#400040",
            highlightthickness=5,
             width=200)
            frame3.pack(side="top")
            labeljudul = tk.Label(frame3,text="Hitung Luas Segi Tiga",font="Arial,20")
            labeljudul.grid(row=0,column=0,columnspan=2)
            labelalas = tk.Label(frame3,text="Panjang Alas : ")
            labelalas.grid(row=1,column=0)
            entryalas = tk.Entry(frame3)
            entryalas.grid(row=1,column=1)
            labeltinggi = tk.Label(frame3,text="Tinggi Segi Tiga :")
            labeltinggi.grid(row=2,column=0)
            entrytinggi = tk.Entry(frame3)
            entrytinggi.grid(row=2,column=1)
            buttonHitungLuasSegiTiga = tk.Button(frame3,text="Hitung Luas Segi Tiga",command=hitungluassegitiga)
            buttonHitungLuasSegiTiga.grid(row=3,column=0,columnspan=2)
            labelluassegitiga = tk.Label(frame3,text="Luas segi tiga = ")
            labelluassegitiga.grid(row=4,column=0)
        def page2():
            def hitungluassegiempat():
                panjang=0.0
                lebar=0.0
                panjang = float(entrypanjang.get())
                lebar=float(entrylebar.get())
                luas=panjang*lebar
                labelluassegiempat.configure(text="Luas segi tiga = "+str(luas))
            hapuspage()
            frame4 = tk.Frame(frame2)
            frame4.configure(
             height=200,
             highlightbackground="#400040",
             highlightthickness=5,
             takefocus=False,
             width=200)
            frame4.pack(side="top")
            labeljudul=tk.Label(frame4,text="Luas Segi Empat",font="Arial,20")
            labeljudul.grid(row=0,column=0,columnspan=2)
            labelpanjang = tk.Label(frame4,text="Panjang Segi Empat : ")
            labelpanjang.grid(row=1,column=0)
            entrypanjang = tk.Entry(frame4)
            entrypanjang.grid(row=1,column=1)
            labellebar = tk.Label(frame4,text="Lebar segi empat : ")
            labellebar.grid(row=2,column=0)
            entrylebar=tk.Entry(frame4)
            entrylebar.grid(row=2,column=1)
            buttonHitungLuasSegiEmpat=tk.Button(frame4,text="Hitung Luas Segi Empat",command=hitungluassegiempat)
            buttonHitungLuasSegiEmpat.grid(row=3,column=0,columnspan=2)
            labelluassegiempat = tk.Label(frame4)
            labelluassegiempat.grid(row=4,column=0)
        panedwindow2 = tk.PanedWindow(master, orient="horizontal")
        panedwindow2.configure(
            height=400,
            proxyrelief="flat",
            sashrelief="flat",
            width=500)
        frame1 = tk.Frame(panedwindow2)
        frame1.configure(height=200, width=200)
        button2 = tk.Button(frame1,command=page1)
        button2.configure(text='Luas Segi Tiga')
        button2.pack(side="top")
        button3 = tk.Button(frame1,command=page2)
        button3.configure(text='Luas Segi Empat')
        button3.pack(side="top")
        frame1.pack(side="top")
        panedwindow2.add(frame1, height="400", sticky="nw", width="100")
        frame2 = tk.Frame(panedwindow2)
        frame2.configure(height=200, width=200)
        frame2.pack(side="top")
        panedwindow2.add(frame2, height="400", sticky="nw", width="400")
        panedwindow2.pack(side="top")

        # Main widget
        self.mainwindow = panedwindow2
        page1()

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('sampel multiple frame')
    root.resizable(False,False)
    app = NewprojectApp(root)
    app.run()
