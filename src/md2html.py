import sys
import os
import json
import argparse
import markdown 
from fileio import read_txt_file_content, save_str_to_file 
from read_config import read_config
import headers as headers

EXTENSIONS=['fenced_code', 'tables', 'md_mermaid']

#def _parse_args(argv:list)->list:
#    usage_str = 'usage: python md2html.py <input.md> <output_dir>'
#    n_args=len(argv)
#    expected_n_args = 3
#    if not(n_args==expected_n_args):
#        print(f'Error: Arguments Incorrect:\n    {usage_str}')
#        return []
#    md_file_exisits = os.path.isfile(argv[1])
#    md_file_valid = os.path.splitext(argv[1])[1]=='.md'
#    if not(md_file_exisits): 
#        print(f'Error: {argv[1]} md file does not exist:\n    {usage_str}')
#        return []
#    if not(md_file_valid):
#        print(f'Error: {argv[1]} is not a md file:\n    {usage_str}')
#        return []
#    # make sure the html dir is valid and exists already
#    html_dir_exists = os.path.isdir(argv[2])
#    if not(html_dir_exists):
#        print(f'Error: {argv[2]} is not an existing directory :\n    {usage_str}')
#        return []
#    #If we make it here we know both arguments are good
#    md_file_str = argv[1]
#    html_dir_str = argv[2]
#    return [md_file_str, html_dir_str]

def _generate_html_header(config:dict)->str:
    header = '<header>\n'
    if config == {}:
        header += '</header>\n<body>' 
        return header
    if config['css_style_path'] != '':
        css_style_path = config['css_style_path']
        header += f'<link rel="stylesheet" href="{css_style_path}">'
    if config['enable_latex_math'] == 1:
        header += headers.MDX_HTML_HEADER
    if config['enable_mermaid_graphs'] == 1:
        header += headers.MERMAID_HTML_HEADER
    header += '</header>\n<body>' 
    return header

def _generate_html_footer(config)->str:
    footer = '\n</body>'
    return footer

def md2html(md_file_path:str, html_dir:str)->None:
    md_content_str = read_txt_file_content(md_file_path)
    config, md_content_str = read_config(md_content_str)
    html_header = _generate_html_header(config)
    html_body = markdown.markdown(md_content_str, extensions=EXTENSIONS)
    html_footer = _generate_html_footer(config)
    html_content_str = html_header + html_body + html_footer
    html_file_name = os.path.splitext(os.path.basename(md_file_path))[0]
    html_file_path = html_dir + html_file_name + '.html'
    save_str_to_file(html_file_path, html_content_str)
    
def main(args)->None:
    args = vars(args)
    if arg_list == []: 
        print('Error while parsing input arguments')
        return 
    md_file_path = arg_list[0]
    html_dir = arg_list[1]
    md2html(md_file_path, html_dir)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_md_file', 
                        help = 'The path to the input markdown file.', 
                        type = str) 
    parser.add_argument('-o', '--output_html_file', 
                        help = 'The path to the output html file.'
                        type = str)
    args = parser.parse_args()
    main(args)
