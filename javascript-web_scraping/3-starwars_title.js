#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const uniqueId = Number(argv[2]);
const opts = {
  method: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/' + uniqueId
};

request(opts, (err, res, body) => {
  if (err) return console.log('Error: ', err);

  console.log(JSON.parse(body).title);
});
