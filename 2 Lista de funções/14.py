def funcao(num):
    num = int(num)
    
    c = num//100
    d = (num%100)//10
    u = num%10
    
    numf = (u*100) + (d*10) + c
    
    return numf