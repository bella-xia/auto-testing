const automator = require("miniprogram-automator");

describe("home page", () => {
  let miniProgram;
  let page;

  beforeAll(async () => {
    miniProgram = await automator.launch({
      cliPath: "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat",
      projectPath: "C:\\Users\\zhiha\\WeChatProjects\\miniprogram-3",
    });
    page = await miniProgram.reLaunch("home");
    await page.waitFor(500);
  }, 300000);

  afterAll(async () => {
    await miniProgram.close();
  });

  it("input box", async () => {
    const input = await page.$(".t-search__input");
    expect(input.tagName).toBe("input");
    expect(await input.attribute("placeholder")).toBe("iphone 13 火热发售中");
  });
});
