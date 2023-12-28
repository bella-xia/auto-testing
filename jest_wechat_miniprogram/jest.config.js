const { Config } = require("@jest/types");

//const baseDir = "<rootDir>/src/app/server_app";
//const baseTestDir = "<rootDir>/src/test/server_app";

const baseTestDir = "<rootDir>/miniprogram-demo-test";

const config = {
  testEnvironment: "node",
  verbose: true,
  testMatch: [`${baseTestDir}/*.js`],
};

module.exports = config;
