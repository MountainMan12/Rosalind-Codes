#Python program to convert fastq sequence to fasta 
from Bio.SeqIO.QualityIO import FastqGeneralIterator

with open('data/rosalind_tfsq.txt','r') as fh:
    for title, seq, qual in FastqGeneralIterator(fh):
        print('>'+title)
        print(seq)
fh.close()       
