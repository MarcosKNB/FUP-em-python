def funcao(num):
    num = int(num)
    
    m = num//1000
    c = (num%1000)//100
    d = (num%100)//10
    u = num%10
    
    return m, c, d, u