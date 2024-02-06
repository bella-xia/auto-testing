import minium, os, sys
from test_json import page_query
from test_minium import minium_query
import unittest

project_path = "C:\\Users\\zhiha\\OneDrive\\Desktop\\auto-testing\\auto_minium\\data"
dev_tool_path = "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat"



if __name__ == "__main__":

    # get project name
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
        print("Querying into miniprogram:", project_name)
    else:
        Exception("no miniprogram name provided")
    
    full_program_path = os.path.join(project_path, project_name)
    project_pages = page_query(project_name)
    pages = project_pages.get_pages()

    mini = minium.Minium({
    "project_path": full_program_path,   # 替换成你的【小程序项目目录地址】
    "dev_tool_path": dev_tool_path,      # 替换成你的【开发者工具cli地址】，macOS: <安装路径>/Contents/MacOS/cli， Windows: <安装路径>/cli.bat
    })
    mq = minium_query(mini)
    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(minium_query)
    result = unittest.TextTestRunner().run(loaded_suite)
    print(result)
    mq.test_get_sysyem_info()
