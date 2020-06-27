#PROGRAM TO TRANSCRIBE DNA

dna = open('rosalind_rna.txt','r')
print('DNA SEQUENCE IS:')
if(dna.mode == 'r'):
    seq = dna.read()
    print(seq)

seq_list = list(seq)

for i in range(len(seq_list)):
    if(seq_list[i] == 'T'):
        seq_list[i] = 'U'

rna = ''.join(seq_list)
print(rna)