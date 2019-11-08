import xlsxwriter
import sys
import glob

# Grab files and open workbook.

filelist = glob.glob('*.BP.txt')
workbook = xlsxwriter.Workbook('Combined' + '.xlsx')

# Format presets

header_format = workbook.add_format({
    'bold':1})
merge_format = workbook.add_format({
    'align':'center',
    'valign':'vcenter'})

for f in filelist:
    Prefix = f.split('.BP')[0]
    BP = Prefix + '.BP.txt'
    CC = Prefix + '.CC.txt'
    MF = Prefix + '.MF.txt'


    worksheet = workbook.add_worksheet(Prefix)


    ## BP Addition

    with open(BP) as infile:
        topline = infile.readline()
        topline = topline.rstrip()
        topline = topline.replace('"','')
        bpdata = []
        bpdata.append(topline)
        for lines in infile:
            lines = lines.replace('"','')
            lines = lines.rstrip()
            fdr = float(lines.split('\t')[-1])
            if fdr <= 0.05:
                bpdata.append(lines)

    worksheet.set_column(0,0,5)
    worksheet.set_column(1,1,11)
    worksheet.set_column(2,2,44)
    worksheet.set_column(3,5,15)
    worksheet.set_column(6,6,20)
    worksheet.set_column(7,7,20)

    top = bpdata[0].split('\t')
    col = 1
    row = 0
    for t in top:
        worksheet.write(row,col,t,header_format)
        col += 1
        
    row = 1
    for b in bpdata[1:]:
        col = 0
        val = b.split('\t')
        for v in val:
            worksheet.write(row,col,v)
            col += 1
        row += 1

    worksheet.merge_range('H2:H' + str(len(bpdata)),'Biological Process',merge_format)

    ## CC Addition

    with open(CC) as infile:
        topline = infile.readline()
        topline = topline.rstrip()
        topline = topline.replace('"','')
        ccdata = []
        ccdata.append(topline)
        for lines in infile:
            lines = lines.replace('"','')
            lines = lines.rstrip()
            fdr = float(lines.split('\t')[-1])
            if fdr <= 0.05:
                ccdata.append(lines)
                
    row += 1

    for c in ccdata[1:]:
        col = 0
        val = c.split('\t')
        for v in val:
            worksheet.write(row,col,v)
            col += 1
        row += 1
        
    worksheet.merge_range('H' + str(len(bpdata) + 2) + ':H' + str(len(ccdata) + len(bpdata)),'Cellular Compartment',merge_format)

    ## MF Addition

    with open(MF) as infile:
        topline = infile.readline()
        topline = topline.rstrip()
        topline = topline.replace('"','')
        mfdata = []
        mfdata.append(topline)
        for lines in infile:
            lines = lines.replace('"','')
            lines = lines.rstrip()
            fdr = float(lines.split('\t')[-1])
            if fdr <= 0.05:
                mfdata.append(lines)

    row += 1

    for m in mfdata[1:]:
        col = 0
        val = m.split('\t')
        for v in val:
            worksheet.write(row,col,v)
            col += 1
        row += 1
        
    worksheet.merge_range('H' + str(len(bpdata) + len(ccdata) + 2) + ':H' + str(len(ccdata) + len(bpdata) + len(mfdata)),'Molecular Function',merge_format)
    
workbook.close()
