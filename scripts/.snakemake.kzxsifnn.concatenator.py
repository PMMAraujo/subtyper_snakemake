
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/araujo/anaconda3/envs/test/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1a\x00\x00\x00aligned/aligned_T001.fastaq\x06X\x1a\x00\x00\x00aligned/aligned_T002.fastaq\x07X\x1a\x00\x00\x00aligned/aligned_T003.fastaq\x08e}q\t(X\x06\x00\x00\x00_namesq\n}q\x0bX\x05\x00\x00\x00filesq\x0cK\x00K\x03\x86q\rsh\x0ccsnakemake.io\nNamedlist\nq\x0e)\x81q\x0f(h\x06h\x07h\x08e}q\x10h\n}q\x11sbubX\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14X\x11\x00\x00\x00all_aligned.fastaq\x15a}q\x16h\n}q\x17sbX\x06\x00\x00\x00paramsq\x18csnakemake.io\nParams\nq\x19)\x81q\x1a}q\x1bh\n}q\x1csbX\x03\x00\x00\x00logq\x1dcsnakemake.io\nLog\nq\x1e)\x81q\x1f}q h\n}q!sbX\x07\x00\x00\x00threadsq"K\x01X\t\x00\x00\x00wildcardsq#csnakemake.io\nWildcards\nq$)\x81q%}q&h\n}q\'sbX\x04\x00\x00\x00ruleq(X\t\x00\x00\x00align_allq)X\x06\x00\x00\x00configq*}q+X\x0e\x00\x00\x00genomic_regionq,X\x05\x00\x00\x00PR-RTq-sX\t\x00\x00\x00resourcesq.csnakemake.io\nResources\nq/)\x81q0(K\x01K\x01e}q1(h\n}q2(X\x06\x00\x00\x00_coresq3K\x00N\x86q4X\x06\x00\x00\x00_nodesq5K\x01N\x86q6uh3K\x01h5K\x01ubub.')
######## Original script #########
#import argparse


def concatenator(input_list):
	for file in input_list:
		with open(file, 'r') as read_in:
			yield read_in.read()





if __name__ == '__main__':
#	parser = argparse.ArgumentParser()
#	parser.add_argument("-i","--input", required = True,
#                        help="Name input file.")
#	parser.add_argument("-o","--output", required = True,
#                        help="Name output file.")
#	args = parser.parse_args()
	input_list = list(snakemake.input[0])
	print(list(concatenator(input_list)))
#	with open(snakemake.output[0], 'w') as out_file:
#		out_file.write(concatenator(input_list))