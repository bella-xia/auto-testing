const automator = require("miniprogram-automator");

const cliPath = "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat";
const projectPath = "C:\\Users\\zhiha\\WeChatProjects\\miniprogram-8";
const pages_info = [];
const input_elements = [];

describe("test all pages", () => {
  let miniProgram;
  let page;
  // let pages_info;

  beforeAll(async () => {
    // const json_file_path = projectPath + "\\miniprogram\\app.json";
    // const fs = require("fs").promises; // Use fs.promises

    // try {
    //   const data = await fs.readFile(json_file_path, "utf8");
    //   const jsonData = JSON.parse(data);
    //   pages_info = jsonData.pages;
    //   console.log(pages_info);
    // } catch (err) {
    //   console.error("Error reading JSON file:", err);
    // }
    const json_file_path = projectPath + "\\miniprogram\\app.json";
    const fs = require("fs").promises;

    try {
      const data = await fs.readFile(json_file_path, "utf8");
      const jsonData = JSON.parse(data);
      pages_info_data = jsonData.pages;
      for (const page of pages_info_data) {
        pages_info.push(page);
      }
      console.log(pages_info);

      miniProgram = await automator.launch({
        cliPath: cliPath,
        projectPath: projectPath,
      });
    } catch (err) {
      console.error("Error reading JSON file or launching automator:", err);
    }
    // await fs.readFile(json_file_path, "utf8", (err, data) => {
    //   if (err) {
    //     console.error("Error reading JSON file:", err);
    //     return;
    //   }
    //   const jsonData = JSON.parse(data);
    //   pages_info = jsonData.pages;
    // });
    // console.log(pages_info);

    // miniProgram = await automator.launch({
    //   cliPath: cliPath,
    //   projectPath: projectPath,
    // });

    // If you need to reLaunch with the first page, you can uncomment the following line
    // page = await miniProgram.reLaunch("/" + pages_info[0]);
  }, 300000);

  afterAll(async () => {
    await miniProgram.close();
  }, 300000);

  afterEach(async () => {
    // Reset the page before each test case
    page = null;
  }, 300000);

  it("should get all the miniprogram pages", async () => {
    console.log("successfully launched miniprogram");
    console.log(pages_info);
  }, 300000);

  it("iterate over all the pages", async () => {
    console.log(pages_info);
    for (const page_name of pages_info) {
      console.log(page_name);
      page = await miniProgram.reLaunch("/" + page_name);
      await page.waitFor(500);
      const inputElements = await page.$$("input");
      console.log(inputElements.length);
      // input_elements.push({
      //   num: inputElements.length,
      //   //placeholder: ele.placeholder,
      //   page: page_name,
      // });
      for (const ele of inputElements) {
        input_elements.push({
          id: ele.id,
          value: await ele.property("value"),
          placeholder: await ele.property("placeholder"),
          page: page_name,
        });
        console.log(ele.id);
        // console.log(await ele.property("value"));
        // console.log(await ele.property("placeholder"));
        // console.log(await ele.property("id"));
        // console.log(await ele.property("class"));
      }
    }
    console.log(input_elements);
  }, 300000);

  it("iterate over all the inputs", async () => {
    const str_exp = "string_example";
    for (const ele of input_elements) {
      // console.log(ele.page);
      // console.log(ele.num);
      page = await miniProgram.reLaunch("/" + ele.page);
      await page.waitFor(1000);
      const inputElement = await page.$(
        `input[value="${ele.value}"][placeholder="${ele.placeholder}"]`
      );
      expect(inputElement.tagName).toBe("input");
      // expect(inputElement.id).toBe(ele.id);
      expect(await inputElement.property("value")).toBe(ele.value);
      expect(await inputElement.property("placeholder")).toBe(ele.placeholder);
      console.log(inputElement);
      // expect(inputElement.length).toBe(ele.num);
      // for (const ele of inputElement) {
      //   expect(ele.tagName).toBe("input");
      //   await ele.input(str_exp);
      //   expect(await ele.property("value")).toBe(str_exp);
      // }
      // const inputElement = await page.$(`input[id=${ele.id}]`);
      // console.log(inputElement);

      // console.log(`testing element ${ele.id} on page ${ele.page}`);
    }
  }, 300000);

  it("inserting values to each input", async () => {
    const str_exp = "string_example";
    for (const ele of input_elements) {
      // console.log(ele.page);
      // console.log(ele.num);
      page = await miniProgram.reLaunch("/" + ele.page);
      await page.waitFor(1000);
      const inputElement = await page.$(
        `input[value="${ele.value}"][placeholder="${ele.placeholder}"]`
      );
      await inputElement.input(str_exp);
      expect(await inputElement.property("value")).toBe(str_exp);

      // expect(inputElement.length).toBe(ele.num);
      // for (const ele of inputElement) {
      //   expect(ele.tagName).toBe("input");
      //   await ele.input(str_exp);
      //   expect(await ele.property("value")).toBe(str_exp);
      // }
      // const inputElement = await page.$(`input[id=${ele.id}]`);
      // console.log(inputElement);

      // console.log(`testing element ${ele.id} on page ${ele.page}`);
    }
  }, 300000);

  // input_elements.forEach((ele_id, ele_page) => {
  //   it("iterate over all the inputs", async () => {
  //     console.log(`testing element ${ele_id}`);
  //   });
  // });

  // it.each(pages_info)(
  //   "check if the input elements are present on page %s",
  //   async (page_name) => {
  //     page = await miniProgram.reLaunch("/" + page_name);
  //     await page.waitFor(500);
  //     const inputElements = await page.$$("input");
  //     console.log(inputElements.length);
  //     // Add your assertions or further test logic here
  //   },
  //   300000
  // );

  // pages_info.forEach(async (page_name, index) => {
  //   page = await miniProgram.reLaunch("/" + page_name);
  //   const inputElement = await page.$$("input");
  //   console.log(inputElement);
  //   await page.waitFor(500);
  // }, 300000);

  // for (const page_name in pages_info) {
  //   console.log("Processing page:", page_name);
  //   it("should find input box", async () => {
  //     const inputElement = await page.$$("input");
  //     console.log(inputElement);
  //     // expect(inputElement.tagName).toBe("input");
  //     // expect(await inputElement.attribute("placeholder")).toBe(
  //     //   "iphone 13 火热发售中"
  //     // );
  //   });

  //   it.skip("should tap on input box to go to new page", async () => {
  //     const inputElement = await page.$(".t-search__input");
  //     expect(inputElement.tagName).toBe("input");
  //     expect(await inputElement.attribute("placeholder")).toBe(
  //       "iphone 13 火热发售中"
  //     );
  //     await inputElement.tap();
  //     await page.waitFor(3000);
  //     expect((await miniProgram.currentPage()).path).toBe(
  //       "pages/goods/search/index"
  //     );
  //   }, 300000);

  //   it.skip("should accept custom search input", async () => {
  //     page = await miniProgram.navigateTo("/pages/goods/search/index");
  //     await page.waitFor(3000);
  //     const inputElement = await page.$(".t-search__input");
  //     expect(inputElement.tagName).toBe("input");
  //     //expect(await inputElement.attribute("placeholder")).toBe("iPhone12pro");
  //     await inputElement.input("电脑");
  //     expect(await inputElement.property("value")).toBe("电脑");
  //   }, 300000);

  //   it.skip("should navigate to page with search result", async () => {
  //     const inputValue = "电脑";
  //     page = await miniProgram.navigateTo(
  //       `/pages/goods/result/index?searchValue=${inputValue}`
  //     );
  //     await page.waitFor(3000);
  //     expect((await miniProgram.currentPage()).path).toBe(
  //       "pages/goods/result/index"
  //     );
  //   }, 300000);
  // }
});

// const cliPath = "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat";
// const projectPath = "C:\\Users\\zhiha\\WeChatProjects\\miniprogram-1";

// before testing, get all the pages
