import os
from .modify_app_json import read_json_file, write_json_file

def modify_config_with_url(miniprogram_path):
    config_path = os.path.join(miniprogram_path, 'project.private.config.json')
    config_json = read_json_file(config_path)
    if (config_json.get('setting') is None):
        config_json['setting'] = {'urlCheck': False}
    else:
        config_json['setting']['urlCheck'] = False
    write_json_file(config_path, config_json)


if __name__ == '__main__':
    config_json_path = "C:/Users/zhiha/OneDrive/Desktop/miniapp_data/utils"
    modify_config_with_url(config_json_path)