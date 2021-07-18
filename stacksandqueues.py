#kalian bisa pakai untuk penumpukan antrian atau penumpukan data
#stacks adalah penumupukan yang diambil dari paling atas
#queues adalah antrian 

tumpukan = [1,2,3,4,5,6]
print ("data sekarang :",tumpukan)
tumpukan.append(7)
print ("data masuk :",7)
tumpukan.append(8)
print("data masuk :",8)

#stacking
#mengambil data yang paling akhir tapi gatau panjangnya berapa
out = tumpukan.pop()
print ("data keluar adalah :",out)
print("data sekarang :",tumpukan)

#queque
#karena kita gaada function build in di python buat que makanya kita pakai library ini
from collections import deque
from typing import Deque 
#collections using s

antrian = deque([1,2,3,4,5])
print ("data sekarang :",antrian)

#menambahkan data
antrian.append(6)
print ("data masuk adalah :",6)
print ("data sekarang adalah :",antrian)

antrian.append(7)
print ("data masuk adalah :",7)
print ("data sekarang adalah :",antrian) 

#untuk mengurangi antrian
out = antrian.popleft()
print ("data keluar adalah:",out)
print ("data sekarang adalah :",antrian)

out = antrian.popleft()
print ("data keluar adalah:",out)
print ("data sekarang adalah :",antrian)

#buat stacks

buku_perpus = [1,2,3,4,5,6,7]
print ("andtrian di bisokop sekarang adalah : ",buku_perpus)

buku_perpus.append (8)
print ("antrian bioskop bertambah menjadi :" , buku_perpus)

buku_perpus.pop()
print ("nomer antrian yang sudah masuk ke dalam adalah :",buku_perpus)





