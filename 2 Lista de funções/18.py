def funcao(v1, v2, v3, vp):
    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)
    vp = float(vp)
    
    vt = v1 + v2 + v3
    
    vp1 = (v1*vp)/vt
    vp2 = (v2*vp)/vt
    vp3 = (v3*vp)/vt
    return vp1, vp2, vp3
