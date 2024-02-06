const cliPath = "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat";
const projectPath = "C:\\Users\\zhiha\\WeChatProjects\\miniprogram-1";
let pages_info = [];

async function readJsonFile() {
  const json_file_path = projectPath + "\\miniprogram\\app.json";
  const fs = require("fs").promises; // Use fs.promises

  try {
    const data = await fs.readFile(json_file_path, "utf8");
    const jsonData = JSON.parse(data);
    pages_info = jsonData.pages;
    console.log(pages_info);
  } catch (err) {
    console.error("Error reading JSON file:", err);
  }
}

readJsonFile(); // Call the async function

const pages = pages_info;
console.log(Array.isArray(pages));
