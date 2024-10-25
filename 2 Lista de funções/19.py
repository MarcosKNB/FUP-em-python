def funcao(d):
    d = int(d)
    
    n100 = d//100
    dr1 = d % 100
    n50 = dr1//50
    dr2 = dr1 % 50
    n20 = dr2//20
    dr3 = dr2%20
    n10 = dr3//10
    dr4 = dr3%10
    n5 = dr4//5
    dr5 = dr4%5
    n2 = dr5//2
    dr6 = dr5%2
    
    return n100, n50, n20, n10, n5, n2, dr6