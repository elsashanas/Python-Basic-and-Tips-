#operator tambahan
#operasi bitwise adalah operasi biner

a = 9
b = 5

#operator bitwise or (|)
c = a|b
print ('\n ===== OR ====')
print ('nilai :' , a,' , binary :' , format (a,'08b'))
print ('nilai :' , b ,' , binary :' , format (b,'08b'))
print ('------------------------------------- (|)')
print ('nilai :' ,c ,' ,  binary :' , format (c,'08b'))

#bitwise AND
c = a & b
print ('\n ===== AND ====')
print ('nilai :' , a,' , binary :' , format (a,'08b'))
print ('nilai :' , b ,' , binary :' , format (b,'08b'))
print ('------------------------------------- (&)')
print ('nilai :' ,c ,' ,  binary :' , format (c,'08b'))

#bitwise XOR 
c = a ^ b
print ('\n ===== AND ====')
print ('nilai :' , a,' , binary :' , format (a,'08b'))
print ('nilai :' , b ,' , binary :' , format (b,'08b'))
print ('------------------------------------- (^)')
print ('nilai :' ,c ,' ,  binary :' , format (c,'08b'))

#operator Shift Right
c = a >> 2
print ('\n ===== >> ====')
print ('nilai :' , a,' , binary :' , format (a,'08b'))
print ('------------------------------------ (>>)')
print ('nilai :' ,c ,' ,  binary :' , format (c,'08b'))

#operator Shift Left
c = a << 2
print ('\n ===== << ====')
print ('nilai :' , a,' , binary :' , format (a,'08b'))
print ('------------------------------------ (<<)')
print ('nilai :' ,c ,' ,  binary :' , format (c,'08b'))

#you still have to do a not bitwise or flip XOR 

