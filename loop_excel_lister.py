import xlsxwriter
import sys


# Grab files and open workbook.

importfile = sys.argv[1]
clusters = []
with open(importfile) as infile:
    for lines in infile:
        lines = lines.rstrip()
        clusters.append(lines)
        
workbook = xlsxwriter.Workbook('Gene_Lists' + '.xlsx')

# Format presets

header_format = workbook.add_format({
    'bold':1,
    'font_size':10,
    'font_name':'Arial'})

def_format = workbook.add_format({
    'font_size':10,
    'font_name':'Arial'})

i = 0
for clu in clusters:
    i += 1
    row = 1
    valz = clu.split('\t')
    if len(valz) < 25:
        continue
    worksheet = workbook.add_worksheet(str(i))
    worksheet.write(0,0,'Gene Name',header_format)
    for v in valz:
        worksheet.write(row,0,v,def_format)
        row += 1
    
workbook.close()
