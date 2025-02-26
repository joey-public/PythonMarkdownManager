# Python Markdown Manager

This project aims to create a python tool to organize a single folder full markdown files. This should allow the user to create all their markdown notes, blog posts, readmes, ect inside of a single directory on their computer.

Each note contains a simple, optional config text at the bottom of the file. This config text, along with the passed cli options, informs the python markdown manager on how to handle that specific markdown file.


## Architecture

I see this the python markdown manager tool as a combination of several smaller tools. My goal is to make smallish self contained python scripts for each distinct function, as well as a few extra scripts for functions that may be useful to more then one of the tools.

The top level `pmm.py` tool contains functionality supported by the following sub-tools:

1. md2html.py 
1. multi_md2html.py
1. site_gen.py 

Each of these sub-tools can also be run independently from the command line.

## md2html.py

This is the heavy lifter of the whole project. This script takes in the following as cli inputs:

    1. A file path to a single existing markdown file. 
    2. An existing directory to save the output html file.

The script outputs an html file that is saved to the passed directory with the same base-name as the input markdown file.

The markdown file can have an optional config string placed at the bottom of the file. For now I am still ironing out the details of all the config options, but I should write up a section explaining what is available once I settle on a working solution.

### md2html.py features

The markdown to html conversion should support the following features for all conversions

    1. Basic Markdown syntax for Heading, bold text, italic, links, ect. All the stuff supported by default in the python markdown package with no plugins
    1. Code Blocks
    1. Tables
    1. Auto-numbering of figures, tables, and equations
    1. auto-update absolute path links into relative links for `.html` files in the passed `html_dir`
    1. auto-update absolute path links to markdown files into links for their `.html` equivalent files

It should also optionally support these features. The features on this list should be optional on a per-markdown file basis. They can be enabled or disabled in the previously mentioned config string at the bottom of each markdown file.

    1. Latex Math inline and block support 
    1. Mermaid Diagram support 
    

## multi_md2html.py

This script takes the following inputs:

    1. An existing directory with a collection of markdown files. 
    2. An existing directory to save the output html files.

It converts all the markdown files in the passed directory into html files saved int eh passed html directory. The conversions will all be done with the `md2html.py` script.

## site_gen.py

This script takes the following inputs:
    
    1. An existing directory with a collection of markdown files. 

It should search though the markdown files in the passed directory looking for files whose config strings have the following:

    - `website_directory`: `/path/to/the/sites/html/folder`
    - `website_publish`: (0 or 1)

If a valid `website_directory` is provided and the `website_publish` options is set to 1, then this script will use the `md2html.py` script to create an html file in the passed `website_directory`.


## misc ideas

- `project_readme_path`: copy this markdown file into a specific directory as a README.md file. I suggest you name the markdown file as `project_name_README.md` in the monolithic markdown folder.
