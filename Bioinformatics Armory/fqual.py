# Python program to count sequences will low quality i.e. below the specified threshold

from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator

def Average(lst): 
    return sum(lst) / len(lst)

thresh = int(0)
cnt = int(0)

with open('data/rosalind_phre.txt','r') as fh1:
    thresh = int(fh1.readline()) #extract threshold
fh1.close()

with open('data/rosalind_phre.txt','r') as fh2:
    next(fh2) #Skip first line for reading fastq file
    for record in SeqIO.parse(fh2, "fastq"):
        if(Average(record.letter_annotations["phred_quality"]) < thresh):
            cnt += 1
fh2.close()

print(cnt) #Number of reads with average quality below threshold
        







