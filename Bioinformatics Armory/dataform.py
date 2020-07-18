from Bio import Entrez

id = []

with open('data/rosalind_frmt.txt','r') as fh:
    if(fh.mode == 'r'):
        id.append(fh.read().split(' '))
fh.close()

id = id[0] #Convert a nested list to a single list

print('Please do not send more than 3 requests per second')

email = input('Please enter your email ID first! GenBank wants to know who you are: ')

Entrez.email = email
handle = Entrez.efetch(db="nucleotide", id=id, retmode="xml")
record = Entrez.read(handle)
handle.close()


min_len = [] #Stores nucleotide seq lengths
for i in range(0, len(id)):
    min_len.append(int(record[i]["GBSeq_length"]))

min_id = min_len.index(min(min_len))
#Output results for the record with minimum nucleotide sequence length
acc = record[min_id]["GBSeq_accession-version"]
desc = record[min_id]["GBSeq_definition"]
seq = str(record[min_id]["GBSeq_sequence"]).upper()

print('>'+acc+' '+desc)
print(seq)

    