from ete3 import Tree
import pandas as pd


def get_support_parents(tree_file):
    """Tree information summarization

    This function uses ete3 package to open the tree file and the function
    'assemble_df' to extract the node information from the tree. Data is
    colected for the parent node (parent) of the sequence node, the node
    above that(g_parent),and the node above that node (gg_parent).
    Exceptions where built to lead with unexisting nodes. More information
    about the node extraction in the 'assemble_df' function.

    Args:
        tree_file (newick): Tree file.
    Returns:
        list (list): List of 7 items.
    """
    name = tree_file.replace('trees/' ,'').replace('.treefile', '')

    try:
#        t = Tree(tree_file, format=0)
        t = Tree(tree_file, format=1)

        parent =    t.search_nodes(name='target')[0].up
        if parent == None:
                g_parent = None
                gg_parent = None
        else:
                g_parent =  t.search_nodes(name='target')[0].up.up

        if g_parent == None:
                gg_parent = None
        else:
                gg_parent = t.search_nodes(name='target')[0].up.up.up

        return [name] + assemble_df(parent) + assemble_df(g_parent) + assemble_df(gg_parent)

    except:
        return [name,'NGI',['NGI'],'NGI',['NGI'],'NGI',['NGI']]


def assemble_df(which_node):
    """Node info extarctor.

    This function is responsable for extracting the information from a
    given tree node parsed as 'which_node'. It lists the leafs in the
    given node and the barnch suupport values for that node.

    Args:
        which_node (ete3 node): A tree node recognized by ete3.
        name (str): Name of a given sample from which we are extracting data.
    Returns:
        list (list): List of two items, node support (str) and leafs in
        node (str).
    """
    if which_node == None:
        return ['None', ['None']]
    else:

        listing = [x for x in [str(leaf).replace('\n--', '') for leaf in
        which_node] if x != 'target']
        listing_short = set([x.split('-')[0] for x in listing])

        result_short = [','.join(listing_short)]

#        return [which_node.name, result_short]
        return [which_node.support, result_short]

# FUNCTION TO TREAT THE SUBTYPING RESULTS AND GENERALIZE -> need to do

def report_writter(results, subtyping_name, report_name):
    """Write to files.

    This function is uses the package pandas to write csv files with the
    outputs from the fucntion 'get_support_parents'.

    Args:
        results (list): List of n=number of trees.
        subtyping_name (str): Name of the file for the simplified results.
        report_name (str): Name of the file for the more complete results.
    Returns:
        This function doe not return.
    """
    report = pd.DataFrame()

    name = [x[0] for x in results]
    supp_p = [x[1] for x in results]
    in_node = [','.join(x[2]) for x in results]
    supp_pnode = [x[3] for x in results]
    in_pnode = [','.join(x[4]) for x in results]
    supp_gpnode = [x[5] for x in results]
    in_gpnode = [','.join(x[6]) for x in results]

    report['name'] = name
    report['node_supp'] = supp_p
    report['in_node'] = in_node
    report['pnode_supp'] = supp_pnode
    report['in_pnode'] = in_pnode
    report['gpnode_supp'] = supp_gpnode
    report['in_gpnode'] = in_gpnode
    report.to_csv(report_name, sep=';', index=False)

    subtyped = report[['name', 'in_node']]
    subtyped.to_csv(subtyping_name, sep=';', index=False)

if __name__ == '__main__':
    input_list = list(snakemake.input)
    subtyping_name = str(snakemake.output[0])
    report_name = str(snakemake.output[1])

    results = []
    for tree in input_list:
        results.append(get_support_parents(tree))

    report_writter(results, subtyping_name, report_name)
