import os, sys
from collections import defaultdict

COMP_SET = {"js", "json", "wxml", "wxss"}
IGNORE_SET = {"png", "jpg"}

def get_all_page_dir(pages_path : str) -> list[str]:
    all_pages_dir: list[str] = []
    if os.path.isdir(pages_path):
        curr_dirs = os.listdir(pages_path)
        for curr_dir in curr_dirs:
            if curr_dir == "pages":
                all_pages_dir.append(os.path.join(pages_path, "pages"))
            else:
                all_pages_dir.extend(get_all_page_dir(os.path.join(pages_path, curr_dir)))
    return all_pages_dir

def get_files(root_path : str, miniprogram_name : str) -> tuple[list[str], list[str]]:
    pages_path : str = os.path.join(root_path, miniprogram_name)
    pages_dirs: list[str] = get_all_page_dir(pages_path)
    corr_pages = []
    miss_pages = []
    for pages_dir in pages_dirs:
        corr_page, miss_page = check_page(pages_dir)
        corr_pages.extend(corr_page)
        miss_pages.extend(miss_page)
    
    return corr_pages, miss_pages

def check_page(page_path : str) -> tuple[list[str], list[str]]:
    print(f"querying path {page_path}")
    corr_pages: list[str] = []
    miss_pages: list[str] = []
    page_comp: list[str] = os.listdir(page_path)
    page_eles: defaultdict[str, set[str]] = defaultdict(set[str])
    for comp in page_comp:
        if os.path.isdir(os.path.join(page_path, comp)):
            inner_page = os.path.join(page_path, comp)
            inner_corr_pages, inner_miss_pages = check_page(inner_page)
            corr_pages.extend(inner_corr_pages)
            miss_pages.extend(inner_miss_pages)
        else:
            comp_name = comp.split(".")[0]
            comp_name = page_path.split("\\")[-1] if comp_name == "index" else comp_name
            ele_name = comp.split(".")[-1]
            if ele_name not in IGNORE_SET:
                page_eles[comp_name].add(ele_name)
    
    for comp_name, ele_names in page_eles.items():
        num_unmatched = 0
        for expected_comp in COMP_SET:
                if expected_comp not in ele_names:
                    num_unmatched += 1
        if num_unmatched != 4:
            if num_unmatched != 0:
                print(f"expected 4 elements but did not get on page {comp_name}, missing {num_unmatched}.")
                miss_pages.append(comp_name)
            else:
                corr_pages.append(comp_name)
    return corr_pages, miss_pages
        
if __name__ == "__main__":

    ROOT_PATH = "C:\\Users\\zhiha\\OneDrive\\Desktop\\miniapp_data\\unpacked_data_unveilr"
    MINIRPOGRAM = "wx1e6b470745deccfd-pc"
    FILE_NAME = "C:\\Users\\zhiha\\OneDrive\\Desktop\\miniapp_data\\utils\\logger.txt"
    original_stdout = sys.stdout
    corr_pages = []
    miss_pages = []
    try:
    # Open the file in append mode ('a')
        with open(FILE_NAME, 'a') as file:
            sys.stdout = file
            corr_pages, miss_pages = get_files(ROOT_PATH, MINIRPOGRAM)
    except FileNotFoundError:
    # If the file does not exist, create it and then append content
        with open(FILE_NAME, 'w') as file:
            sys.stdout = file
            corr_pages, miss_pages = get_files(ROOT_PATH, MINIRPOGRAM)
    except Exception as e:
        print("An error occurred:", e)
        exit
    sys.stdout = original_stdout
    print("correct pages: ", corr_pages)
    print("")
    print("missing pages: ", miss_pages)
