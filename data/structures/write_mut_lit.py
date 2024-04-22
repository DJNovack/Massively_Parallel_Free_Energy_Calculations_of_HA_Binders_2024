import os,sys
file = sys.argv[1]
inde = ['R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'G', 'P', 'A', 'V','I', 'L', 'M', 'F', 'Y', 'W']
sequence = open(file,'r').readlines()[0].strip('\n')
f=open('mut_list.txt','w')
for i,aa in enumerate(sequence):
    f.write(f'B.{aa}.{270+i} B\n')
f.close()

f=open('res_list.txt','w')
for i,aa in enumerate(inde):
    f.write(f'{aa}\n')
f.close()
