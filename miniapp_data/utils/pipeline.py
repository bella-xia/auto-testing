import os
from tqdm import tqdm
from pipeline_utils.modify_wxml import format_wxml_style_attribute, find_wxml_files
from pipeline_utils.modify_babel import modify_babel_path
from pipeline_utils.modify_app_json import check_all_paths
from pipeline_utils.modify_config_json import modify_config_with_url


if __name__ == '__main__':
    ROOT_PATH = "C:/Users/zhiha/OneDrive/Desktop/miniapp_data/unpacked_data_unveilr"
    MINIRPOGRAM_NAME = "miniprogram1"
    MINIRPOGRAM_PATH = os.path.join(ROOT_PATH, MINIRPOGRAM_NAME)

    print('Step 1: Eliminate all missing pages\n')
    check_all_paths(ROOT_PATH, MINIRPOGRAM_NAME)

    print('\nStep 2: Check all invalid style format in wxml files and modify them\n')
    all_wxml_files = find_wxml_files(MINIRPOGRAM_PATH, [])
    print(f'In total, there are {len(all_wxml_files)} wxml files for modification')
    for wxml_dir in tqdm(all_wxml_files):
        format_wxml_style_attribute(os.path.join(MINIRPOGRAM_PATH, wxml_dir))

    print('\nStep 3: Modify @babel typeof definition\n')
    modify_babel_path(MINIRPOGRAM_PATH)

    print('\nStep 4: modify config so that url can be processed unchecked\n')
    modify_config_with_url(MINIRPOGRAM_PATH)