### IMPORTS AND DEPENDENCIES
import os
from Bio import SeqIO
import subprocess
import sys

configfile: "config.yaml"


### GLOBAL VARIABLES

# define genomic region from config file
GR = config['genomic_region']

# confirm there is only 1 file in input folder and define it as INPUT
if len(os.listdir('input')) > 1:
    sys.exit('ERROR: more than 1 file in the input folder')
else:
    INPUT = os.listdir('input')[0]

# get ids from the INPUT file (which is as msa)
MSA = SeqIO.parse('input/{}'.format(INPUT), 'fasta')
IDS = [seq.id for seq in MSA]


### SUBTYPER

rule subtype_all:
    input:
        trees=expand("trees/{sample}.treefile", sample=IDS)
    output:
        "all_subtyped.csv",
        "report_all_subtyped.csv"
    script:
        "scripts/output_subtype.py"


rule tree_maker:
    input:
        "aligned/aligned_{sample}.fasta"
    output:
        "trees/{sample}.treefile"
    priority:
        50
    threads: 2
    shell:
        "python scripts/tree_maker.py -i '{input}' -g {GR}"


###ALIGNER

rule align_all:
    input:
        files = expand("aligned/aligned_{sample}.fasta", sample=IDS)
    output:
        "all_aligned.fasta"
    script:
        "scripts/concatenator.py"


rule map_and_align:
    input:
        "split/{sample}.fasta"
    output:
        "aligned/aligned_{sample}.fasta"
    shell:
        "python scripts/align_and_map.py -i '{input}' -o '{output}' -g {GR}"



rule split:
    input:
        "input/{}".format(INPUT)
    output:
        expand("split/{sample}.fasta", sample=IDS)
    script:
        "scripts/spliter.py"


# write save and clean intermidiate files

rule delete_interm_files:
    params:
        "inter"
    shell:
        "python scripts/cleaner.py -w {params}"

rule delete_all_outputs:
    params:
        "all"
    shell:
        "python scripts/cleaner.py -w {params}"


rule compress_and_del_inter_files:
    params:
        "c_inter"
    shell:
        "python scripts/cleaner.py -w {params}"

rule compress_all:
    params:
        "c_all"
    shell:
        "python scripts/cleaner.py -w {params}"