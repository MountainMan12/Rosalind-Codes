#Python program to count nucleotides

fh = open('data/rosalind_ini.txt','r')
seq = ''
if(fh.mode == 'r'):
    seq = str(fh.read())
fh.close()

print('A_count = ',seq.count('A'))
print('T_count = ',seq.count('T'))
print('G_count = ',seq.count('G'))
print('C_count = ',seq.count('C'))
