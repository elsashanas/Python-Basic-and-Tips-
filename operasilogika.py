## operasi logika di boolean

# not,or, and , xor

#not
print (" == NOT == ")
a = True
c = not a 
print (" data a =" ,a)
print (' -NOT- ')
print ('data c = ', c)

a = False
c = not a 
print (" data a =" ,a)
print (' -NOT- ')
print ('data c = ', c)

# OR 
#jika salah satu True hasilnya adalah True

print ( ' ---- OR ----')
a= True
b= False 
c= a or b 
print ( a, 'or', b ,'=',c)

a= True
b= True
c= a or b 
print ( a, 'or', b ,'=',c)

a= False
b= False
c= a or b 
print ( a, 'or', b ,'=',c)

a= False
b= True
c= a or b 
print ( a, 'or', b ,'=',c)

#AND 
#jika salah satau False hasil adalah False

print ( ' ---- AND ----')
a= True
b= False 
c= a and b 
print ( a, 'and', b ,'=',c)

a= True
b= True
c= a and b 
print ( a, 'and', b ,'=',c)

a= False
b= False
c= a and b 
print ( a, 'and', b ,'=',c)

a= False
b= True
c= a and b 
print ( a, 'and', b ,'=',c)

#XOR
#jika salah satau True maka hasil True
#apabila ada dua True dia false

print ( ' ---- XOR ----')
a= True
b= False 
c= a ^ b 
print ( a, 'XOR', b ,'=',c)

a= True
b= True
c= a ^ b 
print ( a, 'XOR', b ,'=',c)

a= False
b= False
c= a ^ b 
print ( a, 'XOR', b ,'=',c)

a= False
b= True
c= a ^ b 
print ( a, 'XOR', b ,'=',c)