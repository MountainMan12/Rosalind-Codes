# PROGRAM TO FIND SEQUENCE WITH THE HIGHEST GC-CONTENT FROM A FASTA FILE
from Bio import SeqIO

meta = []
dna = []

for sequence in SeqIO.parse('data/rosalind_gc.txt', 'fasta'):
        meta.append(sequence.id)
        dna.append(str(sequence.seq))
        
gc_content = []
temp = 0

for i in range(0, len(dna)):
        temp = float((dna[i].count('G')+dna[i].count('C'))/(dna[i].count('G')+dna[i].count('C')+dna[i].count('A')+dna[i].count('T')))*100
        gc_content.append(temp)
        temp = 0

max_gc = max(gc_content)
seq_id = meta[int(gc_content.index(max_gc))]

print(seq_id)
print(max_gc)


