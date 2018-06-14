
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/araujo/anaconda3/envs/test/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05X\x11\x00\x00\x00all_aligned.fastaq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\x06\x00\x00\x00configq\n}q\x0bX\x0e\x00\x00\x00genomic_regionq\x0cX\x05\x00\x00\x00PR-RTq\rsX\x06\x00\x00\x00paramsq\x0ecsnakemake.io\nParams\nq\x0f)\x81q\x10}q\x11h\x08}q\x12sbX\x03\x00\x00\x00logq\x13csnakemake.io\nLog\nq\x14)\x81q\x15}q\x16h\x08}q\x17sbX\t\x00\x00\x00wildcardsq\x18csnakemake.io\nWildcards\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\x04\x00\x00\x00ruleq\x1dX\t\x00\x00\x00align_allq\x1eX\x07\x00\x00\x00threadsq\x1fK\x01X\t\x00\x00\x00resourcesq csnakemake.io\nResources\nq!)\x81q"(K\x01K\x01e}q#(X\x06\x00\x00\x00_coresq$K\x01X\x06\x00\x00\x00_nodesq%K\x01h\x08}q&(h$K\x00N\x86q\'h%K\x01N\x86q(uubX\x05\x00\x00\x00inputq)csnakemake.io\nInputFiles\nq*)\x81q+(X\x1a\x00\x00\x00aligned/aligned_T001.fastaq,X\x1a\x00\x00\x00aligned/aligned_T002.fastaq-X\x1a\x00\x00\x00aligned/aligned_T003.fastaq.e}q/(X\x05\x00\x00\x00filesq0csnakemake.io\nNamedlist\nq1)\x81q2(h,h-h.e}q3h\x08}q4sbh\x08}q5h0K\x00K\x03\x86q6subub.')
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
	with open(snakemake.output[0], 'w') as out_file:
		out_file.write(concatenator(input_list))