const { Config } = require("@jest/types");

//const baseDir = "<rootDir>/src/app/server_app";
//const baseTestDir = "<rootDir>/src/test/server_app";

const baseTestDir = "<rootDir>/miniprogram-demo-test2";

const config = {
  testEnvironment: "node",
  verbose: true,
  // setupFiles: [`${baseTestDir}/jest.setup.js`],
  setupFilesAfterEnv: [`${baseTestDir}/jest.setup.js`],
  testMatch: [`${baseTestDir}/home.spec.js`],
};

module.exports = config;
