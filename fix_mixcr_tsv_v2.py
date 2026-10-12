import sys

def removeScore(x):
    x_list = x.split(',')
    for i in range(0,len(x_list)):
        x_list[i] = x_list[i].split('(')[0]
        x = ','.join(x_list)
    return(x)
    
for line in open(sys.argv[1], 'r'):
    line = line.replace('WithScore', '')
    line_list = line.rstrip().split('\t')
    line_list[5] = removeScore(line_list[5])
    line_list[6] = removeScore(line_list[6])
    line_list[7] = removeScore(line_list[7])
    line_list[8] = removeScore(line_list[8])
    if line_list[1] == 'readCount':
        print ('\t'.join(line_list))
    elif float(line_list[1]) >= 3:
        print ('\t'.join(line_list))    
