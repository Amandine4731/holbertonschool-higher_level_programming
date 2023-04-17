#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const filename = argv[2];
const data = argv[3];
fs.writeFile(filename, data, 'UTF-8', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
