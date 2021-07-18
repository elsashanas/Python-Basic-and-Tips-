#inheritance adlah pewarisan

class Motor :
    def __init__(self,nama,merk,jangkauan) :
        self.nama = nama
        self.merk = merk
        self.jangkauan = jangkauan 

    def cek_id_motor (self) :
        print ("nama :",self.nama,"\nmerk :",self.merk,"\njangakauan :",self.jangkauan)

class Gojek(Motor):

    def cek_id_motor(self):
       print ("Merupakan motor yang akan dipakai untuk menjadi Ojol")

merek1 = Motor ("Mario", "Yamaha","30KM")
merek2 = Motor ("Farhan", "Yamaha","50KM") #ini akan tetap bisa run karena gojek = motor artinya gojek include motor
merek3 = Gojek ("Aisyah", "Honda", "60KM")

merek1.cek_id_motor() #karena sudah print di atas makanya gausah di print lagi
merek2.cek_id_motor()
merek3.cek_id_motor()


