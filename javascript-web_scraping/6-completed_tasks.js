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
    for (user; user < parse.length; user++) {
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
/*
#!/usr/bin/node

const request = require('request');
const argv = process.argv;
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

*/
