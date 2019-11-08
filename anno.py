import sys

anno = 'TAIR10_Gene.mapping'
tair = {}

with open(anno) as infile:
    for lines in infile:
        lines = lines.rstrip()
        values = lines.split('\t')
        tair[values[0]] = values[1].split(',')[0]
        
with open(sys.argv[1]) as infile:
    for lines in infile:
        lines = lines.rstrip()
        values = lines.split('\t')
        newlist = []
        for v in values:
            try:
                newlist.append(tair[v])
            except:
                newlist.append(v)
        print('\t'.join(newlist))
