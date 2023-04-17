#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const myUrl = argv[2];
const opts = {
  method: 'GET',
  url: myUrl
};

request(opts, (err, res, body) => {
  if (err) return console.log('Error: ', err);

  console.log('code: %d', res.statusCode);
});
