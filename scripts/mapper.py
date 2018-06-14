from Bio import AlignIO
import argparse


REGIONS = {'PR':[2252, 2550], 'RT':[2549,3870], 
		   'PR-RT':[2252,3869], 'INT':[4229,5096]}


def mapper(msa, out, gr):
	try:
		this_region = REGIONS[gr]
	except KeyError:
   		print("\n\nInvalid Genomic regioin in the config file!!!\n(Valid inputs:"
   			  "'PR', 'RT', 'PR-RT', 'INT')\n\n")

	aligned = AlignIO.read(msa, "fasta")
	to_map = aligned[1]
	sequence = aligned[1].seq[this_region[0]:this_region[1]]
	with open(out, 'w') as mapped:
		mapped.write('>{}\n{}\n'.format(to_map.id, sequence))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input", required = True,
                        help="Name input file.")
	parser.add_argument("-o","--output", required = True,
                        help="Name output file.")
	parser.add_argument("-g","--genomic", required = True,
                        help="Name of the genomic region.")
	args = parser.parse_args()
	mapper(args.input, args.output, args.genomic)