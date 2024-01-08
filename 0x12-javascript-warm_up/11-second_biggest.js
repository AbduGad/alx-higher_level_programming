#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const numArgs = args.length;

if (numArgs === 0) {
  console.log(0);
} else if (numArgs === 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
