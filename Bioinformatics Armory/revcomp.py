#Python code to check for number of reverse compliments in fasta file

from Bio import SeqIO
from Bio.Seq import Seq

seq = []
cnt = 0
response = 0
def reverse_comp(nucleotide):
    flag = int(0)
    revcomp = nucleotide[::-1].complement()
    if(revcomp == nucleotide):
        flag = int(1)
    
    return flag


for record in SeqIO.parse('data/rosalind_rvco.txt', 'fasta'):
    seq.append(record.seq)

for i in range(0, len(seq)):
    response = reverse_comp(seq[i])
    if(response == int(1)):
        cnt += 1
    else:
        continue

print(cnt)