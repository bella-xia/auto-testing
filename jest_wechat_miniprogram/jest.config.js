const { Config } = require("@jest/types");

const baseTestDir =
  "/home/bella-xia/auto-testing/jest_wechat_miniprogram/test3";

const config = {
  testEnvironment: "node",
  verbose: true,
  testMatch: [`${baseTestDir}/home.spec.js`],
  transform: {
    "^.+\\.js$": "babel-jest",
  },
};

module.exports = config;
