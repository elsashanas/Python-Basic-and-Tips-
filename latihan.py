#latihan logika dan komperasi
#membuat gabungan area rentang dari angka 

inputUser = float (input ("Masukan angka yang bernilai \n kurang dari 3\n atau\n lebih besar dari 10 \n :"))

#+++ 3 kurang dari 3
#ayo periksa angka kurang dari 3

numKurangdari = (inputUser < 3)
print (" Kurang dari 3 = ", numKurangdari )

#periksa yang lebih besar dari 10

numLebihdari = (inputUser > 10)
print (" Lebih dari 10 = ", numLebihdari )

hasil = numKurangdari or numLebihdari 
print ("Angka yang anda masukan : ", hasil )

#--- 3++++++10-----
#lebih dari 3 tapi  kurang dari 10
#irisan
inputUser = float (input ("Masukan angka yang bernilai \n lebih dari 3\n dan \n kurang dari 10 \n :"))

angkaLebihdari = (inputUser > 3)
print ("Lebih dari dari 3 = ", angkaLebihdari)

angkaKurangdari = (inputUser < 10 )
print ( "Kurang dari dari 10 = ", angkaKurangdari)

isCorrect = angkaLebihdari and angkaKurangdari
print ( " Angka yang anda masukan :" , isCorrect)

#soal
#no 1 . Angka lebih dari 0 kurang dari 5 atau kurang dari 8 lebih dari 11

x= float (input (" \n Masukan angka lebih dari 0 kurang dari 5 atau angka lebih dari 8 kurang dari 11: \n"))
angka = 0 < x < 5
print ("Angkanya adalah :", angka)
number = 8 < x < 11 
print ("Angkanya adalah :" ,number)
Status = angka or number
print ("Angka yang anda masukan berstatus :",Status)

#soal 2
# Angka yang kurang dari 0 lebih dari 5 


