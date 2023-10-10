#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
class Sampelmenudesain2App:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        menu1 = tk.Menu(toplevel1)
        menu1.add("command",command=lambda:layouthalamanmuka(self),label='Home')
        menu1.add("command", command=lambda :layoutsegitiga(self), label='Segi Tiga')
        menu1.add("command", command=lambda :layoutsegiempat(self), label='Segi Empat')
        menu1.add("command", command=self.selesai, label='Selesai')
        toplevel1.configure(menu=menu1)
        self.framemenuutama = ttk.Frame(toplevel1)
        self.framemenuutama.configure(height=200, padding=10, width=200)
        def layouthalamanmuka(self):
            for widgets in self.framemenuutama.winfo_children():
                widgets.destroy()
            label1 = ttk.Label(self.framemenuutama)
            label1.configure(text='Hitung Luas Segi Tiga dan Segi Empat')
            label1.pack(side="top")
            label2 = ttk.Label(self.framemenuutama)
            self.img_BTaKGEBec = tk.PhotoImage(file="BTaKGEBec.gif")
            label2.configure(
                compound="top",
                image=self.img_BTaKGEBec,
                text='Versi 2023')
            label2.pack(side="top")

        def hapuslayouthalaman(self):
            layouthalamanmuka(self)

        def layoutsegitiga(self):
            def hitungluassegitiga():
                alas = 0.0
                tinggi = 0.0
                alas = float(entryalas.get())
                tinggi=float(entrytinggi.get())
                luas=1/2*alas*tinggi
                labelluassegitiga.configure(text="Luas segi tiga = "+str(luas))
            hapuslayouthalaman(self)
            labelframe2 = ttk.Labelframe(self.framemenuutama)
            labelframe2.configure(
                height=200,
                labelanchor="n",
                padding=10,
                text='Luas Segi Tiga',
                width=200)
            label3 = ttk.Label(labelframe2)
            label3.configure(justify="left", text='Panjang Alas')
            label3.pack(side="top")
            entryalas = ttk.Entry(labelframe2)
            entryalas.pack(side="top")
            label4 = ttk.Label(labelframe2)
            label4.configure(text='Tinggi segi tiga\n')
            label4.pack(side="top")
            entrytinggi = ttk.Entry(labelframe2)
            entrytinggi.pack(side="top")
            button1 = ttk.Button(labelframe2)
            button1.configure(text='Hitung Luas Segi Tiga',command=hitungluassegitiga)
            button1.pack(side="top")
            labelluassegitiga = ttk.Label(labelframe2)
            labelluassegitiga.configure(text='Luas segi tiga =')
            labelluassegitiga.pack(side="top")
            labelframe2.place(
                anchor="center",
                bordermode="inside",
                relheight=0.84,
                relwidth=0.86,
                relx=0.46,
                rely=0.49,
                x=0,
                y=0)
        def layoutsegiempat(self):
            def hitungluassegiempat():
                panjang=0.0
                lebar=0.0
                panjang=float(entrypanjang.get())
                lebar=float(entrylebar.get())
                luas=panjang*lebar
                labelluassegiempat.configure(text="Luas segi empat = "+str(luas))
            hapuslayouthalaman(self)
            labelframe4 = ttk.Labelframe(self.framemenuutama)
            labelframe4.configure(
                height=200,
                labelanchor="n",
                padding=10,
                text='Luas Segi Empat',
                width=200)
            label6 = ttk.Label(labelframe4)
            label6.configure(justify="left", text='Panjang segi empat :')
            label6.pack(side="top")
            entrypanjang = ttk.Entry(labelframe4)
            entrypanjang.pack(side="top")
            label7 = ttk.Label(labelframe4)
            label7.configure(text='Lebar segi empat :\n')
            label7.pack(side="top")
            entrylebar = ttk.Entry(labelframe4)
            entrylebar.pack(side="top")
            button2 = ttk.Button(labelframe4)
            button2.configure(text='Hitung Luas Segi Empat',command=hitungluassegiempat)
            button2.pack(side="top")
            labelluassegiempat = ttk.Label(labelframe4)
            labelluassegiempat.configure(text='Luas segi empat =')
            labelluassegiempat.pack(side="top")
            labelframe4.place(
                anchor="center",
                bordermode="inside",
                relheight=0.84,
                relwidth=0.86,
                relx=0.46,
                rely=0.49,
                x=0,
                y=0)

        self.framemenuutama.pack(side="top")
        hapuslayouthalaman(self)
        #layouthalamanmuka(self)

        # Main widget
        toplevel1.title('Hitung Luas Segi Tiga dan Segi Empat')
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()
    def selesai(self):
        self.mainwindow.destroy()
if __name__ == "__main__":
    app = Sampelmenudesain2App()
    app.run()
