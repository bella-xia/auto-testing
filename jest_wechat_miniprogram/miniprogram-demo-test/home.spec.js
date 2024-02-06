const automator = require("miniprogram-automator");

describe("home page", () => {
  let miniProgram;
  let page;

  beforeAll(async () => {
    miniProgram = await automator.launch({
      cliPath: "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat",
      projectPath: "C:\\Users\\zhiha\\WeChatProjects\\miniprogram-3",
    });
  }, 300000);

  beforeEach(async () => {
    page = await miniProgram.reLaunch("/pages/home/home");
    await page.waitFor(500);
  }, 300000);

  afterAll(async () => {
    await miniProgram.close();
  });

  it("should find input box", async () => {
    const inputElement = await page.$(".t-search__input");
    expect(inputElement.tagName).toBe("input");
    expect(await inputElement.attribute("placeholder")).toBe(
      "iphone 13 火热发售中"
    );
  });

  it("should tap on input box to go to new page", async () => {
    const inputElement = await page.$(".t-search__input");
    expect(inputElement.tagName).toBe("input");
    expect(await inputElement.attribute("placeholder")).toBe(
      "iphone 13 火热发售中"
    );
    await inputElement.tap();
    await page.waitFor(3000);
    expect((await miniProgram.currentPage()).path).toBe(
      "pages/goods/search/index"
    );
  }, 300000);

  it("should accept custom search input", async () => {
    page = await miniProgram.navigateTo("/pages/goods/search/index");
    await page.waitFor(3000);
    const inputElement = await page.$(".t-search__input");
    expect(inputElement.tagName).toBe("input");
    //expect(await inputElement.attribute("placeholder")).toBe("iPhone12pro");
    await inputElement.input("电脑");
    expect(await inputElement.property("value")).toBe("电脑");
  }, 300000);

  it("should navigate to page with search result", async () => {
    const inputValue = "电脑";
    page = await miniProgram.navigateTo(
      `/pages/goods/result/index?searchValue=${inputValue}`
    );
    await page.waitFor(3000);
    expect((await miniProgram.currentPage()).path).toBe(
      "pages/goods/result/index"
    );
  }, 300000);
});
