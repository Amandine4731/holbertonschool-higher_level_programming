#!/usr/bin/node

const argv = process.argv;

const a = argv[2];
const b = argv[3];

function add (a, b) {
  if (argv[2] && argv[3]) {
    console.log(Number(a) + Number(b));
  } else {
    console.log('NaN');
  }
}

add(a, b);
