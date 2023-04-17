#!/usr/bin/node

const argv = process.argv;
if (argv.length < 3) {
  console.log('FILENAME');
}
const fs = require('fs');
const filename = argv[2];
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
