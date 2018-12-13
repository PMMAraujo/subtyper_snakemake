import argparse
import subprocess
from Bio import AlignIO

def tree_maker(file_name, gr):
    """Tree creator.

    This function evaluates if the previously aligned sequence is empty (only
    gaps or not). If it is no tree is built, only a warning regarding no
    genetic information is outputed. If the aligned sequence is valid (not
    empty) THe software IQtree is used to buid a phylogenetic tree. The tree
    building is constrained to a backbone provided. The support values for
    bipartitions are calculated using ultrafastbootstraping as SH-like
    likehood. All the normal IQtree outputs are built but only the file
    '.treefile' is mainted (the other IQTree outputs arew deleted).

	Args:
        file_name (fasta): Fasta file containing 1 fasta sequence aligned.
        gr (str): String of the genomic region of interest. Specified in the
        'config.yaml' file.

	Returns:
        This function doe not return.
	"""
    name = file_name.replace('aligned/aligned_' ,'').replace('.fasta', '')

    if ''.join(set(str(AlignIO.read(file_name, 'fasta')[0].seq))) == '-':
        with open(f'trees/{name}.treefile', 'w') as out_empty:
            out_empty.write(f'No genetic imformation in the file \
            {name}.fasta for the region {gr}.')

    else:
        subprocess.call("fasta=$(tail -n 1 '{0}'); echo '>target' > trees/tmp ; \
        echo $fasta >> trees/tmp".format(file_name), shell=True)
        subprocess.call('cat data/test_{0}_subtype_refs.fasta trees/tmp > \
        "trees/msa_{1}.fasta"'.format(gr, name), shell=True)
#        subprocess.call('iqtree -nt 2 -s "trees/msa_{0}.fasta" -m GTR -alrt \
#        1000 -bb 1000 -g data/base_tree001.treefile -redo -pre "trees/{0}" \
#        -quiet'.format(name), shell=True)
        subprocess.call('iqtree -nt 2 -s "trees/msa_{0}.fasta" -m GTR -alrt \
        1000 -g data/base_tree001.treefile -redo -pre "trees/{0}" -quiet \
        -fast'.format(name),shell=True)
        subprocess.call('rm -r "trees/msa_{0}.fasta" "trees/{0}.ckp.gz" \
        "trees/{0}.iqtree" "trees/{0}.log" "trees/{0}.parstree" trees/tmp'.format(name),
        shell=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input", required = True,
                            help="Name input file.")
    parser.add_argument("-g","--genomic", required = True,
                            help="Name of the genomic region.")
    args = parser.parse_args()
    tree_maker(args.input, args.genomic)
