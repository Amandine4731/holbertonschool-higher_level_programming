#!/usr/bin/node

const argv = process.argv;

const x = argv[2];

if (argv[2] && argv[2] > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
