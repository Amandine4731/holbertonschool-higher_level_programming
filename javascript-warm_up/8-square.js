#!/usr/bin/node

const argv = process.argv;

const x = argv[2];
const y = argv[2];

if (argv[2] >= 0 || argv[2] < 0) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < y - 1; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('X');
    console.log('');
  }
} else if (argv[2] !== Number) {
  console.log('Missing size');
}
