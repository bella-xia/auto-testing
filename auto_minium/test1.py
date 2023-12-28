import minium

project_path = r"C:\Users\zhiha\WeChatProjects\miniprogram-3"
dev_tool_path = r"C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
mini = minium.Minium({
    "project_path": project_path,   # 替换成你的【小程序项目目录地址】
    "dev_tool_path": dev_tool_path,      # 替换成你的【开发者工具cli地址】，macOS: <安装路径>/Contents/MacOS/cli， Windows: <安装路径>/cli.bat
})
print(mini.get_system_info())