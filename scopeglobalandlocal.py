#bisa berguna untuk mengubah variabel atau memproteksi sebuah variabel

#scope variable : local
nama_kucing = "cassandra"

def ubah_nama(nama_baru):
    nama_kucing = nama_baru
    print ("saya mengubah nama kucing",nama_kucing)

ubah_nama("Kattie")
print ("nama kucing saya menjadi :",nama_kucing)