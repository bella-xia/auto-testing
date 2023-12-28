import {
  OtherStringUtils,
  calculateComplexity,
  toUpperCaseWithCallback,
} from "../../app/doubles/otherUtils";

describe("OtherUtils test suite", () => {
  describe("OtherStringUtils tests with spies", () => {
    let sut: OtherStringUtils;

    beforeEach(() => {
      sut = new OtherStringUtils();
    });

    test("Use a spy to track calls", () => {
      const toUpperCaseSpy = jest.spyOn(sut, "toUpperCase");
      sut.toUpperCase("asa");
      expect(toUpperCaseSpy).toHaveBeenCalledWith("asa");
    });

    test("Use a spy to track calls to other module", () => {
      const consoleLogSpy = jest.spyOn(console, "log");
      sut.logString("asa");
      expect(consoleLogSpy).toHaveBeenCalledWith("asa");
    });

    // replace the functionality of a function through spy
    test("Use a spy to replace the implementation of a method", () => {
      jest
        .spyOn(sut, "callExternalService")
        .mockImplementation(() =>
          console.log("calling mocked implementation!!!")
        );
      sut.callExternalService();
    });
  });
  // mocks
  describe("Tracking callbacks with Jest mocks", () => {
    const callBackMock = jest.fn();

    afterEach(() => {
      jest.clearAllMocks();
    });

    it("ToUpperCase - calls callback for invalid argument", () => {
      const actual = toUpperCaseWithCallback("", callBackMock);
      expect(actual).toBeUndefined;
      expect(callBackMock).toHaveBeenCalledWith("Invalid argument!");
      expect(callBackMock).toHaveBeenCalledTimes(1);
    });

    it("ToUpperCase - calls callback for valid argument", () => {
      const actual = toUpperCaseWithCallback("abc", callBackMock);
      expect(actual).toBe("ABC");
      expect(callBackMock).toHaveBeenCalledWith("called function with abc");
      expect(callBackMock).toHaveBeenCalledTimes(1);
    });
  });
  describe("Tracking callbacks", () => {
    let cbArgs = [];
    let timesCalled = 0;
    function callBackModel(arg: string) {
      cbArgs.push(arg);
      timesCalled++;
    }

    afterEach(() => {
      cbArgs = [];
      timesCalled = 0;
    });

    it("ToUpperCase - calls callback for invalid argument", () => {
      const actual = toUpperCaseWithCallback("", callBackModel);
      expect(actual).toBeUndefined;
      expect(cbArgs).toContain("Invalid argument!");
      expect(timesCalled).toBe(1);
    });

    it("ToUpperCase - calls callback for valid argument", () => {
      const actual = toUpperCaseWithCallback("abc", callBackModel);
      expect(actual).toBe("ABC");
      expect(cbArgs).toContain("called function with abc");
      expect(timesCalled).toBe(1);
    });
  });

  it("Calculates complexity", () => {
    const someInfo = {
      length: 5,
      extraInfo: {
        field1: "someInfo",
        field2: "someOtherInfo",
      },
    };
    const actual = calculateComplexity(someInfo as any);
    expect(actual).toBe(10);
  });
});
