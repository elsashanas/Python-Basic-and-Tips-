nilai = 75
nilai2=80
nilai3=90

if nilai == 75 : #samadengan nya harus 2 
    print ("makan nilai kamu adalah ",nilai)
    
    if nilai2 == 80 :
     print ("maka nilai kamu adalah : ",nilai2)
     
     #print gaboleh sejajar dengan if
     if nilai3 == 90 :
         print ("maka nilai anda adalah :" , nilai3)


nilai = 100
if 80 <= nilai <= 100:
    print ("Nilai anda adalah : A")
elif 70 <= nilai < 80:
    print ("Nilai anda adalah : B")
elif 60 <= nilai < 70:
    print ("Nilai anda adalah : C")
elif 50 <= nilai <= 60:
    print ("Silahkan melakukan perbaikan")
else :
    print ("Maaf anda tidak lulus mata kuliah ini")


#pembelian makanan
makanan = ["bakwan","sushi","esteh","cireng"]
beli = "mangga"
#beli in makanan , jika yang di beli ada di makanan
if beli in makanan: #harus pakai tanda : untuk mastiin si if nya ini
 print ( 'Mamang : Ya saya jual',beli )
else :
 print ( 'Mamang : Maaf saya jual',beli ) #bisa pake else atau if not more easier for you

masker = ["camille","sleepover","layskin","bemahiraskin","daisy"]
beli = "makanan"
if beli in masker:
 print ( 'Mamang : Ya saya menjual',beli)
if not beli in masker :
     print ( 'Maaf saya tidak menjual',beli)
#jadi if itu harus sejajar satu sama lain karena menghubungkan if pertama dengan if kedua




