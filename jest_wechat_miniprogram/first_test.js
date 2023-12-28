const automator = require("miniprogram-automator");

automator
  .launch({
    cliPath: "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat",
    projectPath: "C:\\Users\\zhiha\\WeChatProjects\\miniprogram-3",
  })
  .then(async (miniProgram) => {
    const page = await miniProgram.reLaunch("home");
    await page.waitFor(500);
    const element = await page.$("[placeholder='iphone 13 火热发售中']");
    console.log(await element.attribute("class"));
    await element.tap();

    await miniProgram.close();
  });
