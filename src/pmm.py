import argparse
import glob

from fileio import read_txt_file_content, save_str_to_file 
from read_config import read_config

def main(args):
    args = vars(args) 
    input_md_dir = args['md_directory']
    print(f'pmm.py called with dir: {input_md_dir}')
    for md_file_path in glob.glob(input_md_dir+'*.md'):
        print(f'looking at: {md_file_path}')
        config, content_str = read_config(read_txt_file_content(md_file_path))
        if config == {}:
            config = {'format_md':0, 'convert_to_html':0, 'format_html':0}
        print(f'...config: {config}')
        if config['format_md'] == 1:
            print('formatting markdown')
            args = config['format_md_args']
            #TODO: implement format_md
        if config['convert_to_html'] == 1:
            print('converting md to html')
            args = config['md2html_args']
            #TODO: implement md2html 
        if config['format_html'] == 1:
            print('formatting html')
            args = config['format_html_args']
            #TODO: implement format_html 
            
     

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
#    parser.add_argument('input_md_file', 
#                        help='The path to the markdown file to be formatted.', 
#                        type=str) 
    parser.add_argument('md_directory', 
                        help = 'Path to the folder of markdown files to be managed.',
                        type = str)
    args = parser.parse_args()
    main(args)
