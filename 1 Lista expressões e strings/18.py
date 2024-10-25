d = int(input())

notas100 = d//100
dr1 = d % 100
notas50 = dr1//50
dr2 = dr1 % 50
notas20 = dr2//20
dr3 = dr2%20
notas10 = dr3//10
dr4 = dr3%10
notas5 = dr4//5
dr5 = dr4%5
notas2 = int(dr5/2)
dr6 = dr5%2

print (notas100)
print (notas50)
print (notas20)
print (notas10)
print (notas5)
print (notas2)
print (dr6)