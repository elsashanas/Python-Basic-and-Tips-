#perbedaan function with argument adalah
def siswa(nama):
    print ("siswa ini bernama:",nama)

siswa ("mario")

#fungsi dengan menggunakankeywords argumen

def guru(nama,matkul) :
    print ("guru ini bernama:",nama,"\ndan mengajar matkul",matkul)
guru(nama='bu iswi' , matkul="kimia")
guru(matkul="bahasa indonesia" , nama= "bu neli")

#fungsi dengan default kamu argumen

def penjaga_sekolah(nama,shift="pagi",sikap="sopan"): #kalaupun argument nya sudah diisi akan tetep bisa di ganti 
    print ("nama penjaga sekolah:",nama,",penjaga di shift :",shift , ",sikap yang dia service :",sikap)
#contoh mengganti arguement
penjaga_sekolah(nama = "entis", shift= "pagi")
penjaga_sekolah(nama = "jajang", shift= "pagi",sikap="kurang baik")
#contoh biasa
penjaga_sekolah(nama = "supri")
penjaga_sekolah(nama = "jajang", shift= "malam",sikap="kurang baik")

penjaga_sekolah(shift="siang") #ini akan eror karena missing one value yaitu nama 





