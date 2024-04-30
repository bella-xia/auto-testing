const { exec } = require("child_process");

// Run npm test with additional options
const npmTestProcess = exec("npm test -- --detectOpenHandles --logHeapUsage");

let memoryUsage = 0;

// Parse npm test output to find memory usage information
npmTestProcess.stdout.on("data", (data) => {
  const output = data.toString();
  console.log(output); // Print npm test output

  // Parse output to extract memory usage (adjust this regex according to your npm test output)
  const memoryMatch = output.match(/(?:heapUsed: )(\d+)(?: kB)/);
  if (memoryMatch) {
    memoryUsage = parseInt(memoryMatch[1]);
  }
});

// Print any errors that occur during npm test execution
npmTestProcess.stderr.on("data", (data) => {
  console.error(`Error: ${data}`);
});

// Calculate overall memory usage after npm test completes
npmTestProcess.on("close", (code) => {
  console.log(`npm test process exited with code ${code}`);
  console.log(`Overall memory usage: ${memoryUsage} kB`);
});
