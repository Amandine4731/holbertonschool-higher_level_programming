#!/usr/bin/node

const args = process.argv;
const argc = process.argv.lenght;

if (args[2] && args[3]) { console.log(args[2] + ' is ' + args[3]); } else if (args[2] && !args[3]) { console.log(args[2] + ' is ' + 'undefined'); } else if (!args[2] && !args[3]) { console.log('undefined' + ' is ' + 'undefined'); }
