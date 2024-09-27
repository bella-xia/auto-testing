import os
from .modify_app_json import read_json_file, write_json_file


def modify_config_with_url(root_path, miniprogram_name, logger=None):
    miniprogram_path = os.path.join(root_path, miniprogram_name)

    config_path = os.path.join(miniprogram_path, "project.config.json")
    if os.path.exists(config_path) is False:
        config_json = {
            "appid": "wxc26bf025c84ef3b7",
            "compileType": "miniprogram",
            "libVersion": "3.4.3",
            "packOptions": {"ignore": [], "include": []},
            "setting": {
                "babelSetting": {"ignore": [], "disablePlugins": [], "outputPath": ""},
                "urlCheck": False,
                "es6": False,
                "enhance": False,
            },
            "condition": {},
            "editorSetting": {"tabIndent": "insertSpaces", "tabSize": 2},
        }
    else:
        try:
            config_json = read_json_file(config_path)
            if config_json.get("appid") is None:
                config_json["appid"] = "wxc26bf025c84ef3b7"
            else:
                config_json["appid"] = "wxc26bf025c84ef3b7"

            if config_json.get("setting") is None:
                config_json["setting"] = {
                    "babelSetting": {
                        "ignore": [],
                        "disablePlugins": [],
                        "outputPath": "",
                    },
                    "urlCheck": False,
                    "es6": False,
                    "enhance": False,
                }
            else:
                config_json["setting"]["urlCheck"] = False
                config_json["setting"]["es6"] = False
                config_json["setting"]["enhance"] = False

        except Exception as e:
            f_data = f"encountering exception when parsing config json file: {str(e)}"
            print(f_data)
            if logger is not None:
                logger.info(f_data)

            config_json = {
                "appid": "wxc26bf025c84ef3b7",
                "compileType": "miniprogram",
                "libVersion": "3.4.3",
                "packOptions": {"ignore": [], "include": []},
                "setting": {
                    "babelSetting": {
                        "ignore": [],
                        "disablePlugins": [],
                        "outputPath": "",
                    },
                    "urlCheck": False,
                    "es6": False,
                    "enhance": False,
                },
                "condition": {},
                "editorSetting": {"tabIndent": "insertSpaces", "tabSize": 2},
            }
    write_json_file(config_path, config_json)

    private_config_path = os.path.join(miniprogram_path, "project.private.config.json")
    if os.path.exists(private_config_path) is False:
        private_config_json = {
            "projectname": miniprogram_name,
            "setting": {
                "compileHotReLoad": True,
                "urlCheck": False,
                "es6": False,
                "enhance": False,
            },
        }
    else:
        try:
            private_config_json = read_json_file(private_config_path)
            if private_config_json.get("setting") is None:
                private_config_json["setting"] = {
                    "urlCheck": False,
                    "es6": False,
                    "enhance": False,
                }
            else:
                private_config_json["setting"]["urlCheck"] = False
                private_config_json["setting"]["es6"] = False
                private_config_json["setting"]["enhance"] = False
        except Exception as e:
            f_data = f"encountering exception when parsing private config json file: {str(e)}"
            print(f_data)
            if logger is not None:
                logger.info(f_data)
            private_config_json = {
                "projectname": miniprogram_name,
                "setting": {
                    "compileHotReLoad": True,
                    "urlCheck": False,
                    "es6": False,
                    "enhance": False,
                },
            }

    write_json_file(private_config_path, private_config_json)


if __name__ == "__main__":
    config_json_path = "C:/Users/zhiha/OneDrive/Desktop/miniapp_data/utils"
    modify_config_with_url(config_json_path)
