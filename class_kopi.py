class Kopi(object):
    """Membuat Class Kopi yang memiliki data dan proses"""
    
    def __init__(self,nama,harga_permili):
        self.nama = nama
        self.harga_permili = harga_permili    
    
    def total_harga(self,ukuran):
        """Membuat proses mencari total harga permili sesuai ukuran gelas"""   
        if ukuran == "S":
            total_harga_ukuran = 250 * self.harga_permili
            return total_harga_ukuran
        elif ukuran =="M":
            total_harga_ukuran = 350 * self.harga_permili
            return total_harga_ukuran
        elif ukuran =="L":
            total_harga_ukuran = 500 * self.harga_permili
            return total_harga_ukuran

kopi_cappucino = Kopi("Kopi Cappucino",70)
kopi_americano = Kopi("Kopi Americano",50)
kopi_luwak = Kopi("Kopi Luwak",50)
kopi_abc = Kopi("Kopi ABC",15)
kopi_latte = Kopi("Kopi Latte",30)
kopi_toraja = Kopi("Kopi Toraja",30)
kopi_susu = Kopi("Kopi Susu",10)
kopi_lampung = Kopi("Kopi Lampung",30)
wedang_kopi = Kopi("Wedang Kopi",15)  