import os
from data.utils.mod_app_id.utils import read_json_file, write_json_file

DEFAULT_APP_ID = "wxc26bf025c84ef3b7"

def modify_config_with_url(root_path, miniprogram_name):
    miniprogram_path = os.path.join(root_path, miniprogram_name)

    config_path = os.path.join(miniprogram_path, 'project.config.json')
    if (os.path.exists(config_path) is False):
         config_json = {
             "appid": DEFAULT_APP_ID,
             "compileType": "miniprogram",
             "libVersion": "3.4.3",
             "packOptions": {
                 "ignore": [],
                 "include": []
                 },
            "setting": {
                "babelSetting": {
                     "ignore": [],
                     "disablePlugins": [],
                     "outputPath": ""
                     }
                },
            "condition": {},
            "editorSetting": {
                "tabIndent": "insertSpaces",
                "tabSize": 2
            }
        }
    else:
        try:
            config_json = read_json_file(config_path)
            config_json['appid'] = DEFAULT_APP_ID
        except Exception as e:
            print(f'encountering exception when parsing config json file: {str(e)}')
            config_json = {
             "appid":  DEFAULT_APP_ID,
             "compileType": "miniprogram",
             "libVersion": "3.4.3",
             "packOptions": {
                 "ignore": [],
                 "include": []
                 },
            "setting": {
                "babelSetting": {
                     "ignore": [],
                     "disablePlugins": [],
                     "outputPath": ""
                     }
                },
            "condition": {},
            "editorSetting": {
                "tabIndent": "insertSpaces",
                "tabSize": 2
            }
            }
    write_json_file(config_path, config_json)


    private_config_path = os.path.join(miniprogram_path, 'project.private.config.json')
    if (os.path.exists(private_config_path) is False):
         private_config_json = {
            "projectname": miniprogram_name,
            "setting": {
                "compileHotReLoad": True,
                'urlCheck': False
                }
        }
    else:
        try:
            private_config_json = read_json_file(private_config_path)
            if (private_config_json.get('setting') is None):
                private_config_json['setting'] = {'urlCheck': False}
            else:
                private_config_json['setting']['urlCheck'] = False
        except Exception as e:
            print(f'encountering exception when parsing private config json file: {str(e)}')
            private_config_json = {
            "projectname": miniprogram_name,
            "setting": {
                "compileHotReLoad": True,
                'urlCheck': False
                }
        }

    write_json_file(private_config_path, private_config_json)