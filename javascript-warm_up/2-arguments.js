#!/usr/bin/node

const argc = process.argv.length;

let test;
if (argc === 2) { test = 'No argument'; } else if (argc === 3) { test = 'Argument found'; } else { test = 'Arguments found'; }
console.log(test);
