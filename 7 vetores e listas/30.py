def funcao(vetor):
    tam_vetor = len(vetor)
    if tam_vetor < 2:
        return -1, -1, -1
    
    max_tam = 0
    inicio1 = -1
    inicio2 = -1
    for tam_seg in range(2, tam_vetor):
        for i in range(tam_vetor - tam_seg + 1):
            segmento1 = vetor[i:i+tam_seg]
            
            for j in range(i + 1, tam_vetor - tam_seg + 1):
                segmento2 = vetor[j:j + tam_seg]
                
                if segmento1 == segmento2 and tam_seg > max_tam:
                    max_tam = tam_seg
                    inicio1 = i
                    inicio2 = j
                    break
                    
    if max_tam == 0:
        return -1, -1, -1
    else:
        return inicio1, inicio2, max_tam