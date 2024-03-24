const automator = require("miniprogram-automator");

const cliPath =
  "/home/bella-xia/wechat-web-devtools-linux/bin/wechat-devtools-cli";
const projectPath = "/home/bella-xia/auto-testing/data/miniprogram-copy/";
const str_exp = "string";

describe("test all pages", () => {
  let page;
  let miniProgram;

  beforeAll(async () => {
    try {
      miniProgram = await automator.launch({
        cliPath: cliPath,
        projectPath: projectPath,
      });
      const systemInfo = await miniProgram.systemInfo();
      console.log(systemInfo);
    } catch (err) {
      console.error(
        `Error reading JSON file or launching automator for program:`,
        err
      );
    }
  }, 300000);

  afterAll(async () => {
    await miniProgram.close();
  }, 300000);

  afterEach(async () => {
    page = null;
  }, 300000);

  it("testing input result", async () => {
    const page_name = "/pages/index/index";
    try {
      page = await miniProgram.navigateTo(page_name);
    } catch (err) {
      page = await miniProgram.switchTab(page_name);
    }
    const inputElements = await page.$$("input");
    for (const inputElement of inputElements) {
      if (inputElement !== null) {
        try {
          console.log(await inputElement.outerWxml());
          // await inputElement.input(str_exp);
          await inputElement.trigger("change", { value: str_exp });
          await page.waitFor(1000);
        } catch (error) {
          console.log("An error occurred:", error.message);
        }
      }
    }
    const form_btn = await page.$(".enter-page");
    await form_btn.tap();
    await page.waitFor(10000);
  }, 300000);
});
