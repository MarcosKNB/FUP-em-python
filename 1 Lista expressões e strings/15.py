s = int(input())

horas = s//3600
sr1 = s % 3600
minutos = sr1//60
sr2 = sr1 % 60

print (horas)
print (minutos)
print (sr2)