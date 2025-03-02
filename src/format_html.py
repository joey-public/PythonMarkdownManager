import argparse
import re
import fileio as fileio


def format_html(html_file_content:str, output_html_files:str=['./out.md'], replace_md_links=False):
    print(f'formatting html file:')
    for path in output_html_files:
        print(path)
        fileio.save_str_to_file(path, html_file_content) 

def main(args)->None:
    args = vars(args) #convert Namespace to dict
    input_path = args.pop('input_html_file', None)
    if input_path == None:
        return 
    #TODO: make sure input path is ok...
    html_content_str = fileio.read_txt_file_content(input_path)
    format_html(html_content_str, **args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_html_file', 
                        help='The path to the markdown file to be formatted.', 
                        type=str)
    parser.add_argument('-o', '--output_html_files', 
                        help='The path to output files to write the formatted results. Uses out.html as the default. You can enter the name of the input file here and it will be overwritten.', 
                        type=str,
                        nargs='+', 
                        default = ['./out.html'])
    parser.add_argument('-rp', '--replace_md_links', 
                        help='Replace the markdown file links with links to the proper html file.',
                        action='store_true')
    args = parser.parse_args()
    main(args)
