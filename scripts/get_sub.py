#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:26:32 2017

@author: araujo
"""

from ete3 import Tree
import argparse


def get_crs(treefile):
    t = Tree(treefile)
    identifier = treefile.replace('trees/', '').replace('.parstree', '')
    node = t.search_nodes(name=identifier)[0]
    parents = node.up
    result =[]
    
    for leaf in parents:
        result.append(str(leaf))
    
    result = [s.strip('\n--') for s in result]
    result = [x for x in result if x != identifier]
    txt_result = ','.join(result)
    out_long = "{0}\t{1}\n".format(identifier, txt_result)
    only_subtype = ','.join(set([x.split('_')[0] for x in result]))
    out_short = "{0}\t{1}\n".format(identifier, only_subtype)
    return out_short, out_long


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input", required = True,
                        help="Name of the tree file, in parstree format.")
    parser.add_argument("-s","--short", required = True,
                        help="Name output file with only subtype.")
    parser.add_argument("-l","--long", required = True,
                        help="Name output file with subtype and closses phylogenetic pair.")
    args = parser.parse_args()

    out_short, out_long = get_crs(args.input)

    with open(args.short, 'w') as short_write:
        short_write.write(out_short)

    with open(args.long, 'w') as long_write:
        long_write.write(out_long)


