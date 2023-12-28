import { StringUtils, getStringInfo, toUpperCase } from "../app/Utils";

describe("Utils test suite", () => {
  // hooks: beforeall; afterall; beforeeach, aftereach
  // xit: it.skip
  // fit: it.only
  describe("StringUtils tests", () => {
    let sut: StringUtils;
    beforeEach(() => {
      sut = new StringUtils();
    });

    afterEach(() => {
      // clearing mocks
    });

    it.todo("test long strings");

    it("should return uppercase of a valid string", () => {
      const actual = sut.toUpperCase("abc");
      expect(actual).toBe("ABC");
    });

    it("Should throw error on invalid argument method 1", () => {
      function expectError() {
        const actual = sut.toUpperCase("");
      }
      expect(expectError).toThrow();
    });

    it("Should throw error on invalid argument method 2", () => {
      expect(() => {
        sut.toUpperCase("");
      }).toThrow();
    });

    it("Should throw error on invalid argument method 3: try-catch block", (done) => {
      // there is a problem:
      //  if no error is thrown, this test will still pass
      try {
        sut.toUpperCase("");
        done("GetStringInfo should throw error for invalid argument");
      } catch (error) {
        expect(error).toBeInstanceOf(Error);
        expect(error).toHaveProperty("message", "Invalid argument");
        done();
      }
    });
  });

  describe("ToUpperCase examples", () => {
    it.each([
      { input: "abc", expected: "ABC" },
      { input: "My-String", expected: "MY-STRING" },
      { input: "def", expected: "DEF" },
    ])("$input toUpperCase should be $expected", ({ input, expected }) => {
      const sut = toUpperCase;
      // act:
      const actual = sut(input);
      expect(actual).toBe(expected);
    });
  });

  describe.skip("getStringInfo for arg My-String should", () => {
    test("return right length", () => {
      const actual = getStringInfo("My-String");
      //expect(actual.characters.length).toBe(9);
      expect(actual.characters).toHaveLength(9);
    });

    test("return right lower case", () => {
      const actual = getStringInfo("My-String");
      expect(actual.lowerCase).toBe("my-string");
    });

    test("return right upper case", () => {
      const actual = getStringInfo("My-String");
      expect(actual.upperCase).toBe("MY-STRING");
    });

    test("return right characters", () => {
      const actual = getStringInfo("My-String");
      expect(actual.characters).toEqual([
        "M",
        "y",
        "-",
        "S",
        "t",
        "r",
        "i",
        "n",
        "g",
      ]);
      expect(actual.characters).toContain<string>("M");
      expect(actual.characters).toEqual(
        expect.arrayContaining(["y", "-", "M", "i", "n", "g", "S", "t", "r"])
      );
    });

    test("return defined extra info", () => {
      const actual = getStringInfo("My-String");

      // three ways of checking defined
      expect(actual.extraInfo).not.toBeUndefined();
      expect(actual.extraInfo).not.toBe(undefined);
      expect(actual.extraInfo).toBeDefined();
      expect(actual.extraInfo).toBeTruthy();
    });

    test("return rightextra info", () => {
      const actual = getStringInfo("My-String");
      // when working with primitive type, use toBe
      // when working with objects, use toEqual
      expect(actual.extraInfo).toEqual({});
    });
  });
});
