
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/araujo/anaconda3/envs/test/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1a\x00\x00\x00aligned/aligned_T001.fastaq\x06X\x1a\x00\x00\x00aligned/aligned_T002.fastaq\x07X\x1a\x00\x00\x00aligned/aligned_T003.fastaq\x08e}q\t(X\x05\x00\x00\x00filesq\ncsnakemake.io\nNamedlist\nq\x0b)\x81q\x0c(h\x06h\x07h\x08e}q\rX\x06\x00\x00\x00_namesq\x0e}q\x0fsbh\x0e}q\x10h\nK\x00K\x03\x86q\x11subX\x06\x00\x00\x00configq\x12}q\x13X\x0e\x00\x00\x00genomic_regionq\x14X\x05\x00\x00\x00PR-RTq\x15sX\t\x00\x00\x00wildcardsq\x16csnakemake.io\nWildcards\nq\x17)\x81q\x18}q\x19h\x0e}q\x1asbX\x04\x00\x00\x00ruleq\x1bX\t\x00\x00\x00align_allq\x1cX\x07\x00\x00\x00threadsq\x1dK\x01X\x06\x00\x00\x00paramsq\x1ecsnakemake.io\nParams\nq\x1f)\x81q }q!h\x0e}q"sbX\x03\x00\x00\x00logq#csnakemake.io\nLog\nq$)\x81q%}q&h\x0e}q\'sbX\t\x00\x00\x00resourcesq(csnakemake.io\nResources\nq))\x81q*(K\x01K\x01e}q+(X\x06\x00\x00\x00_nodesq,K\x01h\x0e}q-(h,K\x00N\x86q.X\x06\x00\x00\x00_coresq/K\x01N\x86q0uh/K\x01ubX\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3X\x11\x00\x00\x00all_aligned.fastaq4a}q5h\x0e}q6sbub.')
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
	print(lis(concatenator(input_list)))
	with open(snakemake.output[0], 'w') as out_file:
		out_file.write(concatenator(input_list))