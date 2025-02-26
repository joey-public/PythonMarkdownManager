import json

def __set_default_config(config)->dict:
    pass

def read_config(content_str:str)->dict:
    md_str = ''
    config_str = ''
    reading_config = False
    content = content_str.splitlines()
    for i, line in enumerate(content):
        if 'config_start' in line:
            reading_config = True
        elif 'config_end' in line:
            break
        elif reading_config:
            config_str += line
        else:
            md_str += '\n' + line
    if config_str == '':
        config = {}
    else:
        #TODO: Handle bad json formatting
        config = json.loads(config_str) 
    return config, md_str
