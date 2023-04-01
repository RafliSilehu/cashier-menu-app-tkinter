from tkinter import *
from random import *
from class_kopi import*

frame_utama = Tk()
frame_utama.title("7.11")
frame_utama.geometry("1500x750")
frame_utama.configure(bg="#292e2e")

logo = PhotoImage(file="assets/logo.png")
frame_utama.iconphoto(True,logo)
kopi = PhotoImage(file="assets/icon_kopi.png")
menu_icon = PhotoImage(file="assets/mmenu.png")
logo_kasir = PhotoImage(file="assets/kasir.png")

#begin===========================================================================

#title    
frame_judul = Frame(frame_utama,bg="#362312")
judul = Label(frame_judul,justify="left",image=logo)
judul_menu = Label(frame_judul, text="7.11 Café",bg="black",fg="white"
                    ,font=("Verdana",20,"bold")) 
icon_kopi = Label(frame_judul,image=kopi,bg="#362312")
frame_judul.pack(fill="x")
icon_kopi.place(x=1140) 
judul.grid(pady=5,padx=10)
judul_menu.grid(row=0,column=1)   
#end===========================================================================


#begin============================================================================

#body
body = Frame(frame_utama,height=900,width=600,bg="#362312")
body.pack(padx=10,pady=10,fill="both")
#end===========================================================================


#begin============================================================================

#content_body
frame_belanja = Frame(body,bg="#997950",height=550,width=700,bd=10,relief="ridge")
frame_kasir = Frame(body,bg="#997950",height=320,width=520,bd=10,relief="ridge")
frame_undian = Frame(body,bg="#997950",height=220,width=520,bd=10,relief="ridge")


rButton_nama = IntVar()   
rButton_size = IntVar() 
rButton_es = IntVar() 
isi_entry = IntVar(value="")
tampilan_hasil_kasir = StringVar()
tampilan_hasil_undian = StringVar()

icon_menu = Label(frame_belanja,bg="#997950" ,image= menu_icon,width=650)
tulisan_ukuran = Label(frame_belanja,bg="#4B3A26",text="     Ukuran "
                    ,font=("Verdana",16),fg="white")
tulisan_isi_jumlah = Label(frame_belanja,bg="#4B3A26",text="     Isi Jumlah Item "
                        ,font=("Verdana",16),fg="white")
entry = Entry(frame_belanja,textvariable=isi_entry,bd=5)   

def keranjang():
        rB_nama = rButton_nama.get()
        rB_size = rButton_size.get()
        rB_es = rButton_es.get()
        banyak = isi_entry.get()
        
        dict_nama_kopi = {
            1 : "Kopi Cappucino",
            2 : "Kopi Americano",
            3 : "Kopi Luwak",
            4 : "Kopi ABC",
            5 : "Kopi Latte",
            6 : "Kopi Susu",
            7 : "Kopi Toraja",
            8 : "Kopi Lampung",
            9 : "Wedang Kopi",
        }
        
        dict_ukuran_kopi = {
            10 : "S",
            11 : "M",
            12 : "L"
        }
        
        if rB_nama  == 1 :
            if rB_size == 10:
                total_harga_end  = kopi_cappucino.total_harga("S")  
            elif rB_size == 11:
                total_harga_end  = kopi_cappucino.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_cappucino.total_harga("L")
        elif rB_nama == 2 :
            if rB_size == 10:
                total_harga_end  = kopi_americano.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_americano.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_americano.total_harga("L")
        elif rB_nama == 3 :
            if rB_size == 10:
                total_harga_end  = kopi_luwak.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_luwak.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_luwak.total_harga("L")
        elif rB_nama == 4 : 
            if rB_size == 10:
                total_harga_end  = kopi_abc.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_abc.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_abc.total_harga("L")
        elif rB_nama == 5 :    
            if rB_size == 10:
                total_harga_end  = kopi_latte.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_latte.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_latte.total_harga("L")
        elif rB_nama == 6 :
            if rB_size == 10:
                total_harga_end  = kopi_susu.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_susu.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_susu.total_harga("L")
        elif rB_nama == 7 :  
            if rB_size == 10:
                total_harga_end  = kopi_toraja.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_toraja.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_toraja.total_harga("L")
        elif rB_nama == 8 :    
            if rB_size == 10:
                total_harga_end  = kopi_lampung.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = kopi_lampung.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = kopi_lampung.total_harga("L")
        elif rB_nama == 9 :  
            if rB_size == 10:
                total_harga_end  = wedang_kopi.total_harga("S")   
            elif rB_size == 11:
                total_harga_end  = wedang_kopi.total_harga("M")
            elif rB_size == 12:
                total_harga_end  = wedang_kopi.total_harga("L")
        
        #Es       
        if rB_es == 13:
            total_harga_end *= isi_entry.get()
            total_harga_end += 1000
            tampilan_hasil_kasir.set(f"""Pesanan Anda
{"="*30}
Nama item : Es {dict_nama_kopi[rB_nama]} 
Ukuran : {dict_ukuran_kopi[rB_size]}
Jumlah : {banyak}
{"="*30}
Total Harga: Rp {total_harga_end}
{"="*30}""")
        #Tidak pakai es
        else:
            total_harga_end *= isi_entry.get()
            tampilan_hasil_kasir.set(f"""Pesanan Anda
{"="*30}
Nama item : {dict_nama_kopi[rB_nama]} 
Ukuran : {dict_ukuran_kopi[rB_size]}
Jumlah : {banyak}
{"="*30}
Total Harga: Rp {total_harga_end}
{"="*30}""")
        
        #Undian 
        hadiah = ["Mobil", "Motor", "Laptop", "Hp","Rumah","Tas","Lemari"]
        no_undian = randint(1,10)
        if total_harga_end >= 50000:
            no_undian_pembeli = randint(1,10)
            if no_undian_pembeli == no_undian:
                hadiah_pembeli = choice(hadiah)
                tampilan_hasil_undian.set(f"""Nomor Undian Hadiah : {no_undian}
Nomor Undian anda adalah {no_undian_pembeli}

Selamat anda mendapatkan {hadiah_pembeli}""")
            else:
                tampilan_hasil_undian.set(f"""Nomor Undian Hadiah : {no_undian}
Nomor Undian anda adalah {no_undian_pembeli}

Mohon maaf anda kurang beruntung""")
        else:
            tampilan_hasil_undian.set(f"""     Ayo tambah Rp {50000-total_harga_end} lagi!!! 
        Untuk mendapatkan 
        kesempatan hadiah 
        MOBIL""")
                                
def keluar():
    frame_utama.quit()
                        
cappucino = Radiobutton(frame_belanja,variable= rButton_nama,text="Kopi Cappucino",
                            command=keranjang,value=1,font=("Verdana",16),bg="#997950"
                            ,activebackground="#4B3A26",activeforeground="white")
americano = Radiobutton(frame_belanja,text="Kopi Americano",font=("Verdana",16)
                            ,variable= rButton_nama,command=keranjang,value=2
                            ,bg="#997950",activebackground="#4B3A26",
                            activeforeground="white" )
luwak = Radiobutton(frame_belanja,text="Kopi Luwak",font=("Verdana",16),
                        variable= rButton_nama,command=keranjang,value=3
                        ,bg="#997950",activebackground="#4B3A26",
                        activeforeground="white" )
abc = Radiobutton(frame_belanja,text="Kopi ABC",font=("Verdana",16)
                    ,variable= rButton_nama,command=keranjang,value=4
                    ,bg="#997950" ,activebackground="#4B3A26",
                    activeforeground="white")
latte = Radiobutton(frame_belanja,text="Kopi Latte",font=("Verdana",16)
                    ,variable= rButton_nama,command=keranjang,value=5
                    ,bg="#997950",activebackground="#4B3A26",
                    activeforeground="white" )
susu = Radiobutton(frame_belanja,text="Kopi Susu",font=("Verdana",16)
                    ,variable= rButton_nama,command=keranjang,value=6
                    ,bg="#997950",activebackground="#4B3A26",
                    activeforeground="white" )
toraja = Radiobutton(frame_belanja,text="Kopi Toraja",font=("Verdana",16)
                    ,variable= rButton_nama,command=keranjang,value=7
                    ,bg="#997950",activebackground="#4B3A26",
                    activeforeground="white" )
lampung = Radiobutton(frame_belanja,text="Kopi Lampung",font=("Verdana",16)
                        ,variable= rButton_nama,command=keranjang,value=8
                        ,bg="#997950",activebackground="#4B3A26",
                        activeforeground="white" )
wedang = Radiobutton(frame_belanja,text="Wedang kopi",font=("Verdana",16)
                        ,variable= rButton_nama,command=keranjang,value=9
                    ,bg="#997950",activebackground="#4B3A26",
                    activeforeground="white" )
    
S = Radiobutton(frame_belanja,text="S",font=("Verdana",14)
                    ,variable= rButton_size,command=keranjang,value=10
                    ,bg="#997950" ,activebackground="#4B3A26",
                    activeforeground="white")
M = Radiobutton(frame_belanja,text="M",font=("Verdana",14)
                    ,variable = rButton_size,command=keranjang,value=11
                    ,bg="#997950",activebackground="#4B3A26",
                    activeforeground="white" )
L = Radiobutton(frame_belanja,text="L",font=("Verdana",14)
                    ,variable = rButton_size,command=keranjang,value=12
                    ,bg="#997950",activebackground="#4B3A26",
                    activeforeground="white" )
es = Checkbutton(frame_belanja,text="Es",bg="#997950",onvalue=13,
                activebackground="#4B3A26",activeforeground="white",
                font=("Verdana",14),variable = rButton_es,command=keranjang)
    
submit =  Button(frame_belanja,text="Submit",font=("Helvetica",16),justify="center",
                    fg="white",command=keranjang,bg="#5C2C06",activebackground="#7E481C"
                    ,activeforeground="white")
tombol_keluar =  Button(frame_kasir,text=" Quit ",font=("Helvetica",16),justify="center",
                    fg="white",command=keluar,bg="#5C2C06",activebackground="#7E481C"
                    ,activeforeground="white")

#frame belanja=======================================================================
frame_belanja.place(x=10,y=10)

icon_menu.place(x=0,y=0) 
cappucino.place(x=10,y=110)
americano.place(x=250,y=110)
luwak.place(x=450,y=110)   
abc.place(x=10,y=170)  
latte.place(x=250,y=170)  
susu.place(x=450,y=170)  
toraja.place(x=10,y=230) 
lampung.place(x=250,y=230)  
wedang.place(x=450,y=230)
es.place(x=10,y=275)
tulisan_ukuran.place(x=0,y=320)
S.place(x=10,y=360)
M.place(x=250,y=360)   
L.place(x=450,y=360) 
tulisan_isi_jumlah.place(x=0,y=410)
entry.place(x=40,y=460)
submit.place(x=560,y=460)

#frame kasir and frame undian==========================================================
frame_kasir.place(x=730,y=10)

icon_kasir = Label(frame_kasir,image=logo_kasir,bg="#997950")
tulisan_kasir = Label(frame_kasir,text="Kasir"
                    ,bg="#997950",font=("Times",32,"bold"))
batas = Label(frame_kasir,text="="*35,bg="#997950"
            ,font=("Times",19,"bold"))
tulisan_undian = Label(frame_undian,text="Undian"
                    ,bg="#997950",font=("Times",25,"bold"))
batas2 = Label(frame_undian,text="="*35,bg="#997950"
            ,font=("Times",19,"bold"))
tampilan_hasil = Label(frame_kasir,textvariable=tampilan_hasil_kasir
                    ,bg="#997950",font=("Times",16,"bold"),justify="left")
tampilan_undian = Label(frame_undian,textvariable=tampilan_hasil_undian,justify="center"
                        ,bg="#997950",font=("Times",18,"bold"))

icon_kasir.place(x=430,y=5)
tulisan_kasir.place(x=20,y=5)
batas.place(x=2,y=60)
tampilan_hasil.place(x=10,y=100)
tombol_keluar.place(x=420,y=250)

frame_undian.place(x=730,y=340)
tulisan_undian.place(x=20,y=5)
batas2.place(x=2,y=40)
tampilan_undian.place(x=70,y=65)

#end===========================================================================
                            
frame_utama.mainloop()