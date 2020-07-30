#Python program to find hamming distance between 2 DNA sequences

fh = open('data/rosalind_hamm.txt','r')

if(fh.mode == 'r'):
    dna = fh.read().split('\n')


seq1 = dna[0]
seq2 = dna[1]

dis = 0
for i in range(0, len(seq1)):

    if(seq1[i] == seq2[i]):
        continue
    else:
        dis += 1

print(dis)