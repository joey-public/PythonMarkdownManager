import argparse
import re
import fileio as fileio

def _renumber(md_file_content:str, renumber_all=False,renumber_figures=False, 
                renumber_tables=False, renumber_equations=False)->str:
    if not(renumber_all or renumber_figures or renumber_tables or renumber_equations):
        return md_file_content 
    figure_regex = r'\*\*Figure \d+:\*\*'
    table_regex = r'\*\*Table \d+:\*\*'
    equation_regex = r'\*\*Equation \d+:\*\*'
    if renumber_all:
        renumber_figures = True
        renumber_tables = True
        renumber_equations = True
    if renumber_figures:
        pass
    if renumber_tables:
        pass
    if renumber_equations: #TODO fix this
        strings = re.split(equation_regex, md_file_content)
        for i, str_ in enumerate(strings):
            print(str_)
    return md_file_content 

def format_md(md_file_content:str, output_md_file:str='./out.md', renumber_all=False, 
              renumber_figures = False, renumber_tables=False, renumber_equations=False):
    print(f'formatting mardown file:')
    md_file_content = _renumber(md_file_content, renumber_all, renumber_figures, renumber_tables, renumber_equations)
    fileio.save_str_to_file(output_md_file, md_file_content)

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
    parser.add_argument('-o', '--output_md_file', 
                        help='The path to output file to write the formatted results. Uses out.md as the default. You can enter the name of the input file here and it will be overwritten.', 
                        type=str,
                        default = './out.md')
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
    args = parser.parse_args()
    main(args)
