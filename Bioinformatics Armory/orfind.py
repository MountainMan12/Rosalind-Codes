#Python program to find the longest protein string that can be translated from an ORF 

from Bio.Seq import translate
from Bio.Data import CodonTable


standard_table = CodonTable.unambiguous_dna_by_id[1]
start_codons = standard_table.start_codons

sense_strand = ''

with open('data/rosalind_orfr.txt') as fh:
    sense_strand = fh.readline().rstrip('\n')

ant_sense = sense_strand[::-1]
ant_sense = ant_sense.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T') 
ant_sense = ant_sense.replace('G', '%temp%').replace('C', 'G').replace('%temp%', 'C')


def get_max_orf(dna):

    start_pos = []

    for i in range(0, 3):
        for index,value in enumerate(dna):
            value = 'ATG'
            if(dna[index:index+3] == value):
                start_pos.append(index)

    start_pos.sort()

    temp_dna = []
    temp = ''
    for i in range(0, len(start_pos)):
        temp = dna[start_pos[i]:]
        temp_dna.append(temp)

    max_l = 0
    temp_protein = ''
    max_protein = ''
    for j in range(0, len(temp_dna)):
        temp_protein = translate(temp_dna[j], table=1, to_stop=True)
        if(len(temp_protein) > max_l):
            max_protein = temp_protein
            max_l = len(temp_protein)
        else:
            continue

    return(max_protein)


forward_protein = get_max_orf(sense_strand)
reverse_protein = get_max_orf(ant_sense)
print('The longest ORF in the forward strand is: ', forward_protein)
print('The longest ORF in the reverse strand is: ', reverse_protein)

