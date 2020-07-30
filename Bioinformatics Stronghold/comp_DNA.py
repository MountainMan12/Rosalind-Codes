#PROGRAM TO COMPLEMENT A DNA STRAND

dna = open('data/rosalind_revc.txt','r')

print('The forward strand od DNA is:')

if(dna.mode == 'r'):
    seq = dna.read()
    print(seq)

#COMPLEMENT OF DNA
seq_list = list(seq)

for i in range(len(seq_list)):
    if(seq_list[i] == 'A'):
        seq_list[i] = 'T'
    elif(seq_list[i] == 'T'):
        seq_list[i] = 'A'
    elif(seq_list[i] == 'G'):
        seq_list[i] = 'C'
    elif(seq_list[i] == 'C'):
        seq_list[i] = 'G'

print('Complement of froward strand:')
rev_seq = seq_list[::-1]
rev_str = ''.join(rev_seq)
print(rev_str)
