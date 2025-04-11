import re
import fileio as fileio

#figure_regex = r'\*\*Figure \d+:\*\*'
#TODO: this can be done using one line and groups in the re.sub call. 
#      see _replace_md_links for an example
def _renumber(md_file_content:str, args:dict)->str:
    renumber_all = False
    renumber_figures = False
    renumber_tables = False
    renumber_equations = False
    if 'renumber_all' in args.keys():
        renumber_all = args['renumber_all']
    if 'renumber_figures' in args.keys():
        renumber_figures = args['renumber_figures']
    if 'renumber_tables' in args.keys():
        renumber_tables = args['renumber_tables']
    if 'renumber_equations' in args.keys():
        renumber_equations = args['renumber_equations']
    return md_file_content

def _replace_md_links(md_file_content:str, args)->str:
    if not('replace_md_links' in args.keys()):
        return md_file_content
    if args['replace_md_links']==False:
        return md_file_content
    pattern = r'(\[.*?\])(\(.*?)\.md\)'
    repl_with = r'\1\2.html)'
    return re.sub(pattern, repl_with, md_file_content)

def format_md(md_file_content, **kwargs)->str:
    md_file_content = _replace_md_links(md_file_content, kwargs) 
    md_file_content = _renumber(md_file_content, kwargs)
    return md_file_content
