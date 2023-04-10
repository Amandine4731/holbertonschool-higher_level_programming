#!/usr/bin/node

const args = process.argv;

if ((args[1] && !args[2]) || (args[1] && args[2] !== Number)) {
  console.log('Not a number');
} else if (args[2]) {
  console.log('My number: ' + Number(~~args[2]));
}
