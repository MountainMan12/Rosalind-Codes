# Python program to extract GO Biological Processes for the given UniprotID
from bs4 import BeautifulSoup
import requests
import re
import glob

fh = open('data/rosalind_uniprot.txt','r')

if(fh.mode == 'r'):
    ID = str(fh.read())

r = requests.get('https://www.uniprot.org/uniprot/'+ID+'.txt')
data = r.text
soup = BeautifulSoup(data)

with open('Uniprot_'+ID+'.txt', 'w') as file:
    file.write(str(soup))

lines = []
#Read the downloaded text from Uniprot website
for file in glob.iglob('Uniprot_'+ID+'.txt'):
        for line in open(file, 'r'):
            if re.search('GO:*', line):
                lines.append(line.split('; ')[2])

#We want to only extract BP name
temp = ''
for i in range(0, len(lines)):
    temp = lines[i].split(':')[1]
    print(temp)
    temp = ''

   