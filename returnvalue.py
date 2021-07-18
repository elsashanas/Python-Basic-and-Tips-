#return valueadalah sebuah function yang dapat memberikan nilai value

def makanan(berat):
    harga = 30000
    tot_makanan = berat*harga
    print("harga satuan adalah :",harga,"\ntotal yang harus anda bayarkan adalah :",tot_makanan)
makanan (3)

def kuadrat (argumen):
    total = argumen**2
    print ("nilai kuadrat dari",argumen,"adalah:",total)
    return total
a = kuadrat (4)
print (a) 
print (kuadrat(4)) #atau bisa buat lebih simple dengan cara langsung print aja

print ('-'*30)

#fungsi dengan return value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1+argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total
a=tambah(3,4)
print (a)
#perkalian
def kali(argumen1,argumen2):
    total = argumen1*argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total
print (kali(4,a))
#atau bisa juga di satuin
print (kali(3,tambah(3,4)))

