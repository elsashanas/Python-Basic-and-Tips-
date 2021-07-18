#membuat aligment di string

#width and multiline
#data

data_nama = " Bang Pukis "
data_umur = 17
data_tinggi = 156
data_nomor_sepatu = 38

#data standard
data_string = f"nama = {data_nama} ,umur{data_umur} ,tinggi = {data_tinggi},nomor sepatu {data_nomor_sepatu} "
print (5*"="+"data string" + 5*"=")
print (data_string)

#data string multilie (dengan menggunakan enter)
data_string = f"nama = {data_nama} ,\numur{data_umur} ,\ntinggi = {data_tinggi},\nnomor sepatu {data_nomor_sepatu} "
print (5*"="+"data string" + 5*"=")
print (data_string)

#string multiline dengan kutip tiplets
data_String = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print (5*"="+"data string" + 5*"=")
print (data_String)

#mengatur lebarnya dengan mudah
data_nama = "Cakep"
data_String = f"""
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print (5*"="+"data string" + 5*"=")
print (data_String) 
#mengatur manual tanda sama dengan
data_nama = "Cakep"
data_String = f"""
nama   = {data_nama}
nama   = {data_nama :>6}
umur   = {data_umur :>3}
tinggi = {data_tinggi:>4}
sepatu = {data_nomor_sepatu:>3}
"""
print (5*"="+"data string" + 5*"=")
print (data_String) 

