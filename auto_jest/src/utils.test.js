const assert = require("node:assert");
const { test, describe } = require("node:test");
const { toUpperCase } = require("./utils");

describe("node test trials", () => {
  test("toUpperCase", () => {
    const actual = toUpperCase("abc");
    const expected = "ABC";
    assert.strictEqual(actual, expected);
  });
});
