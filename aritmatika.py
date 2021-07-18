#Operasi aritmatika

a= 20
b = 3
#operasi tambah
hasil = a + b 
print (a,'+',b,'=',hasil )

#operasi minus
hasil = a - b 
print (a,'-',b,'=',hasil )

#operasi minus
hasil = a * b 
print (a,'*',b,'=',hasil )

#operasi pembagian
hasil = a / b 
print (a,'/',b,'=',hasil )

#operasi eskponen (pangkat)
hasil = a ** b 
print (a,'**',b,'=',hasil )

#operasi modulus (sisa pembagian)
hasil = a % b 
print (a,'%',b,'=',hasil )

#operasi floar divisiom (pembulatan dari pembagian misal 3.3 jadi 3)
hasil = a // b 
print (a,'//',b,'=',hasil )

#prioritas operasi

x = 3
y= 2
z= 4

hitung = x * y // z ** x + x - z / y % z 
print (x ,'*', y, '//', z ,'*', x ,'+', x, '-', z, '/' ,y, '%' ,z ,'=', hitung)

hitung = x * y // z ** (x + x) - z / y % z 
print (x ,'*', y, '//', z ,'*', x ,'+', x, '-', z, '/' ,y, '%' ,z ,'=', hitung)

#urutan dari prioritas dalam artimatika adalah 
#()
# eksponen (perpangkatan)
# perkalian and stuff
# pertambahan 

#oke ini yang simple

hasil = x * y + z
print (x,'*',y,'+',z, '=', hasil)
#ini yang prioritas 
hasil =( x * y) + z
print ('(',x,'*',y,')+',z, '=', hasil)

