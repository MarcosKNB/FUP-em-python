idade = int(input())
tempo = int(input())

if idade >= 65 or tempo >= 30:
    print('Pode se aposentar')
    
elif idade >= 60 and tempo >= 25:
    print('Pode se aposentar')
else:
    print('Nao pode se aposentar')