def funcao(num):
    
    h = num//3600
    m = (num%3600)//60
    s = num%60
    
    return h, m, s