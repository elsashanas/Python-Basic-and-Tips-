#kalau kita punya program dalam satu file itu disebut modul
#untuk mulri file 
#ini cara import modul
#import modul juga sudah ada banyak misalnya modul math,os,sys
import modulimport
print (modulimport.data)

modulimport.cek_modul()

modulimport.kurang(3,7)
modulimport.tambah (3,7) 

#cara lain import (2)
import modulimport as mi
mi.tambah(3,7)

#cara lain import (3)
from modulimport import tambah , kurang
tambah (3,7)
kurang (3,7)

from modulimport import tambah as t 
t (3,4)
#kalau mau import smeuanya 
from modulimport import * 




