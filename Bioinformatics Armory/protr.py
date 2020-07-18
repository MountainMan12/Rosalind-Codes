#Python program to return index of genetic code variant used for translation

from Bio.Seq import translate

seq = []

with open('data/rosalind_ptra.txt','r') as fh:
    if(fh.mode == 'r'):
        seq.append(fh.read().split('\n'))

seq = seq[0]

nuc = seq[0]
prot = seq[1]

trans_prot = []
ids = [1,2,3,4,5,6,9,10,11,12,13,14,15] #Existing table IDs
for i in ids:
    trans_prot.append(translate(nuc, table=i, to_stop=True))

index = []
#Check which index matches the original protein sequence 
for i in range(0, len(trans_prot)):
    if(trans_prot[i] != prot):
        continue
    else:
        index.append(i)

print(ids[index[0]]) #Return the first matched table ID
