#!/usr/bin/node

const args = process.argv;

if (0 > args[2] > 0) {
  console.log(('My number: ' + Number(~~args[2])));
} else if ((args[1] && !args[2]) || (args[1] && args[2] !== Number)) {
  console.log('Not a number');
}