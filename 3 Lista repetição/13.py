def funcao(x):
    numanterior = 1
    numseguinte = 0
    numatual = 0
    for contador in range(x):
        numseguinte = numatual + numanterior
        numanterior = numatual
        numatual = numseguinte
    return numatual