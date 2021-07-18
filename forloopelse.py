#belajar for,loop,else ,range , break

for a in range (0,30,5): # angka lima adalah inchrement
    print (a)

#misal ingin mencari angka 
angka = 35
for a  in range (0,40,5):
      print (a)
      if a is angka:
          print ("angka yang anda masukan = ", a , "dapat di temukan ")
        
#kita akan menggunakan break untuk berhenti di 25
          break 
        #diletakan di bawah print (break berfungsi untuk keluar dari prroses looping)
else:
    print ("angka yang anda masukan =", angka , "tidak di temukan")

#fungsi else adalah untuk menyatakan angka yang tidak ada dalam looping dan memastikan bahwa looping berjalan dari awal sampai akhir


number = 20
for n in range (0,50,5):
    print (n)
    if n is number :
        print ("angka yang anda masukan" , n ,"dapat ditemukan" )
        break
else :
    print ("angka yang anda masukan " , number , "tidak dapat ditemukan")

jumlah = 31
for j in range (0,60,5):
    print (j)
    if j is jumlah:
        print ("angka yang anda masukan = " , j , "dapat di temukan ")
        break
else:
    print ("angka yang anda masukan = " , jumlah , "tidak dapat di temukan ")








