import argparse
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
        print('replace_md_links NOT FOUND')
        return md_file_content
    if args['replace_md_links']==False:
        print('replace_md_links IS FALSE')
        return md_file_content
    print('replace_md_links IS TRUE')
    pattern = r'(\[.*?\])(\(.*?)\.md\)'
    repl_with = r'\1\2.html)'
    return re.sub(pattern, repl_with, md_file_content)

def format_md(md_file_content, **kwargs)->str:
    print(f'formatting mardown file:')
    md_file_content = _replace_md_links(md_file_content, kwargs) 
    md_file_content = _renumber(md_file_content, kwargs)
#    print(md_file_content)
    return md_file_content

def main(args)->None:
    args = vars(args) #convert Namespace to dict
    input_path = args.pop('input_md_file', None)
    if input_path == None:
        return 
    #TODO: make sure input path is ok...
    md_content_str = fileio.read_txt_file_content(input_path)
    format_md(md_content_str, **args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_md_file', 
                        help='The path to the markdown file to be formatted.', 
                        type=str) 
    parser.add_argument('-o', '--output_md_files', 
                        help='The path to output file to write the formatted results. Uses out.md as the default. You can enter the name of the input file here and it will be overwritten.', 
                        nargs='+', 
                        default = ['./out.md'])
    parser.add_argument('-rn', '--renumber_all', 
                        help='Renumbers all figures, tables, and equations in file from 1 to N.',
                        action='store_true')
    parser.add_argument('-rn_f', '--renumber_figures', 
                        help='Renumbers all figures in file from 1 to N.',
                        action='store_true')
    parser.add_argument('-rn_t', '--renumber_tables', 
                        help='Renumbers all tables in file from 1 to N.',
                        action='store_true')
    parser.add_argument('-rn_e', '--renumber_equations', 
                        help='Renumbers all equations in file from 1 to N.',
                        action='store_true')
    parser.add_argument('')
    args = parser.parse_args()
    main(args)
