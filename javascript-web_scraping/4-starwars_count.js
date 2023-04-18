#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const urlId = 'api/people/18/';
const opts = {
  method: 'GET',
  url: argv[2]
};

request(opts, (err, res, body) => {
  if (err) {
    console.log('Error: ', err);
  } else {
    const parse = JSON.parse(body);
    let result = 0;
    for (const i of parse.results) {
      for (const j of i.characters) {
        if (j.includes(urlId)) {
          result += 1;
        }
      }
    }
    console.log(result);
  }
});
