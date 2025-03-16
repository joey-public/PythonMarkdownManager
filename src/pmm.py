import argparse
import glob

from format_md import format_md
from md2html import md2html
from site_gen import site_gen

def pmm():
    pass
################################################################################
def main():
    print('pmm.py called...')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_md_file', 
                        help='The path to the markdown file to be formatted.', 
                        type=str) 
    args = parser.parse_args()
    main(args)
