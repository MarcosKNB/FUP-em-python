def soma_vetores(vetor1, vetor2):
    vetorf = {} 
    vetorf['x'] = vetor1[0]+ vetor2[0]
    vetorf['y'] = vetor1[1] + vetor2[1]
    vetorf['z'] = vetor1[2] + vetor2[2]
    return vetorf
vetor1 = []
vetor2 = []
for i in range(3):
    vetor1.append(float(input()))
for i in range(3):
    vetor2.append(float(input()))
print(soma_vetores(vetor1, vetor2))