
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/araujo/anaconda3/envs/test/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x0e\x00\x00\x00genomic_regionq\x05X\x05\x00\x00\x00PR-RTq\x06sX\t\x00\x00\x00resourcesq\x07csnakemake.io\nResources\nq\x08)\x81q\t(K\x01K\x01e}q\n(X\x06\x00\x00\x00_namesq\x0b}q\x0c(X\x06\x00\x00\x00_nodesq\rK\x01N\x86q\x0eX\x06\x00\x00\x00_coresq\x0fK\x00N\x86q\x10uh\x0fK\x01h\rK\x01ubX\t\x00\x00\x00wildcardsq\x11csnakemake.io\nWildcards\nq\x12)\x81q\x13}q\x14h\x0b}q\x15sbX\x03\x00\x00\x00logq\x16csnakemake.io\nLog\nq\x17)\x81q\x18}q\x19h\x0b}q\x1asbX\x06\x00\x00\x00outputq\x1bcsnakemake.io\nOutputFiles\nq\x1c)\x81q\x1dX\x11\x00\x00\x00all_aligned.fastaq\x1ea}q\x1fh\x0b}q sbX\x06\x00\x00\x00paramsq!csnakemake.io\nParams\nq")\x81q#}q$h\x0b}q%sbX\x07\x00\x00\x00threadsq&K\x01X\x04\x00\x00\x00ruleq\'X\t\x00\x00\x00align_allq(X\x05\x00\x00\x00inputq)csnakemake.io\nInputFiles\nq*)\x81q+(X\x1a\x00\x00\x00aligned/aligned_T001.fastaq,X\x1a\x00\x00\x00aligned/aligned_T002.fastaq-X\x1a\x00\x00\x00aligned/aligned_T003.fastaq.e}q/(X\x05\x00\x00\x00filesq0csnakemake.io\nNamedlist\nq1)\x81q2(h,h-h.e}q3h\x0b}q4sbh\x0b}q5h0K\x00K\x03\x86q6subub.')
######## Original script #########
def concatenator(input_list):
	for file in input_list:
		with open(file, 'r') as read_in:
			yield read_in.read()





if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input", required = True,
                        help="Name input file.")
	parser.add_argument("-o","--output", required = True,
                        help="Name output file.")
	args = parser.parse_args()
	input_list = list(args.input)
	with open(args.output[0], 'w') as out_file:
		out_file.write(concatenator(input_list))