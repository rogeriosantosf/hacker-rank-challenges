"use strict";
// startup of node stdin
process.stdin.resume();
process.stdin.setEncoding("utf-8");

// variables to control the input
let inputString = "";
let currentLine = 0;

// listeners to the data event streams
process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  run();
});

// read a line from standard input
function readLine() {
  return inputString[currentLine++];
}

// write a line to standard output
function writeLine(data) {
  console.log(data);
}

function run() {
  main();
}
