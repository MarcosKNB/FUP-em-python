def SomaSerie(i, j, k):
    if i >= j+1:
        return 0
    else:
        return SomaSerie(i+k, j, k) + i 