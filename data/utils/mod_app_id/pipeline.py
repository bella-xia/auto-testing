import os
from tqdm import tqdm
from data.utils.mod_app_id.modify_config_json import modify_config_with_url


def pipeline_per_miniprogram(root_path, miniprogram_name):
    print(f'\nSurveying miniprogram {miniprogram_name}\n')
    miniprogram_path = os.path.join(root_path, miniprogram_name)

    print('\nStep 1: check config existence and modify config so that url can be processed unchecked\n')
    modify_config_with_url(root_path, miniprogram_name)


if __name__ == '__main__':
    ROOT_PATH = "/home/bella-xia/auto-testing/data/groundtruth"
    miniprogram_list = os.listdir(ROOT_PATH)
    for miniprogram_name in tqdm(miniprogram_list):
        pipeline_per_miniprogram(ROOT_PATH, miniprogram_name)
    