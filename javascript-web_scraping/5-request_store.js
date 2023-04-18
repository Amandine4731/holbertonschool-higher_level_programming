#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const argv = process.argv;
const filename = argv[3];
const opts = {
  method: 'GET',
  url: argv[2]
};

request(opts, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, err => {
      if (err) { console.log(err); }
    });
  }
});
