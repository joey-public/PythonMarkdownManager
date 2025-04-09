import json
import re


def _get_default_config()->dict:
    return {}

def _has_config(content_str:str)->bool:
    return '---config_start---' in content_str

def read_config(content_str:str)->tuple:
    if not _has_config(content_str):
        return _get_default_config(), content_str
    md_str = ''
    config_str = ''
    reading_config = False
    content = content_str.splitlines()
    for i, line in enumerate(content):
        if 'config_start' in line:
            reading_config = True
        elif 'config_end' in line:
            pass 
        elif reading_config:
#            print(f'{i}: {line}')
            config_str += line
        else:
            md_str += '\n' + line
    if config_str == '':
        config = {}
    else:
        #TODO: Handle bad json formatting
        config = json.loads(config_str) 
    return config, md_str
