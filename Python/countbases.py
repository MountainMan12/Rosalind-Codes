dna = open('rosalind_dna.txt','r')

seq = ''
if(dna.mode == 'r'):
    seq = dna.read()
    print(seq)

seq_list = list(seq)

A_count = int(seq_list.count('A'))
T_count = int(seq_list.count('T'))
G_count = int(seq_list.count('G'))
C_count = int(seq_list.count('C'))

print(A_count,'',C_count,'',G_count,'',T_count)
