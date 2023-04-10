#!/usr/bin/node

const args = process.argv;
const list = [];

if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    list.push(Number(args[i]));
  }
  list.sort((lower, upper) => upper - lower);
  console.log(list[1]);
}
