#belajar format string

#contoh generic
nama = "cakeup"
format_str = f"hello {nama}" #biar lebih simple gausah bikin hello satusatu
print (format_str)

# angka
angka=2002.2
format_str = "angka  = " + str(angka) #pake str untuk ke casting
print (format_str)

#boolean
boolean = True
format_str = f"boolean = {boolean}"
print (format_str)

#nah kalo pakai format lebih easy
angka = 2002.5
format_str = f"angka = {angka}" #f nya gabole space sama class nya
print (format_str)
#kalau angka yang mau ditampilin angka bilbul ajaa
angka = 19
format_str= f"angka =  {angka}"
print (format_str)
#gabisa print kalau angkanya terdapat koma karena angka yang di print adalah int
#kalo  mau ubah int nya jadi float biar kalau ada koma bisa di print aja

#bilangan ribuan
angka = 300000
format_str = f"angka = {angka :,}" #fungsi tiitk dua koma biar angkanya itu ada space anatara koma keribuan
print (format_str)

#untuk bilangan decimal
angka = 19.1919
format_str = f"desimal = {angka :.3f}" #fungsi (:.) adalah untuk ngebuat nentuin ada berapa angka di belakang koma yang akan di print
print (format_str)

#leading zero (depannya berapa)
angka = 190402.19191
format_str = f"desimal = {angka :12.3f}" #fungsi (:.) adalah untuk ngebuat nentuin ada berapa angka di belakang koma yang akan di print
print (format_str)                     # dan f itu adalah float
#fungsi 0 adalah menambahkan angka 0 di paling depan

#menampilkan tanda + atau -
angka_minus = - 10
angka_plus = 10
format_minus = f"angka minus {angka_minus :-d}"
format_plus = f"angka plus {angka_plus :+d}" #fungsi dari (:+d) untuk memunculkan angka minus dan plus nya

print (format_minus)
print (format_plus)

#memformat persen

#persentase dalam koma
persentase = 0.12345
format_persentase = f"angka persentase {persentase :.2%}" #angka dua di belakang koma biar ga kepanjangan 0 nya 
print (format_persentase)

#melalukan operasi aritmatika di dalam placeholder (kurung kurawal)
harga = 10000
jumlah = 5
format_string = f"harga total = Rp.{harga*jumlah :,}"
print (format_string)

#format angka lain seperti (binary ,octal,hexadecimal)
angka = 255
format_binary = f"binary = {bin (angka)}"
format_octal = f"binary = {oct(angka)}"
format_hexadecimal = f"binary = {hex(angka)}"

print (format_binary)
print (format_octal)
print (format_hexadecimal)


