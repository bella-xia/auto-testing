import os, subprocess, argparse
from tqdm import tqdm


def run_unpack_script(script_path, method="python"):
    if method == "python":
        subprocess.run(["./unveilr.exe", script_path])
    elif method == "javascript":
        subprocess.run(["node", "./wxappUnpacker/wuWxapkg.js", script_path])


if __name__ == "__main__":

    ROOT = "C:/Users/zhiha/OneDrive/Documents/WeChat Files/Applet"
    parser = argparse.ArgumentParser()
    parser.add_argument("--miniapp", type=str)
    parser.add_argument("--folder", type=str, default=None)

    args = parser.parse_args()
    miniapp_dir = os.path.join(ROOT, args.miniapp)

    if args.folder is None:
        args.folder = os.listdir(miniapp_dir)[0]
    program_dir = os.path.join(miniapp_dir, args.folder)

    run_unpack_script(program_dir)
