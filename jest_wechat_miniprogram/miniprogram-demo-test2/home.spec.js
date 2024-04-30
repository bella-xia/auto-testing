import { project_and_pages } from "./data";

const automator = require("miniprogram-automator");

const cliPath = "C:/Program Files (x86)/Tencent/微信web开发者工具/cli.bat";
const projectPath = "C:/Users/zhiha/OneDrive/Desktop/auto-testing/data/";
const str_exp = "string_example";

describe("test all pages", () => {
  let page;
  let screen_shot_file =
    "C:/Users/zhiha/OneDrive/Desktop/auto-testing/jest_wechat_miniprogram/miniprogram-demo-test2/screenshots/";

  project_and_pages.forEach(async (project_info) => {
    const projectFullPath = projectPath + project_info["app_name"] + "/";
    const pages_info = project_info["page_list"];
    const input_elements = [];
    const ss_file = screen_shot_file + project_info["app_name"];
    let miniProgram;
    beforeAll(async () => {
      try {
        miniProgram = await automator.launch({
          cliPath: cliPath,
          projectPath: projectFullPath,
        });
      } catch (err) {
        console.error(
          `Error reading JSON file or launching automator for program ${project_info["app_name"]}:`,
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

    it.skip("should get all the miniprogram pages", async () => {
      console.log("successfully launched miniprogram");
      console.log(pages_info);
    }, 300000);

    it.each(pages_info)(
      `check if the input elements are present on program ${project_info["app_name"]} page %s`,
      async (page_name) => {
        if (page_name !== null) {
          try {
            page = await miniProgram.navigateTo("/" + page_name);
          } catch (err) {
            page = await miniProgram.switchTab("/" + page_name);
          }
          // await page.waitFor(500);
          const inputElements = await page.$$("input");
          for (const inputElement of inputElements) {
            if (inputElement !== null) {
              try {
                await inputElement.input(str_exp);
              } catch (error) {
                console.log("An error occurred:", error.message);
              }
              // console.log(
              //   "saving screenshot to",
              //   ss_file + inputElement.id + ".png"
              // );
              // await miniProgram.screenshot({
              //   path: ss_file + inputElement.id + ".png",
              // });
            }
          }
          page = await miniProgram.navigateBack();
        }
      },
      300000
    );

    it.skip("iterate over all the pages", async () => {
      console.log(pages_info);
      for (const page_name of pages_info) {
        console.log(page_name);
        page = await miniProgram.navigateTo("/" + page_name);
        await page.waitFor(500);
        const inputElements = await page.$$("input");
        console.log(inputElements.length);
        for (const ele of inputElements) {
          input_elements.push({
            id: ele.id,
            value: await ele.property("value"),
            placeholder: await ele.property("placeholder"),
            page: page_name,
          });
          console.log(ele.id);
        }
      }
      console.log(input_elements);
    }, 300000);

    it.skip("iterate over all the inputs", async () => {
      for (const ele of input_elements) {
        page = await miniProgram.reLaunch("/" + ele.page);
        await page.waitFor(1000);
        const inputElement = await page.$(
          `input[value="${ele.value}"][placeholder="${ele.placeholder}"]`
        );
        expect(inputElement.tagName).toBe("input");
        expect(await inputElement.property("value")).toBe(ele.value);
        expect(await inputElement.property("placeholder")).toBe(
          ele.placeholder
        );
        console.log(inputElement);
      }
    }, 300000);

    it.skip("inserting values to each input", async () => {
      const str_exp = "string_example";
      for (const ele of input_elements) {
        page = await miniProgram.reLaunch("/" + ele.page);
        await page.waitFor(1000);
        const inputElement = await page.$(
          `input[value="${ele.value}"][placeholder="${ele.placeholder}"]`
        );
        if (inputElement !== null) {
          try {
            await inputElement.input(str_exp);
          } catch (error) {
            if (error instanceof TypeError) {
              console.log(
                "TypeError occurred on stopPropagation",
                error.message
              );
            } else {
              console.log("An error occurred:", error.message);
            }
          }
        }
      }
    }, 300000);
  }, 300000000);
});
