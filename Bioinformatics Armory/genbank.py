from Bio import Entrez

fh = open('data/rosalind_gbk.txt','r')
gb = []
if(fh.mode == 'r'):
    gb.append(fh.read().split('\n'))
fh.close()

print('Please do not send any more than 3 requests per second')

email = str(input('Please enter your email ID: ')) #Enter your email ID first 

Entrez.email = email 
handle = Entrez.esearch(db="nucleotide", term= str(gb[0][0])+'[Organism] AND '+str(gb[0][1])+'[Publication Date] : '+str(gb[0][2])+"[Publication Date]")

record = Entrez.read(handle)

print(record["Count"])