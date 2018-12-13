
def concatenator(input_list):
	"""Concatenator of fasta files.

    This function concatenates all the aligned fasta files in the 'aligned'
	folder in one single multiple sequence alignment file.

	Args:
        input_list (list): List of fasta files in the 'aligned' folder.

	Returns:
        This function doe not return.
	"""

	for file in input_list:
		with open(file, 'r') as read_in:
			yield read_in.read()

if __name__ == '__main__':
	input_list = list(snakemake.input)
	with open(snakemake.output[0], 'w') as out_file:
		out_file.write(''.join(list(concatenator(input_list))))