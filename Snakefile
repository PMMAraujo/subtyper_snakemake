### IMPORTS AND DEPENDENCIES
import os
from Bio import SeqIO
import subprocess

configfile: "config.yaml"


### GLOBAL VARIABLES

# define genomic region from config file
GR = config['genomic_region']

# list file in input folder and use the first one
INPUT = os.listdir('input')[0]

# pick up the file in th INPUT variable wich is an MSA and 
# extract the sequences ids from it
MSA = SeqIO.parse('input/{}'.format(INPUT), 'fasta')
IDS = [seq.id for seq in MSA]


### SUBTYPER


rule subtype_all:
    input:
        sho=expand("subtype/short_{sample}.txt", sample=IDS),
        lon=expand("subtype/long_{sample}.txt", sample=IDS)
    output:
        "all_subtyped.txt",
        "with_neighbors_all_subtyped.txt"
    run:
        def my_func():
            for file in input.sho:
                with open(file, 'r') as in_file:
                    yield in_file.read()

        with open(output[0], 'w') as out_file:
            out_file.write(''.join(my_func()))


        def my_func():
            for file in input.lon:
                with open(file, 'r') as in_file:
                    yield in_file.read()

        with open(output[1], 'w') as out_file:
            out_file.write(''.join(my_func()))



rule subtype:
    input:
        "trees/{sample}.parstree"
    output:
        sho="subtype/short_{sample}.txt",
        lon="subtype/long_{sample}.txt"
    shell:
        "python scripts/get_sub.py -i {input} -s {output.sho} -l {output.lon}"



rule tree_maker:
    input:
        "aligned/aligned_{sample}.fasta"
    output:
        "trees/{sample}.parstree"
    run:
        name = input[0].split('_')[-1].split('.')[0]
        subprocess.call('cat {0} data/subtype_refs.fasta > trees/msa_{1}.fasta ; iqtree -nt 2 -s trees/msa_{1}.fasta -m GTR+G4 -g data/backbone_bestTree.result -redo -pre trees/{1} -quiet'.format(input[0], name), shell=True)
        subprocess.call('rm -r trees/msa_*.fasta trees/*.ckp.gz trees/*.iqtree trees/*.treefile trees/*.log', shell=True)

###ALIGNER

rule align_all:
    input:
        files = expand("aligned/aligned_{sample}.fasta", sample=IDS)
    output:
        "all_aligned.fasta"
    script:
        "scripts/concatenator.py"


rule mapper:
    input:
        "aligned/pre_{sample}.fasta",
    output:
        "aligned/aligned_{sample}.fasta"
    shell:
        "python scripts/mapper.py -i {input} -o {output} -g {GR}"



rule aligner:
    input:
        "split/{sample}.fasta"
    output:
        temp("aligned/pre_{sample}.fasta")
    shell:
        'mafft --quiet  --add {input} --keeplength ./data/HXB2.fasta  >  {output}'



rule split:
    input:
        "input/{}".format(INPUT)
    output:
        expand("split/{sample}.fasta", sample=IDS)
    script:
        "scripts/spliter.py"



rule clean:
    shell:
        "rm -r split; rm -r aligned"


rule delete_interm_files:
    shell:
        "rm -r split aligned subtype trees"

# write save and clean intermidiate files

rule delete_all_outputs:
    shell:
        "rm -r split aligned subtype trees all_aligned.fasta  all_subtyped.txt with_neighbors_all_subtyped.txt"

rule save_compress_interm_files:
    shell:
        "tar -zcvf intermidiate_files.tar.gz split aligned subtype trees ;"
        "rm -r split aligned subtype trees"

rule save_compress_all:
    shell:
        "tar -zcvf all.tar.gz * ; "
        "rm -r split aligned subtype trees all_aligned.fasta  all_subtyped.txt with_neighbors_all_subtyped.txt"