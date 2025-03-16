import glob
import argparse
from md2html import md2html

def multi_md2html(input_md_dir:str, output_html_dir:str)->None:
    for md_file_path in glob.glob(input_md_dir+'*.md'):
        md2html(md_file_path, output_html_dir)

def main(args)->None:
    args = vars(args) #convert Namespace to dict
    multi_md2html(**args)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_md_dir', 
                        help='The path to the directory of markdown files to be converted.', 
                        type=str)
    parser.add_argument('output_html_dir', 
                        help='The path to the directory to save the html files.', 
                        type=str)
    args = parser.parse_args()
    main(args)
