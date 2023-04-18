#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const newDict = {};
const opts = {
  method: 'GET',
  url: argv[2]
};
request(opts, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const parse = JSON.parse(body);
    let result = 0;
    let user = 1;
    for (user; user < parse.length + 1; user++) {
      result = 0;
      for (const i of parse) {
        if (i.userId === user) {
          if (i.completed === true) {
            result += 1;
          }
        }
      }
      if (result > 0) {
        newDict[user] = result;
      }
    }
    console.log(newDict);
  }
});
