import os, subprocess, json
from tqdm import tqdm


if __name__ == "__main__":
    ROOT_DIR = "C:/Users/zhiha/OneDrive/Documents/WeChat Files/Applet"
    JSON_DIR = "C:/Users/zhiha/OneDrive/Desktop/auto-testing/miniapp_data/auxiliary_data/miniapp_correspondence.json"
    STORE_DIR = "C:/Users/zhiha/OneDrive/Desktop/auto-testing/miniapp_data/top50_data"
    # all_miniapps = os.listdir(ROOT_DIR)
    # print(f"there are a total of {len(all_miniapps)} mini-programs")
    # print(all_miniapps)

    with open(JSON_DIR, "r", encoding="utf-8") as f:
        miniapp_data = json.load(f)

    for miniapp, name in miniapp_data.items():

        try:
            miniprogram_dir = os.path.join(ROOT_DIR, miniapp)
            folder_name = os.listdir(miniprogram_dir)[0]
            miniapp_dir = os.path.join(miniprogram_dir, folder_name, "__APP__")

            subprocess.run(
                ["./unveilr.exe", os.path.join(miniprogram_dir, folder_name)]
            )

            subprocess.run(
                [
                    "mv",
                    miniapp_dir,
                    os.path.join(STORE_DIR, f"{miniapp}_{name}"),
                ]
            )

            # subprocess.run(["rm", "-rf", os.path.join(ROOT_DIR, miniapp, folders[0])])

            # subprocess.run(
            #     [
            #         "mkdir",
            #         os.path.join(
            #             STORE_DIR,
            #             miniapp,
            #         ),
            #     ]
            # )

            # subprocess.run(
            #     [
            #         "mv",
            #         os.path.join(ROOT_DIR, miniapp, "__APP__") + "/*",
            #         os.path.join(STORE_DIR, miniapp),
            #     ]
            # )
            # subprocess.run(["rm", "-rf", os.path.join(ROOT_DIR, miniapp, folders[0])])
        except Exception as e:
            print(f"exception at miniapp {miniapp} : {str(e)}")
