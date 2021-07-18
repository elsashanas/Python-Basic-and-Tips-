class belanja():

    branch = "Pondok Bambu"
    tambah_barang = 0 

    def __init__(self,input_belanjaan , input_kd):
        self.belanjaan=input_belanjaan
        self.kodebarang=input_kd
        belanja.tambah_barang +=1 

#main programnya adalah :
#segala sesuatu yang ada self nya adalah milik instance
Keysha = belanja("Roma Sari Gandum" , 4502)
Kenzy = belanja ("Malkist Coklat ", 45002)
Alvaro = belanja ("Buah Mangga", 1212)

#kita dapat mengubah branch dengan code ini
#belanja.branch = "Jatiwaringin"
#kalau mau ubah salah satu nya bisa dengan
#Keysha.branch = "Pondok Kelapa"

print (belanja.branch)
print (belanja.branch)
print (Keysha.branch)
print (belanja.tambah_barang)

