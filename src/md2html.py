import sys
import os
import json
import argparse
import markdown 
from fileio import read_txt_file_content, save_str_to_file 
from read_config import read_config
from format_md import format_md
from format_html import format_html
import headers as headers

EXTENSIONS=['fenced_code', 'tables', 'md_mermaid']

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

def md2html(md_file_path:str, html_file_path:str=None)->None:
    if html_file_path == None:
        html_file_name = os.path.splitext(os.path.basename(md_file_path))[0]
        html_file_path = output_html_dir + html_file_name + '.html'
    md_content_str = read_txt_file_content(md_file_path)
    config, md_content_str = read_config(md_content_str)
#    format_md(md_content_str, config. 
    html_header = _generate_html_header(config)
    html_body = markdown.markdown(md_content_str, extensions=EXTENSIONS)
    html_footer = _generate_html_footer(config)
    html_content_str = html_header + html_body + html_footer
#    html_file_name = os.path.splitext(os.path.basename(md_file_path))[0]
#    html_file_path = html_dir + html_file_name + '.html'
    save_str_to_file(html_file_path, html_content_str)
    
def main(args)->None:
    args = vars(args)
    md_file_path = args.pop('input_md_file', None)
    html_file_path = args.pop('output_html_file', None)
    #TODO: make sure md_file_path is valid
    #TODO: set default html_file based on md_file name and path
    #TODO: make sure html_file_path is valid
    md2html(md_file_path, html_file_path)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_md_file', 
                        help = 'The path to the input markdown file.', 
                        type = str) 
    parser.add_argument('output_html_file', 
                        help = 'The path to the output html file.', 
                        type = str)
    args = parser.parse_args()
    main(args)
