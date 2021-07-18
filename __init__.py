class mahasiswa ():

    def __init__(self,input_nama) :
        self.nama = input_nama 

    def belajar (self ) :
        print (self.nama)

    def tidur (self,kondisi) :
        print (self.nama , "sedang tidur di kelas ",kondisi)

otong = mahasiswa ("Otong Surotong")
print (otong.nama)

class belanja () :
    __olshop = "Shopee"

    def __init__(self,keranjang_belanja,total_harga) :
        self.barang = keranjang_belanja 
        self.harga = total_harga

    def makanan (self,) :
        print (self, "Sudah ter scan silahkan masukan keranjang")

    def minuman (self,kondisi) :
        print (self,"expired masih lama")

keranjang = belanja("LADANG LIMA", "Rp.30.000") 

print (keranjang.barang)
print (keranjang.harga)

class kelas() :
    jurusan = "Teknik Sipil"
    __nilai = 50 #private

    def __init__ (self,input_nama,input_nim) :
        self.nama = input_nama
        self.nim = input_nim 

    def uts (self,input_nilai) :
        self .__nilai += input_nilai

    def uas (self,input_nilai)  :
        self.__nilai += input_nilai 

    def cek_status (self):
        if self.__nilai <= 50 :
            print (self.nama,"Tidak lulus")
        else :
              print (self.nama, " : Lulus")

michael = kelas ("Michael Joan",210213)
miskha = kelas ("Mishka Alamanda ",20211113)

michael.uts (20)
michael.uas (40)

michael.cek_status ()
#print (michael.__nilai) #kalau ini di print hasilnya tidak akan keluar karna nilai bersifat private 

#jadi fungsi init ini untuk memudahkan menjalankan argumen argumen yang sudah di buat di class 
#jadi ga usah print satu persatu 

