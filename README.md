# Burks Network Enrichment Pipeline Scripts and Workflow
## Collection of Python/R Scripts for batch enrichment of MCL-Cluster Files

### Sample Workflow
Generate a series of gene clusters using the MCL suite.
Assuming you start with a simple abc format file (network.abc):
```
mcxload -abc network.abc --stream-mirror -write-tab network.tab -o network.mci
mcl network.mci -I 1.5
mcxdump -icl out.network.mci.I15 -tabr network.tab -o dump.network.mci.I15
```
Perform batch enrichment on all clusters with Universe.txt containing only the genes in your network.
Optional: Use FDR-adjustment script to in-place convert all output to FDR-adjusted p-values.
```
RScript --vanilla batchGO.R dump.network.mci.I15
for x in cluster.*
do Rscript --vanilla fdrmaker.R $x
done
```
Convert tables to Formatted Excel Files and Gene Lists
```
python3 loop_excel_mapper.py
python3 loop_excel_lister.py dump.network.mci.I15
```



#### Optional 
Use mapping file to re-annotate network file prior to Excel conversions.
```
python3 anno.py dump.network.mci.I15 > dump.anno.network.mci.I15
python3 loop_excel_lister.py dump.anno.network.mci.I15
```
Use batchgo_custom.R for custom annotations.  An example map file is provided.
