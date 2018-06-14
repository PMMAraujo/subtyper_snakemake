
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/araujo/anaconda3/envs/test/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00resourcesq\tcsnakemake.io\nResources\nq\n)\x81q\x0b(K\x01K\x01e}q\x0c(X\x06\x00\x00\x00_coresq\rK\x01X\x06\x00\x00\x00_nodesq\x0eK\x01h\x07}q\x0f(h\rK\x00N\x86q\x10h\x0eK\x01N\x86q\x11uubX\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14}q\x15h\x07}q\x16sbX\x06\x00\x00\x00configq\x17}q\x18X\x0e\x00\x00\x00genomic_regionq\x19X\x05\x00\x00\x00PR-RTq\x1asX\x07\x00\x00\x00threadsq\x1bK\x01X\x04\x00\x00\x00ruleq\x1cX\t\x00\x00\x00align_allq\x1dX\x03\x00\x00\x00logq\x1ecsnakemake.io\nLog\nq\x1f)\x81q }q!h\x07}q"sbX\x06\x00\x00\x00outputq#csnakemake.io\nOutputFiles\nq$)\x81q%X\x11\x00\x00\x00all_aligned.fastaq&a}q\'h\x07}q(sbX\x05\x00\x00\x00inputq)csnakemake.io\nInputFiles\nq*)\x81q+(X\x1a\x00\x00\x00aligned/aligned_T001.fastaq,X\x1a\x00\x00\x00aligned/aligned_T002.fastaq-X\x1a\x00\x00\x00aligned/aligned_T003.fastaq.e}q/(h\x07}q0X\x05\x00\x00\x00filesq1K\x00K\x03\x86q2sh1csnakemake.io\nNamedlist\nq3)\x81q4(h,h-h.e}q5h\x07}q6sbubub.')
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
	print(concatenator(input_list))
	with open(snakemake.output[0], 'w') as out_file:
		out_file.write(concatenator(input_list))