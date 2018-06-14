def spliter(msa):
	list_seqs = []
	with open(msa, 'r') as input_msa:
		msa = input_msa.read()

	seqs = msa.split('>')[1:]

	for seq in seqs:
		this_seq = seq.split('\n')
		this_seq = [x for x in this_seq if x != '']
		name = this_seq[0]
		list_seqs.append(name)

		with open('./split/{}.fasta'.format(name), 'w') as fasta:
			fasta.write('>{}\n{}\n'.format(name, ''.join(this_seq[1::])))	


if __name__ == '__main__':
	spliter(snakemake.input[0])
