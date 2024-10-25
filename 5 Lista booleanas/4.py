num = int(input())

if num % 3 == 0 and num%5 != 0:
    print ('True')
elif num % 3 != 0 and num%5 == 0:
    print ('True')
else:
    print('False')