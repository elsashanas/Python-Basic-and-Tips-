#set,himpunan:
#untuk memudahkan data yang banyak dan dpuble double
superhero = {"batman",
             "spirderman",
             "si buta dari goa hantu"
             ,"gundala",
             "gatot kaca"}
print (superhero)
superhero.add("captain america")
superhero.add("gundala")
print(superhero) 
#himpunan itu tidak mementingkan urutan dan tidak akan memerhatikan jumlahnya ada berapa banyak
#cara ke 2
superhero = set()
superhero.add ("wirosableng")
superhero.add ("gundala")
superhero.add ("catwomen")
superhero.add ("satria bajaj hitam")
#superhero.add(123) #bisa menggunakan int juga
print (superhero)

#cara mengurutkan 
print (sorted(superhero))
#print (superhero[1]) # ini akan eror karena set tidak support indexing

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {1,3,5,7,11}

print(ganjil.union(genap))
print (ganjil.intersection(genap))
print (ganjil.intersection(prima))

