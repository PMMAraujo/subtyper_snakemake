
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/araujo/anaconda3/envs/test/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0bX\x11\x00\x00\x00all_aligned.fastaq\x0ca}q\rh\x07}q\x0esbX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11}q\x12h\x07}q\x13sbX\x06\x00\x00\x00configq\x14}q\x15X\x0e\x00\x00\x00genomic_regionq\x16X\x05\x00\x00\x00PR-RTq\x17sX\x04\x00\x00\x00ruleq\x18X\t\x00\x00\x00align_allq\x19X\x05\x00\x00\x00inputq\x1acsnakemake.io\nInputFiles\nq\x1b)\x81q\x1c(X\x1a\x00\x00\x00aligned/aligned_T001.fastaq\x1dX\x1a\x00\x00\x00aligned/aligned_T002.fastaq\x1eX\x1a\x00\x00\x00aligned/aligned_T003.fastaq\x1fe}q (X\x05\x00\x00\x00filesq!csnakemake.io\nNamedlist\nq")\x81q#(h\x1dh\x1eh\x1fe}q$h\x07}q%sbh\x07}q&h!K\x00K\x03\x86q\'subX\t\x00\x00\x00resourcesq(csnakemake.io\nResources\nq))\x81q*(K\x01K\x01e}q+(h\x07}q,(X\x06\x00\x00\x00_nodesq-K\x00N\x86q.X\x06\x00\x00\x00_coresq/K\x01N\x86q0uh-K\x01h/K\x01ubX\x07\x00\x00\x00threadsq1K\x01X\x03\x00\x00\x00logq2csnakemake.io\nLog\nq3)\x81q4}q5h\x07}q6sbub.')
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

	input_list = list(snakemake.input)
#	print(input_list)
#	print(''.join(list(concatenator(input_list))))
	with open(snakemake.output[0], 'w') as out_file:
		out_file.write(concatenator(''.join(list(concatenator(input_list)))))