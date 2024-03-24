const automator = require("miniprogram-automator");

const cliPath =
  "/home/bella-xia/wechat-web-devtools-linux/bin/wechat-devtools-cli";
const projectPath = "/home/bella-xia/auto-testing/data/wechat-weapp-movie/";
const str_exp = "string";

describe("test all pages", () => {
  let page;
  const screen_shot_file =
    "/home/bella-xia/auto-testing/jest_wechat_miniprogram/miniprogram-demo-test3/screenshots/";
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

  it.skip("testing input result", async () => {
    const page_name = "/pages/editPersonInfo/editPersonInfo";
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
          //await inputElement.tap();
          // await inputElement.input(str_exp);
          await inputElement.trigger("change", { value: str_exp });
          await page.waitFor(1000);
        } catch (error) {
          console.log("An error occurred:", error.message);
        }
      }
    }
    const form_btn = await page.$(".edit-btn");
    await form_btn.tap();
    await page.waitFor(5000);

    page = await miniProgram.currentPage();

    const textElements = await page.$$(".cell-ft");
    for (const textEle of textElements) {
      console.log(await textEle.outerWxml());
    }
  }, 300000);

  it.skip("testing form submission", async () => {
    const page_name = "/pages/editPersonInfo/editPersonInfo";
    try {
      page = await miniProgram.navigateTo(page_name);
    } catch (err) {
      page = await miniProgram.switchTab(page_name);
    }
    const formElement = await page.$("form");
    console.log(await formElement.outerWxml());
    formElement.trigger("submit", {
      value: {
        name: "str",
        nickName: "string",
        gender: "g",
        age: 11,
        birthday: "str",
        constellation: "str",
        company: "string",
        school: "string",
        tel: "string",
        email: "string",
        intro: "string",
      },
    });

    //const form_btn = await page.$(".edit-btn");
    //await form_btn.tap();
    await page.waitFor(5000);

    page = await miniProgram.currentPage();

    const textElements = await page.$$(".cell-ft");
    for (const textEle of textElements) {
      console.log(await textEle.outerWxml());
    }
  }, 300000);

  it("testing automatic form submission", async () => {
    const page_name = "/pages/editPersonInfo/editPersonInfo";
    try {
      page = await miniProgram.navigateTo(page_name);
    } catch (err) {
      page = await miniProgram.switchTab(page_name);
    }
    const formElement = await page.$("form");
    const inputElements = await formElement.$$("input");
    const inputArrays = {};
    for (const inputElement of inputElements) {
      inputArrays[await inputElement.property("name")] = str_exp;
    }
    formElement.trigger("submit", {
      value: inputArrays,
    });

    //const form_btn = await page.$(".edit-btn");
    //await form_btn.tap();
    await page.waitFor(5000);

    page = await miniProgram.currentPage();

    const textElements = await page.$$(".cell-ft");
    for (const textEle of textElements) {
      expect(await textEle.text()).toBe(str_exp);
    }
  }, 300000);
});
