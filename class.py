#class
class mahasiswa ():
    nama = "nama"

    def __init__(self,nama,alamat):
        self.nama = nama
        self.alamat = alamat
    def belajar (self):
        print (self.nama,"sedang belajar")
    
    def tidur (self,kondisi) :
        print (self.nama , "sedang tidur di kelas ",kondisi)
#kelas harus ada di atas karen python itu interprated language jadi harus berurutan
#cara membuat nama biar template nama nya terganti jadi otong

#main program
rebeka = mahasiswa ("Rebeka Anastasia","tinagal di Jalan Kampung Sumur")  #init akna terpanggil  di main program
#sule = mahasiswa ()

#rebeka.nama = "Rebeka Anastasia"
#sule.nama = "Entis  Sutisna "
#print (sule.nama) # untuk mengambil nama dari template diatas
print (rebeka.nama)

rebeka.tidur ("nyenyak") #kenapa tidak menggunakan pprint########

#sule.belajar() #ini disebut method
#rebeka.belajar()
#sule.tidur ("sangat lelap")
#rebeka.tidur ("larut malam") #kalau codingannya terdaat kondisi maka semua pun harus dimasukankondisi baik sule atau rebeka